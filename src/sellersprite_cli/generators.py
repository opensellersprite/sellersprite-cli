"""Client config generators — produce MCP configs for 10 AI coding tools."""

import json
import shutil
from dataclasses import dataclass, field
from importlib.resources import files as pkg_files
from pathlib import Path

MCP_URL = "https://mcp.sellersprite.com/mcp"

_MCP_JSON = {
    "type": "streamableHttp",
    "url": MCP_URL,
    "headers": {"secret-key": "{key}"},
}
MCP_JSON_TEMPLATE = {"mcpServers": {"sellersprite": dict(_MCP_JSON)}}
MCP_SERVERS_TEMPLATE = {"servers": {"sellersprite": dict(_MCP_JSON)}}


# ── Config table ──────────────────────────────────────────────

@dataclass
class ClientSpec:
    name: str
    label: str
    config_path: str | None = None
    config_format: str = "mcp_servers"   # mcp_servers | servers | toml | none | note
    config_is_global: bool = False
    rules_file: str | None = None
    rules_suffix: str | None = None
    rules_dir: str | None = None
    extra_notes: list[str] = field(default_factory=list)
    inline_rules: bool = False            # Cline: write config + rules into single file


CLIENTS: dict[str, ClientSpec] = {
    "claude-code": ClientSpec(
        "claude-code", "Claude Code",
        config_path=".claude/settings.json",
        rules_file="CLAUDE.md",
        rules_suffix=".md",
        rules_dir=".claude/commands",
    ),
    "cursor": ClientSpec(
        "cursor", "Cursor",
        config_path=".cursor/mcp.json",
        rules_dir=".cursor/rules",
        rules_suffix=".mdc",
    ),
    "cline": ClientSpec(
        "cline", "Cline",
        config_path=".clinerules",
        config_format="none",
        inline_rules=True,
    ),
    "claude-desktop": ClientSpec(
        "claude-desktop", "Claude Desktop",
        config_path=".claude/claude_desktop_config.json",
        config_is_global=True,
        extra_notes=["Skills 需手动粘贴到对话中"],
    ),
    "vscode": ClientSpec(
        "vscode", "VS Code Copilot",
        config_path=".vscode/mcp.json",
        config_format="servers",
        rules_file=".github/copilot-instructions.md",
    ),
    "windsurf": ClientSpec(
        "windsurf", "Windsurf",
        config_path=".windsurf/mcp.json",
        config_is_global=True,
        rules_file=".windsurfrules",
    ),
    "trae": ClientSpec(
        "trae", "Trae",
        config_format="note",
        extra_notes=["MCP 配置需通过 UI 管理"],
        rules_file=".trae-rules.md",
    ),
    "codex": ClientSpec(
        "codex", "Codex (OpenAI)",
        config_path=".codex/config.toml",
        config_format="toml",
        config_is_global=True,
        rules_file="AGENTS.md",
    ),
    "antigravity": ClientSpec(
        "antigravity", "Antigravity",
        config_path=".gemini/antigravity/mcp_config",
        config_is_global=True,
        rules_file="GEMINI.md",
    ),
    "openclaw": ClientSpec(
        "openclaw", "OpenClaw",
        config_format="note",
        extra_notes=[
            "运行命令配置: openclaw mcp set sellersprite",
            "或手动配置 URL={MCP_URL}, secret-key={key_prefix}...",
        ],
        rules_file="OPENCLAW.md",
    ),
}

CLIENT_NAMES = set(CLIENTS.keys())


# ── Helpers ───────────────────────────────────────────────────

def _deep_merge(base: dict, override: dict) -> dict:
    result = dict(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def _resolve_path(spec: ClientSpec, project_dir: Path) -> Path | None:
    if not spec.config_path:
        return None
    base = Path.home() if spec.config_is_global else project_dir
    return base / spec.config_path


def _get_skills_dir() -> Path:
    return Path(str(pkg_files("sellersprite_cli") / "skills"))


def _mcp_config(key: str, fmt: str) -> dict:
    template = MCP_SERVERS_TEMPLATE if fmt == "servers" else MCP_JSON_TEMPLATE
    cfg = json.loads(json.dumps(template))
    root_key = "servers" if fmt == "servers" else "mcpServers"
    cfg[root_key]["sellersprite"]["headers"]["secret-key"] = key
    return cfg


def _write_json(path: Path, data: dict, dry_run: bool) -> str:
    if dry_run:
        return f"  [dry-run] would write: {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    merged = _deep_merge(
        json.loads(path.read_text(encoding="utf-8")) if path.exists() else {},
        data,
    )
    path.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return f"  wrote: {path}"


def _write_text(path: Path, text: str, dry_run: bool) -> str:
    if dry_run:
        return f"  [dry-run] would write: {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return f"  wrote: {path}"


def _copy_dir(src: Path, dst: Path, dry_run: bool) -> list[str]:
    if dry_run:
        return [f"  [dry-run] would copy: {src}/ -> {dst}/"]
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return [f"  copied: {dst}/"]


def _copy_files(src_dir: Path, dst_dir: Path, suffix: str = ".md",
                dry_run: bool = False) -> list[str]:
    if not src_dir.exists():
        return [f"  [skip] source not found: {src_dir}"]
    if dry_run:
        return [f"  [dry-run] would copy: {src_dir}/*.md -> {dst_dir}/*{suffix}"]
    dst_dir.mkdir(parents=True, exist_ok=True)
    msgs = []
    for f in src_dir.iterdir():
        if f.is_file():
            dst = dst_dir / (f.stem + suffix)
            shutil.copy2(f, dst)
            msgs.append(f"  wrote: {dst}")
    return msgs


# ── Config writers ────────────────────────────────────────────

def _write_config(path: Path, key: str, spec: ClientSpec, dry_run: bool) -> str:
    fmt = spec.config_format
    if fmt in ("mcp_servers", "servers"):
        return _write_json(path, _mcp_config(key, fmt), dry_run)
    if fmt == "toml":
        return _write_toml_config(path, key, dry_run)
    return ""


def _write_toml_config(path: Path, key: str, dry_run: bool) -> str:
    toml_content = (
        '[mcp_servers.sellersprite]\n'
        'url = "https://mcp.sellersprite.com/mcp"\n\n'
        '[mcp_servers.sellersprite.headers]\n'
        f'secret-key = "{key}"\n'
    )
    if dry_run:
        return f"  [dry-run] would write: {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if "sellersprite" not in existing:
            path.write_text(existing + "\n" + toml_content, encoding="utf-8")
            return f"  appended: {path}"
        return f"  [skip] already configured: {path}"
    path.write_text(toml_content, encoding="utf-8")
    return f"  wrote: {path}"


# ── Rules writers ─────────────────────────────────────────────

def _read_instructions() -> str:
    path = _get_skills_dir() / "agent-instructions.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _build_rules_content(spec: ClientSpec, key: str, skills: bool) -> str:
    parts = []
    if spec.inline_rules:
        parts.append(
            "## SellerSprite MCP Server\n\n"
            f"URL: {MCP_URL}\nProtocol: Streamable HTTP\n"
            "Tools prefix: mcp__sellersprite__\n\n"
            f"secret-key: {key}\n\n"
        )
    parts.append(_read_instructions())
    if skills and (cmd_dir := _get_skills_dir() / "comprehensive").exists():
        parts.append("\n\n## 综合分析命令\n")
        for f in sorted(cmd_dir.iterdir()):
            if f.is_file():
                parts.append(f"\n### {f.stem}\n\n{f.read_text(encoding='utf-8')}\n---\n")
    return "".join(parts)


def _write_rules(spec: ClientSpec, project_dir: Path, skills_dir: Path,
                 key: str, skills: bool, dry_run: bool) -> list[str]:
    msgs = []
    if spec.inline_rules:
        rules_path = project_dir / spec.config_path
        content = _build_rules_content(spec, key, skills)
        if dry_run:
            msgs.append(f"  [dry-run] would write: {rules_path}")
        else:
            rules_path.write_text(content, encoding="utf-8")
            msgs.append(f"  wrote: {rules_path}")
        return msgs

    if spec.rules_file:
        instructions = _read_instructions()
        if instructions:
            msgs.append(_write_text(
                project_dir / spec.rules_file, instructions, dry_run))

    if spec.rules_dir and skills:
        msgs += _copy_files(
            skills_dir / "comprehensive",
            project_dir / spec.rules_dir,
            suffix=spec.rules_suffix or ".md",
            dry_run=dry_run,
        )

    return msgs


# ── Main entry ────────────────────────────────────────────────

def generate(name: str, key: str, project_dir: Path,
             skills: bool = False, dry_run: bool = False) -> list[str]:
    spec = CLIENTS.get(name)
    if not spec:
        return [f"  [skip] unknown client: {name}"]

    msgs = [f">> {spec.label}"]

    # Config
    config_path = _resolve_path(spec, project_dir)
    if config_path and spec.config_format not in ("none", "note"):
        msgs.append(_write_config(config_path, key, spec, dry_run))

    # Notes
    for note in spec.extra_notes:
        rendered = note.format(MCP_URL=MCP_URL, key_prefix=key[:8])
        msgs.append(f"  [note] {rendered}")

    # Skills + Rules
    skills_dir = _get_skills_dir()
    if skills:
        msgs += _copy_dir(skills_dir, project_dir / "skills", dry_run)
    msgs += _write_rules(spec, project_dir, skills_dir, key, skills, dry_run)

    return msgs
