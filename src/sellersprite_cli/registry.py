"""Tool metadata registry — 43 MCP tools organized by business domain."""

from dataclasses import dataclass


@dataclass
class ToolMeta:
    name: str
    domain: str           # asin, product, keyword, traffic, market, trend, trademark
    label: str            # Chinese short description
    required: list[str]   # snake_case param names
    list_params: set[str] # camelCase params accepting comma-separated values
    style: str            # "asin", "request", "request_node", "traffic_stat", "bsr", "review", "flat"
    paginated: bool = True  # whether the tool supports pagination (page/size)


TOOLS: dict[str, ToolMeta] = {
    # ── ASIN 分析 (6) ──
    "asin_detail": ToolMeta("asin_detail", "asin", "ASIN 完整详情", ["asin"], set(), "asin", paginated=False),
    "asin_prediction": ToolMeta("asin_prediction", "asin", "销量与销售额预测", ["asin"], set(), "asin", paginated=False),
    "asin_coupon_trend": ToolMeta("asin_coupon_trend", "asin", "优惠价格趋势", ["asin"], set(), "asin", paginated=False),
    "asin_detail_with_coupon_trend": ToolMeta("asin_detail_with_coupon_trend", "asin", "详情+优惠趋势", ["asin"], set(), "asin", paginated=False),
    "keepa_info": ToolMeta("keepa_info", "asin", "Keepa 历史趋势", ["asin"], set(), "asin", paginated=False),
    "asin_sales_trend": ToolMeta("asin_sales_trend", "asin", "ASIN 销量趋势", ["asin"], set(), "asin", paginated=False),

    # ── 商品与竞品 (3) ──
    "product_research": ToolMeta("product_research", "product", "高级商品筛选", [], {"keywordList"}, "request"),
    "competitor_lookup": ToolMeta("competitor_lookup", "product", "竞品查询", [], {"asins"}, "request"),
    "product_node": ToolMeta("product_node", "product", "产品类目查询", [], set(), "request", paginated=False),

    # ── 关键词 (5) ──
    "keyword_miner": ToolMeta("keyword_miner", "keyword", "关键词深度挖掘", [], {"keywordList"}, "request"),
    "keyword_research": ToolMeta("keyword_research", "keyword", "关键词市场选品", [], {"keywordList"}, "request"),
    "keyword_research_trends": ToolMeta("keyword_research_trends", "keyword", "关键词趋势分析", ["keyword"], set(), "flat", paginated=False),
    "keyword_order": ToolMeta("keyword_order", "keyword", "关键词反查（转化）", ["asins", "reverseType", "date"], {"asins"}, "request"),
    "bsr_prediction": ToolMeta("bsr_prediction", "keyword", "BSR 销量预测", ["bsr", "category_id"], set(), "bsr", paginated=False),

    # ── 流量 (6) ──
    "traffic_keyword": ToolMeta("traffic_keyword", "traffic", "流量关键词明细", ["asin"], set(), "request"),
    "traffic_keyword_stat": ToolMeta("traffic_keyword_stat", "traffic", "流量关键词统计", ["asin"], set(), "traffic_stat", paginated=False),
    "traffic_source": ToolMeta("traffic_source", "traffic", "流量来源分析", [], set(), "request", paginated=False),
    "traffic_listing_stat": ToolMeta("traffic_listing_stat", "traffic", "免费/付费流量结构", ["asin"], set(), "traffic_stat", paginated=False),
    "traffic_listing": ToolMeta("traffic_listing", "traffic", "关联商品查询", ["asin_list", "relations"], {"asinList", "relations"}, "request"),
    "traffic_extend": ToolMeta("traffic_extend", "traffic", "关键词拓展", ["asin_list"], {"asinList"}, "request"),

    # ── 市场分析 (14) ──
    "market_research": ToolMeta("market_research", "market", "类目市场分析", [], set(), "request"),
    "market_research_statistics": ToolMeta("market_research_statistics", "market", "类目统计深度分析", ["node_id_path"], set(), "request_node", paginated=False),
    "market_price_distribution": ToolMeta("market_price_distribution", "market", "价格区间分布", ["node_id_path"], set(), "request_node", paginated=False),
    "market_brand_concentration": ToolMeta("market_brand_concentration", "market", "品牌集中度", ["node_id_path"], set(), "request_node", paginated=False),
    "market_product_concentration": ToolMeta("market_product_concentration", "market", "商品集中度", ["node_id_path"], set(), "request_node", paginated=False),
    "market_seller_concentration": ToolMeta("market_seller_concentration", "market", "卖家集中度", ["node_id_path"], set(), "request_node", paginated=False),
    "market_rating_distribution": ToolMeta("market_rating_distribution", "market", "评分值分布", ["node_id_path"], set(), "request_node", paginated=False),
    "market_ratings_count_distribution": ToolMeta("market_ratings_count_distribution", "market", "评分数分布", ["node_id_path"], set(), "request_node", paginated=False),
    "market_listing_date_distribution": ToolMeta("market_listing_date_distribution", "market", "上架时间分布", ["node_id_path"], set(), "request_node", paginated=False),
    "market_listing_trend_distribution": ToolMeta("market_listing_trend_distribution", "market", "上架时间趋势", ["node_id_path"], set(), "request_node", paginated=False),
    "market_seller_country_distribution": ToolMeta("market_seller_country_distribution", "market", "卖家所属地分布", ["node_id_path"], set(), "request_node", paginated=False),
    "market_seller_type_concentration": ToolMeta("market_seller_type_concentration", "market", "发货类型分布", ["node_id_path"], set(), "request_node", paginated=False),
    "market_ebc_distribution": ToolMeta("market_ebc_distribution", "market", "A+页面与视频分布", ["node_id_path"], set(), "request_node", paginated=False),
    "market_product_demand_trend": ToolMeta("market_product_demand_trend", "market", "需求趋势", ["node_id_path"], set(), "request_node", paginated=False),

    # ── ABA / 趋势 (5) ──
    "aba_research_weekly": ToolMeta("aba_research_weekly", "trend", "ABA 周度趋势", [], {"keywordList"}, "request"),
    "aba_research_monthly": ToolMeta("aba_research_monthly", "trend", "ABA 月度趋势", [], {"keywordList"}, "request"),
    "aba_research_trend": ToolMeta("aba_research_trend", "trend", "ABA 趋势分析", ["keyword"], set(), "flat", paginated=False),
    "google_trend": ToolMeta("google_trend", "trend", "Google 搜索趋势", [], set(), "request", paginated=False),
    "review": ToolMeta("review", "trend", "买家评论查询", ["asin"], set(), "review", paginated=True),

    # ── 商标查询 (4) ──
    "trademark_country_list": ToolMeta("trademark_country_list", "trademark", "商标国家列表", [], set(), "flat", paginated=False),
    "trademark_detail": ToolMeta("trademark_detail", "trademark", "商标详情", ["office", "brand_id"], set(), "flat", paginated=False),
    "trademark_list": ToolMeta("trademark_list", "trademark", "商标列表", ["text"], {"office", "brandName", "status", "applicant", "niceClass", "applicationYear", "expiryYear"}, "request", paginated=True),
    "trademark_stats": ToolMeta("trademark_stats", "trademark", "商标统计", ["office", "text"], {"office"}, "request", paginated=False),
}

ALL_LIST_PARAMS: set[str] = {
    "asinList", "asins", "relations", "keywordList",
    "nodeIdPaths", "excludeKeywords", "includeKeywords",
    "office", "brandName", "status", "applicant", "niceClass", "applicationYear", "expiryYear",
}

# Domain -> display name mapping
DOMAINS: dict[str, str] = {
    "asin": "ASIN 分析",
    "product": "商品与竞品",
    "keyword": "关键词",
    "traffic": "流量",
    "market": "市场分析",
    "trend": "ABA / 趋势",
    "trademark": "商标查询",
}

# Domain -> sorted tool names
DOMAIN_TOOLS: dict[str, list[str]] = {}
for _name, _meta in TOOLS.items():
    DOMAIN_TOOLS.setdefault(_meta.domain, []).append(_name)


def to_camel(name: str) -> str:
    """Convert snake_case or kebab-case to camelCase."""
    parts = name.replace("-", "_").split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
