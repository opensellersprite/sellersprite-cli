#!/usr/bin/env python3
"""Unified docs manager — audit and fix reference/*.md against mcp-api-source.md.

Usage:
    python docs_manager.py audit    # Read-only report
    python docs_manager.py fix      # Auto-fill missing sections
"""

import argparse
import re
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "src" / "sellersprite_cli" / "reference"
MCP_FILE = Path(__file__).parent.parent / "docs" / "mcp-api-source.md"
OUTPUT_DIR = Path(__file__).parent.parent / "output"


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
    mcp_params = find_section(mcp_sections, ["请求参数"])
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


def run_audit() -> list[tuple[str, str, list[str]]]:
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


def main():
    parser = argparse.ArgumentParser(description="Docs manager: audit or fix reference/*.md")
    parser.add_argument("command", choices=["audit", "fix"], help="audit=report only, fix=auto-fill missing")
    args = parser.parse_args()

    if args.command == "audit":
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
