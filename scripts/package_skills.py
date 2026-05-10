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
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / "src" / "sellersprite_cli" / "skills"
REFERENCE_DIR = ROOT / "src" / "sellersprite_cli" / "reference"
DIST_DIR = ROOT / "output"

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


def main():
    DIST_DIR.mkdir(exist_ok=True)

    # Collect all skill files
    skill_files = []
    for subdir in (SKILLS_DIR / "comprehensive", SKILLS_DIR / "tactical"):
        if subdir.exists():
            skill_files.extend(sorted(subdir.glob("*.md")))

    print(f"Found {len(skill_files)} skill files")

    # Parse all skills
    skills = [parse_skill(f) for f in skill_files]

    # Generate system prompt markdown
    system_prompt = build_system_prompt(skills)
    prompt_file = DIST_DIR / "skills-system-prompt.md"
    prompt_file.write_text(system_prompt, encoding="utf-8")
    print(f"Generated: {prompt_file} ({len(system_prompt)} chars)")

    # Generate JSON
    json_file = DIST_DIR / "skills.json"
    json_file.write_text(
        json.dumps(skills, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Generated: {json_file}")

    # Summary
    total_tools = sum(len(s["referenced_tools"]) for s in skills)
    print(f"\nSummary: {len(skills)} skills, {total_tools} tool references resolved")


if __name__ == "__main__":
    main()
