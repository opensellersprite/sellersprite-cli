#!/usr/bin/env python3
"""Unified docs manager — scrape, sync, audit and fix docs.

Usage:
    python docs_manager.py sync     # Scrape official API docs and force-overwrite mcp-api-source.md
    python docs_manager.py audit    # Read-only report
    python docs_manager.py fix      # Auto-fill missing sections from mcp-api-source.md to reference/*.md
"""

import argparse
import json
import re
from pathlib import Path

# Optional deps — only needed for sync mode
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None
try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

DOCS_DIR = Path(__file__).parent.parent / "src" / "sellersprite_cli" / "reference"
MCP_FILE = Path(__file__).parent.parent / "docs" / "mcp-api-source.md"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
CACHE_FILE = Path(__file__).parent.parent / "temp" / "api_docs_cache.json"

# API page ID → (section_number, chinese_title)
# MCP Code is scraped from the page itself, so we don't hardcode it.
API_PAGES = [
    (1, "查竞品"),
    (2, "选产品"),
    (9, "查产品类目"),
    (3, "ASIN 详情"),
    (56, "ASIN优惠趋势"),
    (57, "ASIN详情及优惠趋势"),
    (27, "ASIN 销量预测"),
    (26, "BSR销量预测"),
    (14, "关键词反查(流量词列表)"),
    (22, "商品趋势详情(keepa)"),
    (10, "关键词选品"),
    (11, "关键词选品-趋势数据"),
    (6, "关键词挖掘"),
    (46, "拓展流量词"),
    (19, "ABA 数据选品-按周"),
    (20, "ABA 数据选品-按月"),
    (60, "ABA 数据选品-关键词趋势"),
    (12, "谷歌趋势"),
    (24, "出单词反查"),
    (16, "关联流量列表"),
    (13, "流量词统计"),
    (15, "关联流量统计"),
    (17, "查流量来源(关键词流向)"),
    (29, "选市场列表"),
    (30, "选市场-统计"),
    (31, "选市场-商品集中度"),
    (32, "选市场-品牌集中度"),
    (35, "选市场-卖家所属地分布"),
    (33, "选市场-卖家集中度"),
    (34, "选市场-卖家类型分布"),
    (36, "选市场-商品需求趋势"),
    (37, "选市场-上架时间分布"),
    (38, "选市场-上架趋势分布"),
    (39, "选市场-评分数分布"),
    (40, "选市场-评分值分布"),
    (41, "选市场-价格分布"),
    (42, "选市场-A+视频分布"),
    (25, "查评论"),
]


# ── Web scraping ──────────────────────────────────────────

def scrape_all_pages(use_cache: bool = True) -> dict[str, dict]:
    """Scrape all API pages and return {mcp_code: data_dict}."""
    if use_cache and CACHE_FILE.exists():
        try:
            data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            print(f"[CACHE] Loaded {len(data)} tools from {CACHE_FILE}")
            return data
        except Exception:
            pass

    if sync_playwright is None:
        raise RuntimeError("playwright is required for sync. Run: pip install playwright")
    if BeautifulSoup is None:
        raise RuntimeError("beautifulsoup4 is required for sync. Run: pip install beautifulsoup4")

    results: dict[str, dict] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for api_id, title in API_PAGES:
            url = f"https://open.sellersprite.com/api/{api_id}"
            print(f"[FETCH] {url} ...")
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(2000)
                html = page.content()
                data = parse_html_tables(html)
                if data.get("mcp_code"):
                    results[data["mcp_code"]] = data
                    print(f"  -> {data['mcp_code']} ({title})")
                else:
                    print(f"  -> WARNING: no MCP Code found")
            except Exception as e:
                print(f"  -> ERROR: {e}")
        browser.close()

    # Save cache
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[CACHE] Saved {len(results)} tools to {CACHE_FILE}")
    return results


def parse_html_tables(html: str) -> dict:
    """Extract tables from scraped HTML."""
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")

    data: dict = {"method": "", "url": "", "mcp_code": "", "request_params": [], "response_params": []}

    for i, table in enumerate(tables):
        rows = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
            if cells and any(cells):
                rows.append(cells)

        if not rows:
            continue

        # Table 0: basic info
        if i == 0 and any("Http Method" in str(r) for r in rows):
            for row in rows:
                if len(row) >= 2:
                    key, val = row[0], row[1]
                    if "Method" in key:
                        data["method"] = val
                    elif "Request URL" in key:
                        data["url"] = val
                    elif "MCP Code" in key:
                        data["mcp_code"] = val

        # Table 1: request params (has "是否必填" column)
        elif any("是否必填" in str(r) for r in rows[:1]):
            header = rows[0]
            for row in rows[1:]:
                if len(row) >= 6:
                    data["request_params"].append({
                        "idx": row[0],
                        "name": row[1],
                        "type": row[2],
                        "required": row[3],
                        "label": row[4],
                        "desc": row[5] if len(row) > 5 else "",
                    })

        # Table 2+: response params (no "是否必填", but has "参数名称" and "参数描述")
        elif any("参数名称" in str(r) for r in rows[:1]) and not any("是否必填" in str(r) for r in rows[:1]):
            for row in rows[1:]:
                if len(row) >= 4:
                    data["response_params"].append({
                        "idx": row[0],
                        "name": row[1],
                        "type": row[2],
                        "label": row[3],
                        "desc": row[4] if len(row) > 4 else "",
                    })

    return data


def generate_markdown(api_id: int, title: str, data: dict) -> str:
    """Generate a markdown section matching mcp-api-source.md format."""
    lines = []
    lines.append(f"## {api_id}. {title}")
    lines.append("")
    lines.append("### 基本信息")
    lines.append(f"- **MCP Code**: `{data['mcp_code']}`")
    lines.append(f"- **Method**: {data['method']}")
    lines.append(f"- **URL**: `{data['url']}`")
    lines.append("")

    # Request params
    if data["request_params"]:
        lines.append("### 请求参数")
        lines.append("")
        lines.append("| # | 参数 | 类型 | 必填 | 说明 |")
        lines.append("|---|------|------|------|------|")
        for p in data["request_params"]:
            req = "✓" if p["required"] and p["required"] != " " else ""
            desc = p["desc"] if p["desc"] else ""
            if p["label"] and p["label"] != p["name"]:
                if desc:
                    desc = f"{p['label']}，{desc}"
                else:
                    desc = p["label"]
            lines.append(f"| {p['idx']} | {p['name']} | {p['type']} | {req} | {desc} |")
        lines.append("")

    # Response params
    if data["response_params"]:
        lines.append("### 响应参数")
        lines.append("")
        lines.append("| # | 字段 | 类型 | 说明 | 示例 |")
        lines.append("|---|------|------|------|------|")
        for p in data["response_params"]:
            label = p["label"] if p["label"] else ""
            desc = p["desc"] if p["desc"] else ""
            lines.append(f"| {p['idx']} | {p['name']} | {p['type']} | {label} | {desc} |")
        lines.append("")

    # Request example
    lines.append("### 请求示例")
    lines.append("")
    lines.append("```bash")
    lines.append(f"curl -X {data['method']} '{data['url']}' \\")
    lines.append("  -H 'secret-key: Your Secret' \\")
    if data["method"] == "POST":
        lines.append("  -H 'Content-Type: application/json' \\")
    # Try to build a minimal example body
    body_params = [p for p in data["request_params"] if p["required"] and p["required"] != " "]
    if body_params:
        example = {}
        for p in body_params:
            if p["name"] == "marketplace":
                example["marketplace"] = "US"
            elif p["name"] == "nodeIdPath":
                example["nodeIdPath"] = "2619525011"
            elif p["name"] == "asin":
                example["asin"] = "B08GHW4TBS"
            elif p["name"] == "keyword":
                example["keyword"] = "test"
            elif p["name"] == "date":
                example["date"] = "202412"
            elif p["name"] == "bsr":
                example["bsr"] = 2
            elif p["name"] == "category_id":
                example["category_id"] = "11260432011"
            elif p["type"] == "String":
                example[p["name"]] = ""
            elif p["type"] == "Integer":
                example[p["name"]] = 1
            elif p["type"] == "List":
                example[p["name"]] = []
            else:
                example[p["name"]] = ""
        if data["method"] == "GET" and example:
            qs = "&".join(f"{k}={v}" for k, v in example.items())
            lines.append(f"  -G -d '{qs}'")
        elif example:
            import json as _json
            lines.append(f"  -d '{_json.dumps(example)}'")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


# ── mcp-api-source.md sync ────────────────────────────────

def find_tool_section(mcp_content: str, mcp_code: str) -> tuple[int, int] | None:
    """Find start/end positions of a tool section in mcp-api-source.md."""
    code_pattern = rf"\*\*MCP Code\*\*:\s*`{re.escape(mcp_code)}`"
    match = re.search(code_pattern, mcp_content)
    if not match:
        return None
    start = mcp_content.rfind("\n## ", 0, match.start())
    if start == -1:
        start = 0
    else:
        start += 1
    end = mcp_content.find("\n## ", match.start())
    if end == -1:
        end = len(mcp_content)
    return start, end


def sync_mcp_source(force: bool = False) -> tuple[int, int, int]:
    """Sync official API docs to mcp-api-source.md. Returns (updated, unchanged, new)."""
    scraped = scrape_all_pages(use_cache=not force)
    mcp_content = MCP_FILE.read_text(encoding="utf-8")

    updated = 0
    unchanged = 0
    new = 0

    # Since scraping returns {mcp_code: data} in insertion order,
    # we zip API_PAGES order with scraped items.
    scraped_items = list(scraped.items())

    for idx, (api_id, title) in enumerate(API_PAGES):
        if idx >= len(scraped_items):
            print(f"[WARN] No scraped data for {api_id}. {title}")
            continue
        code, data = scraped_items[idx]

        new_section = generate_markdown(api_id, title, data)
        existing = find_tool_section(mcp_content, code)

        if existing is None:
            print(f"[NEW] {api_id}. {title} ({code})")
            mcp_content = mcp_content.rstrip() + "\n\n---\n\n" + new_section
            new += 1
        else:
            start, end = existing
            old_section = mcp_content[start:end]
            if old_section.strip() == new_section.strip():
                print(f"[OK] {api_id}. {title} ({code})")
                unchanged += 1
            else:
                print(f"[UPDATE] {api_id}. {title} ({code})")
                mcp_content = mcp_content[:start] + new_section + mcp_content[end:]
                updated += 1

    MCP_FILE.write_text(mcp_content, encoding="utf-8")
    print(f"\nSync complete: {updated} updated, {unchanged} unchanged, {new} new")
    return updated, unchanged, new


# ── Original audit/fix logic (unchanged) ──────────────────

def extract_sections(content: str) -> dict[str, str]:
    """Extract sections from a markdown file by ## / ### headings."""
    sections: dict[str, str] = {}
    lines = content.splitlines()
    current, buffer = None, []

    for line in lines:
        if line.startswith("## ") or line.startswith("### "):
            if current:
                sections[current] = "\n".join(buffer).strip()
            current = line.strip()
            buffer = []
        elif current:
            buffer.append(line)

    if current:
        sections[current] = "\n".join(buffer).strip()
    return sections


def has_basic_info(content: str) -> bool:
    """Check if content has Method and URL."""
    return "Method" in content and "URL" in content


def extract_params_from_table(content: str) -> set[str]:
    """Extract parameter names from a markdown table."""
    params: set[str] = set()
    for line in content.splitlines():
        stripped = line.strip()
        if "|" not in stripped or "---" in stripped:
            continue
        cells = [c.strip().strip("`") for c in stripped.split("|")[1:-1]]
        if not cells or not any(cells) or cells[0].startswith("-"):
            continue
        first = cells[0]
        if first in ("参数", "参数名", "字段", "序号", "#"):
            continue
        # Handle tables with a leading number column (mcp-api-source.md style)
        if first.isdigit() and len(cells) >= 2:
            param = cells[1].split("[")[0].split(".")[0]
        else:
            param = first.split("[")[0].split(".")[0]
        if param and not param.isdigit():
            # mcp-api-source.md 中范围参数用斜杠合并
            parts = [p.strip() for p in param.split("/")]
            if len(parts) == 2 and parts[0] in ("min", "max"):
                a, b = parts
                suffix = b[3:] if b.startswith(("min", "max")) else b
                params.add(f"min{suffix}")
                params.add(f"max{suffix}")
            else:
                for p in parts:
                    if p:
                        params.add(p)
    return params


def find_tool_in_mcp(tool_name: str, mcp_content: str) -> str | None:
    """Find the section for a tool in mcp-api-source.md by MCP Code."""
    code_pattern = rf"\*\*MCP Code\*\*:\s*`{tool_name}`"
    match = re.search(code_pattern, mcp_content)
    if not match:
        return None
    start = mcp_content.rfind("\n## ", 0, match.start())
    if start == -1:
        start = 0
    else:
        start += 1
    end = mcp_content.find("\n## ", match.start())
    if end == -1:
        end = len(mcp_content)
    return mcp_content[start:end]


def find_section(sections: dict[str, str], keywords: list[str]) -> str | None:
    """Find first section whose heading contains any keyword."""
    for key, value in sections.items():
        for kw in keywords:
            if kw in key:
                return value
    return None


def build_doc(tool_name: str, doc_content: str, mcp_content: str) -> str:
    """Build merged doc: preserve existing, fill missing from mcp."""
    doc_sections = extract_sections(doc_content)
    mcp_sections = extract_sections(mcp_content)

    parts = []

    # 1. Title
    parts.append(f"# {tool_name}")
    parts.append("")

    # 2. Description (keep from doc)
    desc = find_section(doc_sections, ["描述"])
    if desc:
        parts.append("## 描述")
        parts.append("")
        parts.append(desc)
        parts.append("")

    # 3. MCP name
    parts.append("## MCP 调用名称")
    parts.append("")
    parts.append(f"`mcp__sellersprite__{tool_name}`")
    parts.append("")

    # 4. Request params (keep from doc; fall back to mcp)
    doc_params = find_section(doc_sections, ["参数"])
    mcp_params = find_section(mcp_sections, ["参数"])
    params = doc_params or mcp_params
    if params:
        parts.append("## 参数")
        parts.append("")
        parts.append(params)
        parts.append("")

    # 5. Basic info (from mcp if missing in doc)
    basic = find_section(doc_sections, ["基本信息"])
    if not basic:
        basic = find_section(mcp_sections, ["基本信息"])
    if basic:
        parts.append("## 基本信息")
        parts.append("")
        parts.append(basic)
        parts.append("")

    # 6. Response params (from mcp if missing in doc)
    resp = find_section(doc_sections, ["响应参数"])
    if not resp:
        resp = find_section(mcp_sections, ["响应参数"])
    if resp:
        parts.append("## 响应参数")
        parts.append("")
        parts.append(resp)
        parts.append("")

    # 7. Request example (prefer doc, fall back to mcp)
    example = find_section(doc_sections, ["请求示例"])
    if not example:
        example = find_section(mcp_sections, ["请求示例"])
    if example:
        parts.append("## 请求示例")
        parts.append("")
        parts.append(example)
        parts.append("")

    return "\n".join(parts) + "\n"


def run_audit() -> tuple[list, list[Path]]:
    """Audit mode: compare reference/*.md against mcp-api-source.md."""
    mcp_content = MCP_FILE.read_text(encoding="utf-8")
    doc_files = sorted([f for f in DOCS_DIR.glob("*.md")])
    issues = []

    for doc_file in doc_files:
        tool_name = doc_file.stem
        doc_content = doc_file.read_text(encoding="utf-8")
        doc_sections = extract_sections(doc_content)

        mcp_section = find_tool_in_mcp(tool_name, mcp_content)
        if not mcp_section:
            issues.append((tool_name, "NOT FOUND in mcp-api-source.md", []))
            continue

        mcp_sections = extract_sections(mcp_section)

        doc_has_basic = any(has_basic_info(v) for v in doc_sections.values())
        mcp_has_basic = any(has_basic_info(v) for v in mcp_sections.values())

        doc_req_params = set()
        mcp_req_params = set()
        for k, v in doc_sections.items():
            if "参数" in k:
                doc_req_params |= extract_params_from_table(v)
        for k, v in mcp_sections.items():
            if "请求参数" in k:
                mcp_req_params |= extract_params_from_table(v)

        doc_resp_params = set()
        mcp_resp_params = set()
        for k, v in doc_sections.items():
            if "响应" in k or "响应参数" in k:
                doc_resp_params |= extract_params_from_table(v)
        for k, v in mcp_sections.items():
            if "响应参数" in k:
                mcp_resp_params |= extract_params_from_table(v)

        missing_req = mcp_req_params - doc_req_params
        missing_resp = mcp_resp_params - doc_resp_params
        doc_has_example = any("请求示例" in k for k in doc_sections)
        mcp_has_example = any("请求示例" in k for k in mcp_sections)

        tool_issues = []
        if not doc_has_basic and mcp_has_basic:
            tool_issues.append("缺少基本信息 (Method/URL)")
        if missing_req:
            tool_issues.append(f"请求参数缺失: {', '.join(sorted(missing_req))}")
        if missing_resp:
            tool_issues.append(f"响应参数缺失: {', '.join(sorted(missing_resp))}")
        if not doc_has_example and mcp_has_example:
            tool_issues.append("缺少请求示例")

        if tool_issues:
            issues.append((tool_name, doc_file.name, tool_issues))

    return issues, doc_files


def print_report(issues: list, doc_files: list[Path]) -> str:
    """Print audit report and return the report text."""
    lines = []
    lines.append("=" * 80)
    lines.append("DOCS AUDIT REPORT")
    lines.append("=" * 80)

    if not issues:
        lines.append("\n所有文档完整，无缺失！")
    else:
        lines.append(f"\n发现 {len(issues)} 个文档存在问题:\n")
        for tool_name, doc_name, tool_issues in issues:
            lines.append(f"\n[{tool_name}] ({doc_name})")
            for issue in tool_issues:
                lines.append(f"  - {issue}")

    all_tools = {f.stem for f in doc_files}
    issue_tools = {i[0] for i in issues}
    ok_tools = sorted(all_tools - issue_tools)

    if ok_tools:
        lines.append(f"\n\n[OK] 完整文档 ({len(ok_tools)} 个):")
        for t in ok_tools:
            lines.append(f"  - {t}")

    lines.append("\n" + "=" * 80)
    lines.append(f"总计检查: {len(doc_files)} 个文档")
    lines.append(f"存在问题: {len(issues)} 个")
    lines.append(f"完整文档: {len(ok_tools)} 个")
    lines.append("=" * 80)

    text = "\n".join(lines)
    print(text)
    return text


def run_fix() -> tuple[int, int]:
    """Fix mode: auto-fill missing sections from mcp."""
    mcp_raw = MCP_FILE.read_text(encoding="utf-8")
    mcp_tools: dict[str, str] = {}
    parts = re.split(r'\n(?=## \d+\. )', mcp_raw)
    for part in parts:
        m = re.search(r'\*\*MCP Code\*\*:\s*`([a-z_]+)`', part)
        if m:
            mcp_tools[m.group(1)] = part

    updated = 0
    unchanged = 0

    for doc_file in sorted(DOCS_DIR.glob("*.md")):
        tool_name = doc_file.stem
        if tool_name not in mcp_tools:
            print(f"[SKIP] {tool_name}: not in mcp-api-source.md")
            continue

        doc_raw = doc_file.read_text(encoding="utf-8")
        new_content = build_doc(tool_name, doc_raw, mcp_tools[tool_name])

        if new_content.strip() != doc_raw.strip():
            doc_file.write_text(new_content, encoding="utf-8")
            print(f"[UPDATED] {tool_name}")
            updated += 1
        else:
            print(f"[OK] {tool_name}")
            unchanged += 1

    return updated, unchanged


# ── Main ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Docs manager: sync, audit or fix reference/*.md")
    parser.add_argument("command", choices=["sync", "audit", "fix"],
                        help="sync=scrape official docs and overwrite mcp-api-source.md, audit=report only, fix=auto-fill missing")
    parser.add_argument("--force", action="store_true", help="Force re-scrape (ignore cache)")
    args = parser.parse_args()

    if args.command == "sync":
        updated, unchanged, new = sync_mcp_source(force=args.force)
        print(f"\nRunning fix to sync reference/*.md...")
        fixed, ok = run_fix()
        print(f"\nDone: mcp-api-source.md ({updated} updated, {unchanged} unchanged, {new} new), reference/*.md ({fixed} updated, {ok} unchanged)")
    elif args.command == "audit":
        issues, doc_files = run_audit()
        report = print_report(issues, doc_files)
        OUTPUT_DIR.mkdir(exist_ok=True)
        output_file = OUTPUT_DIR / "audit_report.txt"
        output_file.write_text(report, encoding="utf-8")
        print(f"\n报告已保存到: {output_file}")
        if issues:
            raise SystemExit(1)
    else:
        updated, unchanged = run_fix()
        print(f"\nDone: {updated} updated, {unchanged} unchanged")


if __name__ == "__main__":
    main()
