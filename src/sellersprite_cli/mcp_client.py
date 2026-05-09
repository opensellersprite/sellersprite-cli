"""SellerSprite MCP 客户端 — Python client for the SellerSprite MCP Server.

Communicates via MCP Streamable HTTP (JSON-RPC 2.0 over HTTP with SSE support).
Provides 36 methods covering ASIN analysis, product research, keywords,
traffic, market analysis, ABA trends, and reviews.
"""

import json
import logging
import os
import time
from importlib.metadata import version as _version

import requests

from .errors import ApiError, McpError

logger = logging.getLogger(__name__)

__version__ = _version("sellersprite-cli")


class SellerSprite:
    """卖家精灵 API 客户端。

    Usage::

        ss = SellerSprite()                       # reads SELLERSPRITE_KEY env
        ss = SellerSprite("your-secret-key")      # explicit key

        result = ss.product_node(keyword="earbuds")
    """

    def __init__(self, secret_key: str | None = None, marketplace: str = "US",
                 base_url: str = "https://mcp.sellersprite.com/mcp"):
        self.secret_key = secret_key or os.environ.get("SELLERSPRITE_KEY", "")
        if not self.secret_key:
            raise ValueError(
                "缺少 API 密钥。请设置 SELLERSPRITE_KEY 环境变量或传入 secret_key"
            )
        self.marketplace = marketplace
        self.base_url = base_url
        self._session = requests.Session()
        self._session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "secret-key": self.secret_key,
            "x-cli-version": __version__,
        })
        self._id = 0

    # ── core transport ────────────────────────────────────────

    def _call(self, tool_name: str, arguments: dict) -> dict | list:
        self._id += 1
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": arguments},
            "id": self._id,
        }
        logger.info("-> %s args=%s", tool_name, arguments)
        start = time.monotonic()

        try:
            resp = self._session.post(self.base_url, json=payload, timeout=60)
            resp.raise_for_status()
        except requests.ConnectionError as e:
            logger.error("<- %s FAILED connection_error %.0fms %s", tool_name,
                         (time.monotonic() - start) * 1000, e)
            raise ConnectionError(f"[{tool_name}] MCP Server 连接失败: {e}") from e
        except requests.Timeout as e:
            logger.error("<- %s FAILED timeout %.0fms", tool_name,
                         (time.monotonic() - start) * 1000)
            raise TimeoutError(f"[{tool_name}] 请求超时 (60s): {e}") from e
        except requests.HTTPError as e:
            logger.error("<- %s FAILED http_%d %.0fms", tool_name,
                         e.response.status_code, (time.monotonic() - start) * 1000)
            raise ConnectionError(
                f"[{tool_name}] HTTP {e.response.status_code}: {e}"
            ) from e

        text = resp.text.strip()
        elapsed = (time.monotonic() - start) * 1000

        # SSE format: data: {...}\ndata: {...}\n\n
        if text.startswith("data:"):
            lines = [
                line[len("data:"):].strip()
                for line in text.split("\n")
                if line.startswith("data:")
            ]
            text = "\n".join(lines) if lines else text

        try:
            rpc = json.loads(text)
        except json.JSONDecodeError as e:
            logger.error("<- %s FAILED json_parse %.0fms", tool_name, elapsed)
            raise ValueError(
                f"[{tool_name}] 响应 JSON 解析失败: {e}\n原始: {text[:200]}"
            ) from e

        if "error" in rpc:
            err = rpc["error"]
            logger.error("<- %s FAILED rpc_error code=%s msg=%s %.0fms",
                         tool_name, err.get("code"), err.get("message", ""), elapsed)
            raise McpError(err)

        content = rpc.get("result", {}).get("content", [])
        if not content:
            logger.warning("<- %s empty_content %.0fms", tool_name, elapsed)
            return {}

        text_raw = content[0].get("text", "")
        if not text_raw or not text_raw.strip():
            logger.warning("<- %s empty_data %.0fms", tool_name, elapsed)
            return {}
        try:
            inner = json.loads(text_raw)
        except json.JSONDecodeError as e:
            logger.error("<- %s FAILED inner_json_parse %.0fms", tool_name, elapsed)
            raise ValueError(
                f"[{tool_name}] 响应数据解析失败: {e}\n原始: {text_raw[:200]}"
            ) from e
        if inner.get("code") != "OK":
            code, msg = inner.get("code"), inner.get("message")
            logger.error("<- %s api_error code=%s msg=%s %.0fms", tool_name, code, msg, elapsed)
            raise ApiError(code, msg)

        data = inner.get("data")
        result_count = len(data) if isinstance(data, (list, dict)) else 1
        logger.debug("<- %s ok %s %.0fms", tool_name, result_count, elapsed)
        return data

    # ── helpers ──────────────────────────────────────────────

    _LIST_PARAMS = frozenset({
        "asinList", "asins", "relations", "keywordList",
        "nodeIdPaths", "starList", "typeList",
    })
    _STR_PARAMS = frozenset({
        "includeKeywords", "excludeKeywords",
    })

    @staticmethod
    def _to_camel(name: str) -> str:
        parts = name.replace("-", "_").split("_")
        return parts[0] + "".join(p.capitalize() for p in parts[1:])

    def _req(self, marketplace: str | None, **kw) -> dict:
        body = {"marketplace": marketplace or self.marketplace}
        for k, v in kw.items():
            key = self._to_camel(k) if "_" in k else k
            if key in self._LIST_PARAMS and isinstance(v, str):
                v = [v]
            elif key in self._STR_PARAMS and isinstance(v, list):
                v = ",".join(v)
            body[key] = v
        return body

    @staticmethod
    def _clean(params: dict) -> dict:
        return {k: v for k, v in params.items() if v is not None}

    # ── ASIN 分析 (5) ──────────────────────────────────────

    def asin_detail(self, asin: str, marketplace: str | None = None) -> dict:
        return self._call("asin_detail", self._req(marketplace, asin=asin))

    def asin_prediction(self, asin: str, marketplace: str | None = None) -> dict:
        return self._call("asin_prediction", self._req(marketplace, asin=asin))

    def asin_coupon_trend(self, asin: str, marketplace: str | None = None) -> dict:
        return self._call("asin_coupon_trend", self._req(marketplace, asin=asin))

    def asin_detail_with_coupon_trend(self, asin: str, marketplace: str | None = None) -> dict:
        return self._call("asin_detail_with_coupon_trend", self._req(marketplace, asin=asin))

    def keepa_info(self, asin: str, marketplace: str | None = None) -> dict:
        return self._call("keepa_info", self._req(marketplace, asin=asin))

    # ── 商品与竞品 (3) ─────────────────────────────────────

    def product_research(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("product_research", {"request": self._clean(self._req(marketplace, **kw))})

    def competitor_lookup(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("competitor_lookup", {"request": self._clean(self._req(marketplace, **kw))})

    def product_node(self, marketplace: str | None = None, **kw) -> list:
        return self._call("product_node", {"request": self._clean(self._req(marketplace, **kw))})

    # ── 关键词 (5) ─────────────────────────────────────────

    def keyword_miner(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("keyword_miner", {"request": self._clean(self._req(marketplace, **kw))})

    def keyword_research(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("keyword_research", {"request": self._clean(self._req(marketplace, **kw))})

    def keyword_research_trends(self, keyword: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("keyword_research_trends", self._clean({
            "marketplace": marketplace or self.marketplace, "keyword": keyword, **kw}))

    def keyword_order(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("keyword_order", {"request": self._clean(self._req(marketplace, **kw))})

    def bsr_prediction(self, bsr: int, category_id: str, marketplace: str | None = None) -> dict:
        return self._call("bsr_prediction", {
            "marketplace": marketplace or self.marketplace,
            "bsr": bsr, "categoryId": category_id,
        })

    # ── 流量 (6) ───────────────────────────────────────────

    def traffic_keyword(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("traffic_keyword", {"request": self._clean(self._req(marketplace, **kw))})

    def traffic_keyword_stat(self, asin: str, month: str | None = None,
                             marketplace: str | None = None) -> dict:
        p = self._req(marketplace, asin=asin)
        if month:
            p["month"] = month
        return self._call("traffic_keyword_stat", p)

    def traffic_source(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("traffic_source", {"request": self._clean(self._req(marketplace, **kw))})

    def traffic_listing_stat(self, asin: str, marketplace: str | None = None) -> dict:
        return self._call("traffic_listing_stat", self._req(marketplace, asin=asin))

    def traffic_listing(self, asin_list: list[str], relations: list[str],
                        marketplace: str | None = None, **kw) -> dict:
        return self._call("traffic_listing", {"request": self._clean(self._req(
            marketplace, asin_list=asin_list, relations=relations, **kw))})

    def traffic_extend(self, asin_list: list[str], marketplace: str | None = None, **kw) -> dict:
        return self._call("traffic_extend", {"request": self._clean(self._req(
            marketplace, asin_list=asin_list, **kw))})

    # ── 市场分析 (14) ──────────────────────────────────────

    def market_research(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_research", {"request": self._clean(self._req(marketplace, **kw))})

    def market_research_statistics(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_research_statistics", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_price_distribution(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_price_distribution", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_brand_concentration(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_brand_concentration", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_product_concentration(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_product_concentration", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_seller_concentration(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_seller_concentration", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_rating_distribution(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_rating_distribution", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_ratings_count_distribution(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_ratings_count_distribution", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_listing_date_distribution(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_listing_date_distribution", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_listing_trend_distribution(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_listing_trend_distribution", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_seller_country_distribution(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_seller_country_distribution", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_seller_type_concentration(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_seller_type_concentration", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_ebc_distribution(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_ebc_distribution", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    def market_product_demand_trend(self, node_id_path: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("market_product_demand_trend", {
            "request": self._clean(self._req(marketplace, node_id_path=node_id_path, **kw))})

    # ── ABA / 趋势 (5) ────────────────────────────────────

    def aba_research_weekly(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("aba_research_weekly", {"request": self._clean(self._req(marketplace, **kw))})

    def aba_research_monthly(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("aba_research_monthly", {"request": self._clean(self._req(marketplace, **kw))})

    def aba_research_trend(self, keyword: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("aba_research_trend", self._clean({
            "marketplace": marketplace or self.marketplace, "keyword": keyword, **kw}))

    def google_trend(self, marketplace: str | None = None, **kw) -> dict:
        return self._call("google_trend", {"request": self._clean(self._req(marketplace, **kw))})

    def review(self, asin: str, marketplace: str | None = None, **kw) -> dict:
        return self._call("review", self._clean({
            "marketplace": marketplace or self.marketplace, "asin": asin, **kw}))
