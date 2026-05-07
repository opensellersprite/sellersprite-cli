"""MCP and API error types."""


class McpError(Exception):
    """JSON-RPC / transport layer error."""

    def __init__(self, err: dict):
        self.code = err.get("code")
        self.message = err.get("message", "")
        super().__init__(f"MCP Error {self.code}: {self.message}")


class ApiError(Exception):
    """Business logic error from the SellerSprite API."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"API Error {code}: {message}")
