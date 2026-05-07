# sellersprite-cli

卖家精灵 CLI — Python MCP 客户端 + 交互式终端 + 27 AI Skills，通过 MCP 调用 38 个 Amazon 数据工具。

## 环境

- Windows 环境，使用 `python` 而非 `python3`（python3 指向微软商店空壳）
- Bash 工具运行在 **bash** 环境中（非 PowerShell），不要使用 `$null`、`Select-String` 等 PowerShell 语法
- 执行 Python 脚本时加前缀 `PYTHONIOENCODING=utf-8` 避免 Windows GBK 编码错误
- 包管理器使用 `uv pip`（非 `pip`）

## 项目结构

```
src/sellersprite_cli/
  __init__.py          # 入口，导出 SellerSprite, ApiError, McpError
  cli.py               # Typer CLI + 交互式 TUI
  mcp_client.py        # MCP Streamable HTTP 客户端（SellerSprite 类）
  registry.py          # 38 个工具元数据注册表
  generators.py        # 10 种 AI 客户端配置生成器
  markdown_utils.py    # Skills 卡片加载器
  errors.py            # McpError, ApiError
  skills/              # 27 个 .md 技能卡片 + agent-instructions.md
```

## 构建

```bash
rm -rf dist/ && python -m build
twine upload dist/*
```

## 版本

版本号仅在 `pyproject.toml` 中维护，`__init__.py` 通过 `importlib.metadata` 读取。
