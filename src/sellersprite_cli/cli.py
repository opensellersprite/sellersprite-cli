"""CLI entry point — Typer app with domain-grouped subcommands and interactive TUI."""

import difflib
import json
import os
import platform
import sys
from pathlib import Path
from typing import Annotated, Optional

if sys.stdout and hasattr(sys.stdout, "buffer"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .registry import TOOLS, DOMAINS, DOMAIN_TOOLS, to_camel, ALL_LIST_PARAMS
from .markdown_utils import load_skills, get_skills_by_category, CATEGORY_NAMES, load_skills_index
from .generators import CLIENT_ALIASES, CLIENT_NAMES, generate

app = typer.Typer(
    name="sellersprite",
    help="卖家精灵 CLI — 交互式终端 + MCP 客户端 + 27 AI Skills",
    no_args_is_help=False,
    add_completion=False,
)

console = Console()

# ── Shared state ──────────────────────────────────────────────

_state = {"key": None, "marketplace": "US"}


def _resolve_key(explicit: str | None = None) -> str:
    key = explicit or _state.get("key")
    if not key:
        # 1. Try project-level .env first
        key = _read_env_file(Path.cwd() / ".env")
    if not key:
        # 2. Fall back to global .env
        key = _read_env_file(_global_config_file())
    if not key:
        console.print("[red]缺少 API 密钥。[/red]请执行 sellersprite config --key <你的密钥> 进行配置")
        raise typer.Exit(1)
    return key


def _get_mcp(key: str | None = None, marketplace: str = "US"):
    from .mcp_client import SellerSprite
    return SellerSprite(secret_key=_resolve_key(key), marketplace=marketplace)


def _call_tool(tool_name: str, key: str | None, marketplace: str, **kwargs):
    """Generic tool caller — routes to the right MCP client method."""
    ss = _get_mcp(key, marketplace)
    method = getattr(ss, tool_name)
    cleaned = {k: v for k, v in kwargs.items() if v is not None}
    # 组装 order 排序对象
    order_field = cleaned.pop("order_field", None)
    order_desc = cleaned.pop("order_desc", None)
    if order_field is not None or order_desc is not None:
        order = {}
        if order_field is not None:
            order["field"] = order_field
        if order_desc is not None:
            order["desc"] = order_desc
        cleaned["order"] = order
    # 列表查询默认分页参数（仅对支持分页的工具）
    meta = TOOLS.get(tool_name)
    if meta and meta.paginated:
        size_max = _SIZE_MAX.get(tool_name, 100)
        if "page" not in cleaned:
            cleaned["page"] = 1
        if "size" not in cleaned:
            cleaned["size"] = _SIZE_DEFAULTS.get(tool_name, 50)
        else:
            # 用户显式传入 size，做边界校验
            cleaned["size"] = min(max(1, cleaned["size"]), size_max)
    return method(**cleaned)


def _parse_extra(extra: list[str] | None) -> dict:
    """Parse key=value arguments into a dict with auto-coerced values."""
    result = {}
    if not extra:
        return result
    for item in extra:
        if "=" in item:
            k, v = item.split("=", 1)
            result[k.strip()] = _coerce_arg(k.strip(), v.strip())
    return result


def _coerce_arg(key: str, value: str):
    """Auto-coerce CLI string args to Python types."""
    camel = to_camel(key)
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    if camel in ALL_LIST_PARAMS:
        return [v.strip() for v in value.split(",")]
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def _print_result(data):
    """Pretty-print tool result."""
    if isinstance(data, (dict, list)):
        console.print_json(json.dumps(data, ensure_ascii=False))
    else:
        console.print(str(data))


# ── Root callback (no command = TUI) ──────────────────────────

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    key: Annotated[Optional[str], typer.Option("--key", "-k", help="API 密钥")] = None,
    marketplace: Annotated[str, typer.Option("--marketplace", "-m", help="站点 (默认 US)")] = "US",
):
    """卖家精灵 CLI — 不带子命令时进入交互式 TUI。"""
    _state["key"] = key
    _state["marketplace"] = marketplace
    if ctx.invoked_subcommand is None:
        _run_tui()


# ── Interactive TUI ──────────────────────────────────────────

def _run_tui():
    """Launch interactive terminal UI."""
    from rich.prompt import Prompt

    console.print(Panel(
        "[bold cyan]卖家精灵 CLI[/bold cyan] — 交互式模式\n"
        "选择工具分类，然后选择具体工具执行查询",
        title="SellerSprite",
        border_style="cyan",
    ))

    # Step 1: Select domain
    console.print("\n[bold]选择工具分类:[/bold]")
    domain_keys = list(DOMAINS.keys())
    for i, dk in enumerate(domain_keys, 1):
        tools = DOMAIN_TOOLS.get(dk, [])
        console.print(f"  [cyan]{i}[/cyan]. {DOMAINS[dk]} ({len(tools)} 个工具)")
    console.print(f"  [cyan]0[/cyan]. 退出")

    choice = Prompt.ask("\n请选择", choices=[str(i) for i in range(len(domain_keys) + 1)], default="0")
    if choice == "0":
        return

    domain = domain_keys[int(choice) - 1]
    tool_names = DOMAIN_TOOLS[domain]

    # Step 2: Select tool
    console.print(f"\n[bold]{DOMAINS[domain]} — 选择工具:[/bold]")
    for i, tn in enumerate(tool_names, 1):
        meta = TOOLS[tn]
        console.print(f"  [cyan]{i}[/cyan]. {meta.label} [dim]({tn})[/dim]")
    console.print(f"  [cyan]0[/cyan]. 返回")

    choice = Prompt.ask("\n请选择", choices=[str(i) for i in range(len(tool_names) + 1)], default="0")
    if choice == "0":
        return _run_tui()

    tool_name = tool_names[int(choice) - 1]
    meta = TOOLS[tool_name]

    # Step 3: Collect required params
    kwargs = {}
    console.print(f"\n[bold]执行: {meta.label}[/bold] [dim]({tool_name})[/dim]")

    for param in meta.required:
        val = Prompt.ask(f"  [yellow]{param}[/yellow] (必填)")
        kwargs[param] = _coerce_arg(param, val)

    # Optional params
    console.print("  [dim]输入可选参数 (格式: key=value)，直接回车跳过[/dim]")
    while True:
        extra = Prompt.ask("  可选参数", default="")
        if not extra:
            break
        if "=" in extra:
            k, v = extra.split("=", 1)
            kwargs[k.strip()] = _coerce_arg(k.strip(), v.strip())

    # Step 4: Execute
    console.print(f"\n[dim]正在查询 {tool_name}...[/dim]")
    try:
        result = _call_tool(tool_name, _state["key"], _state["marketplace"], **kwargs)
        _print_result(result)
    except Exception as e:
        console.print(f"[red]错误: {e}[/red]")


# ── Domain sub-apps ──────────────────────────────────────────

asin_app = typer.Typer(help="ASIN 分析 (5 个工具)")
product_app = typer.Typer(help="商品与竞品 (3 个工具)")
keyword_app = typer.Typer(help="关键词 (5 个工具)")
traffic_app = typer.Typer(help="流量 (6 个工具)")
market_app = typer.Typer(help="市场分析 (14 个工具)")
trend_app = typer.Typer(help="ABA / 趋势 (5 个工具)")

app.add_typer(asin_app, name="asin")
app.add_typer(product_app, name="product")
app.add_typer(keyword_app, name="keyword")
app.add_typer(traffic_app, name="traffic")
app.add_typer(market_app, name="market")
app.add_typer(trend_app, name="trend")


# ── Common param annotations ─────────────────────────────────

KeyOpt = Annotated[Optional[str], typer.Option("--key", "-k", help="API 密钥")]
MpOpt = Annotated[str, typer.Option("--marketplace", "-m", help="站点")]
AsinArg = Annotated[str, typer.Argument(help="ASIN 编号")]
SizeOpt = Annotated[Optional[int], typer.Option("--size", help="返回条数")]
PageOpt = Annotated[Optional[int], typer.Option("--page", help="页码")]
OrderFieldOpt = Annotated[Optional[str], typer.Option("--order-field", help="排序字段")]
OrderDescOpt = Annotated[Optional[bool], typer.Option("--order-desc", help="是否降序 true/false")]
ExtraArg = Annotated[Optional[list[str]], typer.Argument(help="额外参数 key=value ...")]


# ── ASIN commands ─────────────────────────────────────────────

@asin_app.command("detail")
def asin_detail(asin: AsinArg, marketplace: MpOpt = "US", key: KeyOpt = None):
    """查询 ASIN 完整详情"""
    _print_result(_call_tool("asin_detail", key, marketplace, asin=asin))


@asin_app.command("predict")
def asin_predict(asin: AsinArg, marketplace: MpOpt = "US", key: KeyOpt = None):
    """销量与销售额预测"""
    _print_result(_call_tool("asin_prediction", key, marketplace, asin=asin))


@asin_app.command("coupon")
def asin_coupon(asin: AsinArg, marketplace: MpOpt = "US", key: KeyOpt = None):
    """优惠价格趋势"""
    _print_result(_call_tool("asin_coupon_trend", key, marketplace, asin=asin))


@asin_app.command("detail-coupon")
def asin_detail_coupon(asin: AsinArg, marketplace: MpOpt = "US", key: KeyOpt = None):
    """详情 + 优惠趋势"""
    _print_result(_call_tool("asin_detail_with_coupon_trend", key, marketplace, asin=asin))


@asin_app.command("keepa")
def asin_keepa(
    asin: AsinArg,
    start_timestamp: Annotated[Optional[int], typer.Option("--start-timestamp", help="趋势起始时间戳(毫秒)")] = None,
    end_timestamp: Annotated[Optional[int], typer.Option("--end-timestamp", help="趋势结束时间戳(毫秒)")] = None,
    daily_latest: Annotated[Optional[bool], typer.Option("--daily-latest", help="仅获取每日最新数据 true/false")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """Keepa 历史趋势"""
    kwargs = {"asin": asin}
    if start_timestamp is not None:
        kwargs["startTimestamp"] = start_timestamp
    if end_timestamp is not None:
        kwargs["endTimestamp"] = end_timestamp
    if daily_latest is not None:
        kwargs["dailyLatest"] = daily_latest
    _print_result(_call_tool("keepa_info", key, marketplace, **kwargs))


# ── Product commands ──────────────────────────────────────────

@product_app.command("search")
def product_search(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    min_price: Annotated[Optional[float], typer.Option("--min-price", help="最低价")] = None,
    max_price: Annotated[Optional[float], typer.Option("--max-price", help="最高价")] = None,
    min_units: Annotated[Optional[int], typer.Option("--min-units", help="最低月销")] = None,
    max_units: Annotated[Optional[int], typer.Option("--max-units", help="最高月销")] = None,
    min_rating: Annotated[Optional[float], typer.Option("--min-rating", help="最低评分")] = None,
    max_rating: Annotated[Optional[float], typer.Option("--max-rating", help="最高评分")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """高级商品筛选"""
    kwargs = _parse_extra(extra)
    if keyword:
        kwargs["keyword"] = keyword
    if min_price is not None:
        kwargs["priceMin"] = min_price
    if max_price is not None:
        kwargs["priceMax"] = max_price
    if min_units is not None:
        kwargs["unitsMin"] = min_units
    if max_units is not None:
        kwargs["unitsMax"] = max_units
    if min_rating is not None:
        kwargs["ratingMin"] = min_rating
    if max_rating is not None:
        kwargs["ratingMax"] = max_rating
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    _print_result(_call_tool("product_research", key, marketplace, **kwargs))


@product_app.command("competitor")
def product_competitor(
    asins: Annotated[Optional[str], typer.Option("--asins", help="ASIN 列表 (逗号分隔)")] = None,
    month: Annotated[Optional[str], typer.Option("--month", help="查询月份 yyyyMM")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """竞品查询"""
    kwargs = _parse_extra(extra)
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    if asins:
        kwargs["asins"] = [a.strip() for a in asins.split(",")]
    if month:
        kwargs["month"] = month
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("competitor_lookup", key, marketplace, **kwargs))


@product_app.command("node")
def product_node(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    node_id_path: Annotated[Optional[str], typer.Option("--node-id-path", help="类目节点路径")] = None,
    month: Annotated[Optional[str], typer.Option("--month", help="查询月份 yyyyMM")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """产品类目查询"""
    kwargs = {}
    if keyword:
        kwargs["keyword"] = keyword
    if node_id_path:
        kwargs["nodeIdPath"] = node_id_path
    if month:
        kwargs["month"] = month
    _print_result(_call_tool("product_node", key, marketplace, **kwargs))


# ── Keyword commands ──────────────────────────────────────────

@keyword_app.command("mine")
def keyword_mine(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    keyword_list: Annotated[Optional[str], typer.Option("--keyword-list", help="关键词列表 (逗号分隔)")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词深度挖掘"""
    kwargs = _parse_extra(extra)
    if keyword:
        kwargs["keyword"] = keyword
    if keyword_list:
        kwargs["keywordList"] = [k.strip() for k in keyword_list.split(",")]
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    _print_result(_call_tool("keyword_miner", key, marketplace, **kwargs))


@keyword_app.command("research")
def keyword_research(
    keywords: Annotated[Optional[str], typer.Option("--keywords", help="关键词")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词市场选品分析"""
    kwargs = _parse_extra(extra)
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    if keywords:
        kwargs["keywords"] = keywords
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("keyword_research", key, marketplace, **kwargs))


@keyword_app.command("order")
def keyword_order(
    date: Annotated[str, typer.Option("--date", help="日期: W模式=yyyyMMdd(当周周六), M模式=yyyyMM")],
    asins: Annotated[Optional[str], typer.Option("--asins", help="ASIN 列表 (逗号分隔)")] = None,
    reverse_type: Annotated[str, typer.Option("--reverse-type", help="反查模式: W=周 M=月")] = "M",
    conversion_type: Annotated[Optional[str], typer.Option("--conversion-type", help="转化类型 (逗号分隔): E=优质词 S=平稳词 L=流失词 I=无效曝光词")] = None,
    variation: Annotated[Optional[str], typer.Option("--variation", help="是否查询变体: Y=否 N=是")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词反查（转化分析）"""
    kwargs = {"reverseType": reverse_type, "date": date,
              "order_field": order_field, "order_desc": order_desc}
    if asins:
        kwargs["asins"] = [a.strip() for a in asins.split(",")]
    if conversion_type:
        kwargs["conversionType"] = [c.strip() for c in conversion_type.split(",")]
    if variation:
        kwargs["variation"] = variation
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("keyword_order", key, marketplace, **kwargs))


@keyword_app.command("bsr")
def keyword_bsr(
    bsr: Annotated[int, typer.Argument(help="BSR 排名")],
    category_id: Annotated[str, typer.Argument(help="类目 ID")],
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """BSR 销量预测"""
    _print_result(_call_tool("bsr_prediction", key, marketplace, bsr=bsr, category_id=category_id))


@keyword_app.command("trends")
def keyword_trends(
    keyword: Annotated[str, typer.Argument(help="关键词")],
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词趋势分析"""
    kwargs = {"keyword": keyword}
    _print_result(_call_tool("keyword_research_trends", key, marketplace, **kwargs))


# ── Traffic commands ──────────────────────────────────────────

@traffic_app.command("keyword")
def traffic_keyword(
    asin: AsinArg,
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    month: Annotated[Optional[str], typer.Option("--month", help="历史月份 yyyyMM")] = None,
    badges: Annotated[Optional[str], typer.Option("--badges", help="流量词类型 (逗号分隔)")] = None,
    traffic_keyword_types: Annotated[Optional[str], typer.Option("--traffic-keyword-types", help="流量占比类型 (逗号分隔)")] = None,
    conversion_keyword_types: Annotated[Optional[str], typer.Option("--conversion-keyword-types", help="转化效果类型 (逗号分隔)")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """流量关键词明细"""
    kwargs = {"asin": asin, "order_field": order_field, "order_desc": order_desc}
    if keyword:
        kwargs["keyword"] = keyword
    if month:
        kwargs["month"] = month
    if badges:
        kwargs["badges"] = [b.strip() for b in badges.split(",")]
    if traffic_keyword_types:
        kwargs["trafficKeywordTypes"] = [t.strip() for t in traffic_keyword_types.split(",")]
    if conversion_keyword_types:
        kwargs["conversionKeywordTypes"] = [c.strip() for c in conversion_keyword_types.split(",")]
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("traffic_keyword", key, marketplace, **kwargs))


@traffic_app.command("keyword-stat")
def traffic_keyword_stat(
    asin: AsinArg,
    month: Annotated[Optional[str], typer.Option("--month", help="历史月份 yyyyMM")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """流量关键词统计"""
    kwargs = {"asin": asin}
    if month:
        kwargs["month"] = month
    _print_result(_call_tool("traffic_keyword_stat", key, marketplace, **kwargs))


@traffic_app.command("source")
def traffic_source(
    month: Annotated[str, typer.Option("--month", help="查询月份 yyyyMM (必填)")],
    asin: Annotated[Optional[str], typer.Option("--asin", help="ASIN 或关键词")] = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """流量来源分析"""
    kwargs = {"order_field": order_field, "order_desc": order_desc, "month": month}
    if asin:
        kwargs["q"] = asin
    _print_result(_call_tool("traffic_source", key, marketplace, **kwargs))


@traffic_app.command("listing-stat")
def traffic_listing_stat(
    asin: AsinArg,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """免费/付费流量结构"""
    _print_result(_call_tool("traffic_listing_stat", key, marketplace, asin=asin))


@traffic_app.command("listing")
def traffic_listing(
    asin_list: Annotated[str, typer.Option("--asin-list", help="ASIN 列表 (逗号分隔)")],
    relations: Annotated[str, typer.Option("--relations", help="关联类型 (逗号分隔)")],
    variations: Annotated[Optional[bool], typer.Option("--variations", help="是否查询变体 true/false")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关联商品查询"""
    kwargs = {
        "asin_list": [a.strip() for a in asin_list.split(",")],
        "relations": [r.strip() for r in relations.split(",")],
        "order_field": order_field,
        "order_desc": order_desc,
    }
    if variations is not None:
        kwargs["variations"] = variations
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("traffic_listing", key, marketplace, **kwargs))


@traffic_app.command("extend")
def traffic_extend(
    asin_list: Annotated[str, typer.Option("--asin-list", help="ASIN 列表 (逗号分隔)")],
    query_type: Annotated[int, typer.Option("--query-type", help="查询方式: 0=所有变体 1=畅销变体 2=当前变体")] = 2,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词拓展"""
    kwargs = _parse_extra(extra)
    kwargs["asin_list"] = [a.strip() for a in asin_list.split(",")]
    kwargs["query_type"] = query_type
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    _print_result(_call_tool("traffic_extend", key, marketplace, **kwargs))


# ── Market commands ───────────────────────────────────────────

@market_app.command("research")
def market_research(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """类目市场分析"""
    kwargs = _parse_extra(extra)
    if keyword:
        kwargs["keyword"] = keyword
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    _print_result(_call_tool("market_research", key, marketplace, **kwargs))


def _make_market_command(tool_name: str, label: str):
    """Factory for market analysis commands that all take node_id_path."""
    def cmd(
        node_id_path: Annotated[str, typer.Option("--node-id-path", help="类目节点路径")],
        month: Annotated[Optional[str], typer.Option("--month", help="筛选日期 yyyyMM，默认最近30天，最早支持2021年7月")] = None,
        top_n: Annotated[Optional[int], typer.Option("--top-n", help="头部Listing数量，仅需求趋势有效")] = None,
        new_product: Annotated[Optional[int], typer.Option("--new-product", help="新品定义阈值（月），仅需求趋势有效")] = None,
        marketplace: MpOpt = "US",
        key: KeyOpt = None,
    ):
        kwargs = {"node_id_path": node_id_path}
        # Only add month for tools that support it
        if tool_name in ("market_research_statistics", "market_listing_trend_distribution", "market_product_demand_trend"):
            if month:
                kwargs["month"] = month
        # Only add demand-trend-specific params
        if tool_name == "market_product_demand_trend":
            if top_n is not None:
                kwargs["top_n"] = top_n
            if new_product is not None:
                kwargs["new_product"] = new_product
        _print_result(_call_tool(tool_name, key, marketplace, **kwargs))
    cmd.__doc__ = label
    return cmd


# Dynamically register all node-based market commands
_NODE_COMMANDS = {
    "market_research_statistics": ("stats", "类目统计深度分析"),
    "market_price_distribution": ("price", "价格区间分布"),
    "market_brand_concentration": ("brand", "品牌集中度"),
    "market_product_concentration": ("product", "商品集中度"),
    "market_seller_concentration": ("seller", "卖家集中度"),
    "market_rating_distribution": ("rating", "评分值分布"),
    "market_ratings_count_distribution": ("ratings-count", "评分数分布"),
    "market_listing_date_distribution": ("listing-date", "上架时间分布"),
    "market_listing_trend_distribution": ("listing-trend", "上架时间趋势"),
    "market_seller_country_distribution": ("seller-country", "卖家所属地分布"),
    "market_seller_type_concentration": ("seller-type", "发货类型分布"),
    "market_ebc_distribution": ("ebc", "A+页面与视频分布"),
    "market_product_demand_trend": ("demand", "需求趋势"),
}

for _tool, (_cmd_name, _label) in _NODE_COMMANDS.items():
    market_app.command(name=_cmd_name)(_make_market_command(_tool, _label))


# ── Trend commands ────────────────────────────────────────────

@trend_app.command("aba-weekly")
def trend_aba_weekly(
    keyword_list: Annotated[Optional[str], typer.Option("--keyword-list", help="关键词列表 (逗号分隔)")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """ABA 周度趋势"""
    kwargs = _parse_extra(extra)
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    if keyword_list:
        kwargs["keywordList"] = [k.strip() for k in keyword_list.split(",")]
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("aba_research_weekly", key, marketplace, **kwargs))


@trend_app.command("aba-monthly")
def trend_aba_monthly(
    keyword_list: Annotated[Optional[str], typer.Option("--keyword-list", help="关键词列表 (逗号分隔)")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    order_field: OrderFieldOpt = None,
    order_desc: OrderDescOpt = None,
    extra: ExtraArg = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """ABA 月度趋势"""
    kwargs = _parse_extra(extra)
    if order_field is not None:
        kwargs["order_field"] = order_field
    if order_desc is not None:
        kwargs["order_desc"] = order_desc
    if keyword_list:
        kwargs["keywordList"] = [k.strip() for k in keyword_list.split(",")]
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("aba_research_monthly", key, marketplace, **kwargs))


@trend_app.command("aba-trend")
def trend_aba_trend(
    keyword: Annotated[str, typer.Argument(help="关键词")],
    time_granularity: Annotated[Optional[str], typer.Option("--time-granularity", help="时间粒度")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """ABA 趋势分析"""
    kwargs = {"keyword": keyword}
    if time_granularity:
        kwargs["timeGranularity"] = time_granularity
    _print_result(_call_tool("aba_research_trend", key, marketplace, **kwargs))


@trend_app.command("google")
def trend_google(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    google_prop: Annotated[Optional[str], typer.Option("--google-prop", help="类别: web=网页搜索, shoppingCart=购物搜索")] = None,
    monthly: Annotated[Optional[bool], typer.Option("--monthly", help="是否按月份 true/false")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """Google 搜索趋势"""
    kwargs = {}
    if keyword:
        kwargs["keyword"] = keyword
    if google_prop:
        kwargs["googleProp"] = google_prop
    if monthly is not None:
        kwargs["monthly"] = monthly
    _print_result(_call_tool("google_trend", key, marketplace, **kwargs))


@trend_app.command("review")
def trend_review(
    asin: AsinArg,
    star_list: Annotated[Optional[str], typer.Option("--star-list", help="评论星级 (逗号分隔): 1-5")] = None,
    type_list: Annotated[Optional[str], typer.Option("--type-list", help="评论类型 (逗号分隔): 1=图片 2=视频 3=VP 4=VINE")] = None,
    page: PageOpt = None,
    size: SizeOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """买家评论查询"""
    kwargs = {"asin": asin}
    if star_list:
        kwargs["starList"] = [int(s.strip()) for s in star_list.split(",")]
    if type_list:
        kwargs["typeList"] = [int(t.strip()) for t in type_list.split(",")]
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    _print_result(_call_tool("review", key, marketplace, **kwargs))


# 工具特定的 size 默认值和上限（来自 API 文档）
_SIZE_DEFAULTS = {
    "keyword_research": 15,
    "review": 10,
    "aba_research_weekly": 40,
    "aba_research_monthly": 15,
    "traffic_extend": 50,
    "traffic_keyword": 100,
    "traffic_listing": 100,
    "traffic_source": 100,
}
_SIZE_MAX = {
    "keyword_research": 15,
    "review": 10,
    "aba_research_weekly": 40,
    "aba_research_monthly": 15,
    "traffic_extend": 50,
}

# Mapping: tool_name -> CLI command path
_TOOL_COMMANDS = {
    "asin_detail": "sellersprite asin detail",
    "asin_prediction": "sellersprite asin predict",
    "asin_coupon_trend": "sellersprite asin coupon",
    "asin_detail_with_coupon_trend": "sellersprite asin detail-coupon",
    "keepa_info": "sellersprite asin keepa",
    "product_research": "sellersprite product search",
    "competitor_lookup": "sellersprite product competitor",
    "product_node": "sellersprite product node",
    "keyword_miner": "sellersprite keyword mine",
    "keyword_research": "sellersprite keyword research",
    "keyword_order": "sellersprite keyword order",
    "keyword_research_trends": "sellersprite keyword trends",
    "bsr_prediction": "sellersprite keyword bsr",
    "traffic_keyword": "sellersprite traffic keyword",
    "traffic_keyword_stat": "sellersprite traffic keyword-stat",
    "traffic_source": "sellersprite traffic source",
    "traffic_listing_stat": "sellersprite traffic listing-stat",
    "traffic_listing": "sellersprite traffic listing",
    "traffic_extend": "sellersprite traffic extend",
    "market_research": "sellersprite market research",
    "market_research_statistics": "sellersprite market stats",
    "market_price_distribution": "sellersprite market price",
    "market_brand_concentration": "sellersprite market brand",
    "market_product_concentration": "sellersprite market product",
    "market_seller_concentration": "sellersprite market seller",
    "market_rating_distribution": "sellersprite market rating",
    "market_ratings_count_distribution": "sellersprite market ratings-count",
    "market_listing_date_distribution": "sellersprite market listing-date",
    "market_listing_trend_distribution": "sellersprite market listing-trend",
    "market_seller_country_distribution": "sellersprite market seller-country",
    "market_seller_type_concentration": "sellersprite market seller-type",
    "market_ebc_distribution": "sellersprite market ebc",
    "market_product_demand_trend": "sellersprite market demand",
    "aba_research_weekly": "sellersprite trend aba-weekly",
    "aba_research_monthly": "sellersprite trend aba-monthly",
    "aba_research_trend": "sellersprite trend aba-trend",
    "google_trend": "sellersprite trend google",
    "review": "sellersprite trend review",
}


@app.command("list")
def list_tools():
    """列出所有 38 个可用工具"""
    for domain, tools in DOMAIN_TOOLS.items():
        table = Table(title=DOMAINS.get(domain, domain), show_header=True,
                      header_style="bold cyan")
        table.add_column("命令", style="green")
        table.add_column("说明")
        for tn in tools:
            table.add_row(_TOOL_COMMANDS.get(tn, f"sellersprite {domain} {tn}"), TOOLS[tn].label)
        console.print(table)
        console.print()
    try:
        console.print(f"[bold]共 {len(TOOLS)} 个工具[/bold]")
    except OSError:
        print(f"共 {len(TOOLS)} 个工具")


# ── Config helpers ───────────────────────────────────────────

def _global_config_dir() -> Path:
    """Return the global config directory (cross-platform)."""
    if platform.system() == "Windows":
        app_data = os.environ.get("APPDATA") or str(Path.home() / "AppData" / "Roaming")
        return Path(app_data) / "sellersprite"
    return Path.home() / ".config" / "sellersprite"


def _global_config_file() -> Path:
    """Return the global config file path."""
    return _global_config_dir() / ".env"


def _read_env_file(env_file: Path) -> str:
    """Read SELLERSPRITE_KEY from a .env file."""
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("SELLERSPRITE_KEY="):
                return line.split("=", 1)[1].strip().strip("\"'")
    return ""


def _write_env_file(env_file: Path, key: str) -> None:
    """Write SELLERSPRITE_KEY to a .env file."""
    env_file.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    replaced = False

    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("SELLERSPRITE_KEY="):
                lines.append(f"SELLERSPRITE_KEY={key}")
                replaced = True
            else:
                lines.append(line)

    if not replaced:
        lines.append(f"SELLERSPRITE_KEY={key}")

    env_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── Config command ────────────────────────────────────────────

@app.command("config")
def config_key(
    key: Annotated[Optional[str], typer.Option("--key", "-k", help="API 密钥")] = None,
    project: Annotated[bool, typer.Option("--project", "-p", help="保存到当前项目 .env 文件（覆盖全局密钥）")] = False,
):
    """配置 API 密钥（默认保存到全局配置文件）"""
    from rich.prompt import Prompt

    if not key:
        key = Prompt.ask("请输入你的 SellerSprite API 密钥", password=True)

    key = key.strip().strip("\"'")
    if not key:
        console.print("[red]密钥不能为空[/red]")
        raise typer.Exit(1)

    if project:
        env_file = Path.cwd() / ".env"
        _write_env_file(env_file, key)
        console.print(f"[green]密钥已保存到 {env_file}[/green]")
        console.print("[dim]提示：当前项目优先使用此密钥，其他项目仍使用全局配置[/dim]")
        return

    config_file = _global_config_file()
    _write_env_file(config_file, key)
    console.print(f"[green]密钥已保存到 {config_file}[/green]")


# ── Init command ──────────────────────────────────────────────

@app.command("init")
def init_client(
    client: Annotated[Optional[str], typer.Argument(help="客户端名称")] = None,
    all_clients: Annotated[bool, typer.Option("--all", help="生成所有客户端配置")] = False,
    skills: Annotated[bool, typer.Option("--skills", help="同时复制 Skills 文件")] = False,
    project: Annotated[Optional[str], typer.Option("--project", help="目标项目目录")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="预览模式")] = False,
    key: KeyOpt = None,
):
    """生成 AI 客户端 MCP 配置"""
    if all_clients:
        clients = sorted(CLIENT_NAMES)
    elif client:
        clients = [client]
    else:
        console.print("[red]请指定客户端名称或使用 --all[/red]")
        console.print(f"可用客户端: {', '.join(sorted(CLIENT_NAMES))}")
        raise typer.Exit(1)

    # Resolve known aliases (e.g. "claude" → "claude-code") with a notice.
    resolved = []
    for c in clients:
        canonical = CLIENT_ALIASES.get(c)
        if canonical:
            console.print(f"[yellow]提示: '{c}' 已解析为 '{canonical}'[/yellow]")
            resolved.append(canonical)
        else:
            resolved.append(c)
    clients = resolved

    unknown = [c for c in clients if c not in CLIENT_NAMES]
    if unknown:
        for u in unknown:
            suggestions = difflib.get_close_matches(
                u, sorted(CLIENT_NAMES), n=3, cutoff=0.4
            )
            console.print(f"[red]未知客户端: {u}[/red]")
            if suggestions:
                console.print(f"[yellow]  你是不是想用: {', '.join(suggestions)}?[/yellow]")
        console.print(f"可用客户端: {', '.join(sorted(CLIENT_NAMES))}")
        raise typer.Exit(1)

    project_dir = Path(project).resolve() if project else Path.cwd()
    api_key = _resolve_key(key)

    for name in clients:
        msgs = generate(name, api_key, project_dir, skills=skills, dry_run=dry_run)
        for msg in msgs:
            if msg.startswith("  wrote:") or msg.startswith("  copied:"):
                console.print(f"[green]{msg}[/green]")
            elif msg.startswith("  ["):
                console.print(f"[yellow]{msg}[/yellow]")
            else:
                console.print(f"[bold]{msg}[/bold]")
        console.print()


# ── Skill commands ────────────────────────────────────────────

@app.command("skill")
def skill_cmd(
    action: Annotated[Optional[str], typer.Argument(help="list | show")] = None,
    name: Annotated[Optional[str], typer.Option("--name", "-n", help="Skill 名称")] = None,
):
    """查看 Skills 技能卡片"""
    if action == "list" or action is None:
        _skill_list()
    elif action == "show":
        if not name:
            console.print("[red]请指定 --name[/red]")
            raise typer.Exit(1)
        _skill_show(name)
    else:
        console.print(f"[red]未知操作: {action}[/red]")
        console.print("可用操作: list, show")
        raise typer.Exit(1)


def _skill_list():
    """List all skills in a table."""
    by_category = get_skills_by_category()
    for cat, cards in by_category.items():
        cat_label = CATEGORY_NAMES.get(cat, cat)
        table = Table(title=cat_label, show_header=True, header_style="bold cyan")
        table.add_column("名称", style="green")
        table.add_column("文件")
        for card in cards:
            table.add_row(card.name, str(card.path.name))
        console.print(table)
        console.print()
    console.print(f"[bold]共 {sum(len(c) for c in by_category.values())} 个 Skills[/bold]")


def _skill_show(name: str):
    """Show a specific skill's content."""
    for card in load_skills():
        if card.name == name:
            console.print(Panel(card.content, title=card.name, border_style="cyan"))
            return
    console.print(f"[red]未找到 Skill: {name}[/red]")
    console.print("使用 [bold]sellersprite skill list[/bold] 查看所有可用 Skills")


# ── Docs command ──────────────────────────────────────────────

_DOCS_DIR = Path(__file__).parent / "reference"


def _parse_md_table(content: str, section_markers: tuple[str, ...] = ("## 参数", "### 请求参数")) -> list[list[str]] | None:
    """Extract markdown table rows from a parameter section."""
    lines = content.splitlines()
    in_section = False
    table_lines: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not in_section:
            if any(stripped.startswith(m) for m in section_markers):
                in_section = True
            continue
        # In section: collect table lines until blank line or new section
        if stripped.startswith("#"):
            break
        if stripped.startswith("|"):
            table_lines.append(stripped)
        elif table_lines and not stripped:
            # Allow one blank line inside table, but stop after consecutive blanks
            pass

    if len(table_lines) < 3:
        return None

    # Skip header separator line (contains ---)
    rows: list[list[str]] = []
    for line in table_lines:
        if "---" in line.replace(" ", ""):
            continue
        cells = [cell.strip().strip("`") for cell in line.split("|")[1:-1]]
        if cells and any(cells):
            rows.append(cells)

    return rows if len(rows) >= 2 else None


@app.command("docs")
def docs_cmd(
    tool: Annotated[str, typer.Argument(help="工具名称，例如 product_research, traffic_keyword")],
):
    """查看接口参数文档"""
    meta = TOOLS.get(tool)
    if not meta:
        console.print(f"[red]未知工具: {tool}[/red]")
        console.print(f"可用工具: {', '.join(TOOLS.keys())}")
        raise typer.Exit(1)

    # Try individual doc first
    doc_file = _DOCS_DIR / f"{tool}.md"
    content = None
    if doc_file.exists():
        content = doc_file.read_text(encoding="utf-8")
    else:
        # Fallback to mcp-api-source.md
        mcp_file = Path(__file__).parent.parent.parent / "docs" / "mcp-api-source.md"
        if mcp_file.exists():
            full = mcp_file.read_text(encoding="utf-8")
            # Find the section for this tool
            pattern = f"## \\d+\\. .*\\(`{tool}`\\)"
            import re
            match = re.search(pattern, full)
            if match:
                start = match.start()
                end = full.find("\n## ", start + 1)
                if end == -1:
                    end = len(full)
                content = full[start:end]

    if not content:
        console.print(f"[red]未找到 {tool} 的文档[/red]")
        raise typer.Exit(1)

    rows = _parse_md_table(content)
    if not rows:
        console.print(f"[yellow]{tool} 文档中未找到参数表格[/yellow]")
        raise typer.Exit(1)

    # Build table
    table = Table(title=f"{meta.label} — {tool}", show_header=True, header_style="bold cyan")
    headers = rows[0]
    for h in headers:
        table.add_column(h)
    for row in rows[1:]:
        # Truncate very long descriptions
        cells = [c[:80] + "..." if len(c) > 80 else c for c in row]
        # Pad short rows
        while len(cells) < len(headers):
            cells.append("")
        table.add_row(*cells[:len(headers)])

    console.print(table)
    console.print(f"\n[dim]提示: 支持 extra key=value 传参的命令可用这些字段[/dim]")
