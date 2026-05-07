"""卖家精灵 CLI — Python MCP 客户端 + 交互式终端 + 27 AI Skills."""

from importlib.metadata import version as _version

__version__ = _version("sellersprite-cli")

from .mcp_client import SellerSprite
from .errors import ApiError, McpError
