#!/usr/bin/env python3
"""Package skills into LLM-consumable formats.

Reads skills from src/sellersprite_cli/skills/ (comprehensive/ + tactical/),
resolves reference links to src/sellersprite_cli/reference/*.md,
and produces:
  - dist/skills-system-prompt.md  (single file for system prompt injection)
  - dist/skills.json               (structured data for programmatic use)
"""

import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / "src" / "sellersprite_cli" / "skills"
REFERENCE_DIR = ROOT / "src" / "sellersprite_cli" / "reference"
DIST_DIR = ROOT / "output"
PYPROJECT_FILE = ROOT / "pyproject.toml"

# Regex to find reference links in skill files
REF_LINK_RE = re.compile(r"- \[`([a-z_]+)`\]\([^)]+\)")


def extract_inline_docs(tool_name: str) -> str:
    """Extract key sections from a reference doc for inlining."""
    ref_file = REFERENCE_DIR / f"{tool_name}.md"
    if not ref_file.exists():
        return f"> 引用文档缺失: {tool_name}.md\n"

    content = ref_file.read_text(encoding="utf-8")
    parts = []

    # Extract ### 参数 section
    param_match = re.search(r"## 参数\n\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if param_match:
        parts.append("参数表:")
        parts.append(param_match.group(1).strip())

    # Extract ### 基本信息 section (Method/URL)
    basic_match = re.search(r"## 基本信息\n\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if basic_match:
        parts.append("基本信息:")
        parts.append(basic_match.group(1).strip())

    # Extract ### 请求示例 section
    example_match = re.search(r"## 请求示例\n\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if example_match:
        parts.append("请求示例:")
        parts.append(example_match.group(1).strip())

    if not parts:
        return content.strip()

    return "\n\n".join(parts)


def parse_skill(md_file: Path) -> dict:
    """Parse a single skill markdown file."""
    content = md_file.read_text(encoding="utf-8")

    # Extract title: prefer # heading, fallback to first non-empty line
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        first_line = next((line.strip() for line in content.splitlines() if line.strip()), "")
        title = first_line if first_line else md_file.stem

    # Extract referenced tools from ## 参考文档 section
    ref_section_match = re.search(r"## 参考文档.*?\n(.*?)(?=\n---|\Z)", content, re.DOTALL)
    tools = []
    if ref_section_match:
        tools = REF_LINK_RE.findall(ref_section_match.group(1))

    # Build inlined API docs
    api_docs = {}
    for tool in tools:
        api_docs[tool] = extract_inline_docs(tool)

    # Skill body: everything before ## 参考文档 (or the --- before it)
    body = content
    ref_marker = re.search(r"\n---\n\n## 参考文档", body)
    if ref_marker:
        body = body[:ref_marker.start()].strip()
    else:
        # Fallback: just strip trailing --- if present
        body = body.rstrip().rstrip("-").strip()

    # Determine category from parent directory
    category = md_file.parent.name

    return {
        "name": title,
        "slug": md_file.stem,
        "category": category,
        "content": body,
        "referenced_tools": tools,
        "api_docs": api_docs,
    }


def build_system_prompt(skills: list[dict]) -> str:
    """Build a single markdown file suitable for system prompt injection."""
    lines = [
        "# SellerSprite Skills System Prompt",
        "",
        "你是一名跨境电商选品专家，掌握以下 SellerSprite 数据技能。当用户提出相关需求时，请按照对应 Skill 的步骤、参数和逻辑执行。",
        "",
        "## 技能体系总览",
        "",
        "| 技能名称 | 类别 | 触发方式 | 核心场景 |",
        "|---------|------|----------|----------|",
    ]

    for skill in skills:
        cat_label = "综合分析" if skill["category"] == "comprehensive" else "战术选品"
        trigger = "`/命令`" if skill["category"] == "comprehensive" else "对话引用"
        # Extract first line of content as brief description
        desc = skill["content"].splitlines()[0][:30] if skill["content"] else ""
        lines.append(f"| {skill['name']} | {cat_label} | {trigger} | {desc}... |")

    lines.extend(["", "---", ""])

    for i, skill in enumerate(skills, 1):
        lines.append(f"## Skill {i}: {skill['name']}")
        lines.append("")
        lines.append(f"类别: {'综合分析' if skill['category'] == 'comprehensive' else '战术选品'} | slug: `{skill['slug']}`")
        lines.append("")
        lines.append(skill["content"])
        lines.append("")

        if skill["referenced_tools"]:
            lines.append("### 引用的 API 参数")
            lines.append("")
            for tool in skill["referenced_tools"]:
                lines.append(f"#### {tool}")
                lines.append("")
                lines.append(skill["api_docs"][tool])
                lines.append("")

        lines.extend(["---", ""])

    return "\n".join(lines)


def read_project_version() -> str:
    """Read version via importlib.metadata, fallback to pyproject.toml."""
    try:
        from importlib.metadata import version as _version, PackageNotFoundError
        try:
            return _version("sellersprite-cli")
        except PackageNotFoundError:
            pass
    except ImportError:
        pass

    content = PYPROJECT_FILE.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if not match:
        raise RuntimeError(f"version not found in {PYPROJECT_FILE}")
    return match.group(1)


def sync_skill_md_version() -> tuple[bool, str]:
    """Rewrite SKILL.md frontmatter `version:` to match pyproject.toml.

    Returns (changed, version). Raises if SKILL.md has no frontmatter version line.
    """
    version = read_project_version()
    skill_md = SKILLS_DIR / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")
    new_content, n = re.subn(
        r"^(version:\s*)\S+",
        lambda m: f"{m.group(1)}{version}",
        content,
        count=1,
        flags=re.MULTILINE,
    )
    if n == 0:
        raise RuntimeError("frontmatter 'version:' line not found in SKILL.md")
    changed = new_content != content
    if changed:
        skill_md.write_text(new_content, encoding="utf-8")
    return changed, version


def build_skills_zip(version: str) -> Path:
    """Bundle the skills/ directory into output/sellersprite-skills.zip."""
    zip_path = DIST_DIR / "sellersprite-skills.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SKILLS_DIR.rglob("*")):
            if path.is_file():
                arcname = Path("skills") / path.relative_to(SKILLS_DIR)
                zf.write(path, arcname.as_posix())
    return zip_path


def build_system_prompt_readme(version: str, skill_count: int) -> str:
    """Generate README for the system-prompt zip explaining how to use the bundled files."""
    return f"""# SellerSprite Skills — System Prompt Bundle

版本: **v{version}**  |  Skills 数量: **{skill_count}**

本压缩包包含 SellerSprite CLI 提供的 AI 技能体系的两种机器可读形式，
方便你在不安装 CLI 的前提下，把这套能力注入到任意 LLM / Agent 系统中。

---

## 📦 文件清单

| 文件 | 类型 | 用途 |
|------|------|------|
| `skills-system-prompt.md` | Markdown | 用于直接注入 LLM 的 system prompt |
| `skills.json` | JSON | 程序化使用：检索、动态加载、按需注入 |
| `README.md` | Markdown | 本文档 |

---

## 1. `skills-system-prompt.md` 用法

一份合成好的 Markdown，将所有 {skill_count} 个 Skill 的执行步骤、参数、引用 API 文档
全部内联在一起，可直接作为 system prompt 灌入 LLM。

### 适用场景

- 自建 Agent / Chatbot，希望让模型一次性掌握全部 Skill
- 需要在不依赖 MCP 客户端的环境中复用这套技能
- 评测、研究、Prompt 工程

### 使用示例 — Anthropic API (Python)

```python
import anthropic

with open("skills-system-prompt.md", encoding="utf-8") as f:
    system_prompt = f.read()

client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=2048,
    system=system_prompt,
    messages=[{{"role": "user", "content": "帮我找月销 500+ 的 FBM 产品"}}],
)
print(resp.content[0].text)
```

### 使用示例 — OpenAI API (Python)

```python
from openai import OpenAI

with open("skills-system-prompt.md", encoding="utf-8") as f:
    system_prompt = f.read()

client = OpenAI()
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {{"role": "system", "content": system_prompt}},
        {{"role": "user", "content": "帮我找月销 500+ 的 FBM 产品"}},
    ],
)
print(resp.choices[0].message.content)
```

### 使用示例 — 本地 LLM (Ollama / vLLM / LM Studio)

将文件内容粘贴到对应推理框架的 system prompt 配置项，
或通过 OpenAI 兼容 API 与上面示例相同方式注入。

> 提示：`skills-system-prompt.md` 体积约 200 KB / ~80K tokens，
> 注入前请确认目标模型支持的上下文窗口足够（建议 128K+）。

---

## 2. `skills.json` 用法

结构化数据，每个 Skill 一条记录，字段如下：

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | Skill 中文名 |
| `slug` | string | Skill 标识符（文件名） |
| `category` | string | `comprehensive`（综合分析）或 `tactical`（战术选品） |
| `content` | string | Skill 完整 Markdown 内容（步骤、参数等） |
| `referenced_tools` | string[] | 该 Skill 引用的 MCP 工具名列表 |
| `api_docs` | object | `{{工具名: 内联 API 文档}}` 映射 |

### 适用场景

- 检索：按用户意图模糊匹配最合适的 Skill
- 动态注入：仅把需要的 Skill 加入 prompt，节省 token
- 二次加工：转成你自己平台的 prompt template / 知识库格式
- 评测：批量跑 Skill 的端到端验证

### 使用示例 — 按需注入

```python
import json

with open("skills.json", encoding="utf-8") as f:
    skills = json.load(f)

# 用户问到 FBM 产品 → 只把 fbm-intercept 这一条注入
needed = next(s for s in skills if s["slug"] == "fbm-intercept")
system_prompt = f"你将按以下 Skill 执行：\\n\\n{{needed['content']}}"
```

### 使用示例 — 按类别筛选

```python
comp = [s for s in skills if s["category"] == "comprehensive"]
tac  = [s for s in skills if s["category"] == "tactical"]
print(f"综合分析 {{len(comp)}} 个，战术选品 {{len(tac)}} 个")
```

### 使用示例 — 工具引用图谱

```python
from collections import Counter

# 哪些 MCP 工具被最多 Skill 引用
counter = Counter(t for s in skills for t in s["referenced_tools"])
print(counter.most_common(5))
```

---

## 3. 两种格式怎么选？

- **想"零代码"快速上手** → 用 `skills-system-prompt.md`，整包 system prompt 一灌即可
- **想精细控制 token 与上下文** → 用 `skills.json`，按需挑选注入
- **企业级 Agent 系统** → 推荐 `skills.json` + 自建检索（向量库 / BM25 / 标签）

---

## 4. 配合 MCP 工具使用

Skill 内的执行步骤都会调用形如 `mcp__sellersprite__<tool_name>` 的工具。
若要让模型真正"跑通"这些工具，你的 Agent 需要接入 SellerSprite MCP Server：

- MCP 接入文档: <https://open.sellersprite.com/mcp>
- API 文档: <https://open.sellersprite.com/api>
- PyPI 包: <https://pypi.org/project/sellersprite-cli>
- GitHub: <https://github.com/opensellersprite/sellersprite-cli>
- Gitee: <https://gitee.com/opensellersprite/sellersprite-cli>

若仅做 prompt 实验、暂不接入真实 API，可让模型 mock 工具返回值，仍然能验证 Skill 的逻辑结构。

---

## 5. 版本与更新

- 当前版本: **v{version}**（与 `sellersprite-cli` 主包版本同步，可在本 README 顶部查看）
- 更新方式: 重新拉取最新 `skills-system-prompt.zip` 覆盖即可
- 如需保留多版本，请下载后自行重命名（如 `skills-system-prompt-v{version}.zip`）

---

## 6. 反馈

- 邮箱: open.seller.sprite@gmail.com
- Issues: <https://github.com/opensellersprite/sellersprite-cli/issues>

© SellerSprite. All rights reserved.
"""


def build_system_prompt_zip(system_prompt_md: str, skills_json: str, readme_md: str) -> Path:
    """Bundle the system-prompt markdown, JSON and README into a single zip in-memory."""
    zip_path = DIST_DIR / "skills-system-prompt.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README.md", readme_md)
        zf.writestr("skills-system-prompt.md", system_prompt_md)
        zf.writestr("skills.json", skills_json)
    return zip_path


def main():
    DIST_DIR.mkdir(exist_ok=True)

    # Sync SKILL.md frontmatter version to pyproject.toml (single source of truth)
    changed, version = sync_skill_md_version()
    if changed:
        print(f"SKILL.md frontmatter version updated -> {version}")
    else:
        print(f"SKILL.md frontmatter version already at {version}")

    # Collect all skill files
    skill_files = []
    for subdir in (SKILLS_DIR / "comprehensive", SKILLS_DIR / "tactical"):
        if subdir.exists():
            skill_files.extend(sorted(subdir.glob("*.md")))

    print(f"Found {len(skill_files)} skill files")

    # Parse all skills
    skills = [parse_skill(f) for f in skill_files]

    # Build artefacts in memory
    system_prompt_md = build_system_prompt(skills)
    skills_json = json.dumps(skills, ensure_ascii=False, indent=2)
    readme_md = build_system_prompt_readme(version, len(skills))

    # Generate skills zip for web download
    zip_file = build_skills_zip(version)
    print(f"Generated: {zip_file}")

    # Generate system-prompt zip (prompt + json + README) directly from memory
    sp_zip = build_system_prompt_zip(system_prompt_md, skills_json, readme_md)
    print(f"Generated: {sp_zip}")

    # Summary
    total_tools = sum(len(s["referenced_tools"]) for s in skills)
    print(f"\nSummary: {len(skills)} skills, {total_tools} tool references resolved")


if __name__ == "__main__":
    # Lightweight mode: only sync SKILL.md frontmatter version, skip artefact build.
    # Used by sync-skills-to-clawhub.ps1 before pushing the subtree.
    if "--sync-version" in sys.argv:
        changed, version = sync_skill_md_version()
        if changed:
            print(f"SKILL.md frontmatter version updated -> {version}")
            sys.exit(2)  # signal "file changed, please commit"
        print(f"SKILL.md frontmatter version already at {version}")
        sys.exit(0)
    main()
