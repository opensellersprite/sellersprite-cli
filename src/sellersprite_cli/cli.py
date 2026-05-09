"""CLI entry point — Typer app with domain-grouped subcommands and interactive TUI."""

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
from .generators import CLIENT_NAMES, generate

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
    key = explicit or _state.get("key") or os.environ.get("SELLERSPRITE_KEY", "")
    if not key:
        # Try .env file
        env_file = Path.cwd() / ".env"
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("SELLERSPRITE_KEY="):
                    key = line.split("=", 1)[1].strip().strip("\"'")
                    break
    if not key:
        console.print("[red]缺少 API 密钥。[/red]请设置 SELLERSPRITE_KEY 环境变量或使用 --key")
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
    return method(**cleaned)


def _coerce_arg(key: str, value: str):
    """Auto-coerce CLI string args to Python types."""
    camel = to_camel(key)
    if value.lower() in ("true", "yes", "y"):
        return True
    if value.lower() in ("false", "no", "n"):
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
def asin_keepa(asin: AsinArg, marketplace: MpOpt = "US", key: KeyOpt = None):
    """Keepa 历史趋势"""
    _print_result(_call_tool("keepa_info", key, marketplace, asin=asin))


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
    page: Annotated[Optional[int], typer.Option("--page", help="页码")] = None,
    size: SizeOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """高级商品筛选"""
    _print_result(_call_tool("product_research", key, marketplace,
                             keyword=keyword, priceMin=min_price, priceMax=max_price,
                             unitsMin=min_units, unitsMax=max_units,
                             ratingMin=min_rating, ratingMax=max_rating,
                             page=page, size=size))


@product_app.command("competitor")
def product_competitor(
    asins: Annotated[Optional[str], typer.Option("--asins", help="ASIN 列表 (逗号分隔)")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """竞品查询"""
    kwargs = {}
    if asins:
        kwargs["asins"] = [a.strip() for a in asins.split(",")]
    _print_result(_call_tool("competitor_lookup", key, marketplace, **kwargs))


@product_app.command("node")
def product_node(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """产品类目查询"""
    _print_result(_call_tool("product_node", key, marketplace, keyword=keyword))


# ── Keyword commands ──────────────────────────────────────────

@keyword_app.command("mine")
def keyword_mine(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    keyword_list: Annotated[Optional[str], typer.Option("--keyword-list", help="关键词列表 (逗号分隔)")] = None,
    size: SizeOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词深度挖掘"""
    kwargs = {}
    if keyword:
        kwargs["keyword"] = keyword
    if keyword_list:
        kwargs["keywordList"] = [k.strip() for k in keyword_list.split(",")]
    if size:
        kwargs["size"] = size
    _print_result(_call_tool("keyword_miner", key, marketplace, **kwargs))


@keyword_app.command("research")
def keyword_research(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    keyword_list: Annotated[Optional[str], typer.Option("--keyword-list", help="关键词列表 (逗号分隔)")] = None,
    size: SizeOpt = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词市场选品分析"""
    kwargs = {}
    if keyword:
        kwargs["keywords"] = keyword
    if keyword_list:
        kwargs["keywordList"] = [k.strip() for k in keyword_list.split(",")]
    if size:
        kwargs["size"] = size
    _print_result(_call_tool("keyword_research", key, marketplace, **kwargs))


@keyword_app.command("order")
def keyword_order(
    asins: Annotated[Optional[str], typer.Option("--asins", help="ASIN 列表 (逗号分隔)")] = None,
    reverse_type: Annotated[str, typer.Option("--reverse-type", help="反查模式: W=周 M=月")] = "M",
    date: Annotated[Optional[str], typer.Option("--date", help="周(yyyyMMdd) 或 月(YYYYMM)")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词反查（转化分析）"""
    kwargs = {"reverseType": reverse_type}
    if asins:
        kwargs["asins"] = [a.strip() for a in asins.split(",")]
    if date:
        kwargs["date"] = date
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
    month: Annotated[Optional[str], typer.Option("--month", help="月份 (YYYY-MM)")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词趋势分析"""
    kwargs = {"keyword": keyword}
    if month:
        kwargs["month"] = month
    _print_result(_call_tool("keyword_research_trends", key, marketplace, **kwargs))


# ── Traffic commands ──────────────────────────────────────────

@traffic_app.command("keyword")
def traffic_keyword(
    asin: AsinArg,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """流量关键词明细"""
    _print_result(_call_tool("traffic_keyword", key, marketplace, asin=asin))


@traffic_app.command("keyword-stat")
def traffic_keyword_stat(
    asin: AsinArg,
    month: Annotated[Optional[str], typer.Option("--month", help="月份 (YYYY-MM)")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """流量关键词统计"""
    _print_result(_call_tool("traffic_keyword_stat", key, marketplace, asin=asin, month=month))


@traffic_app.command("source")
def traffic_source(
    asin: Annotated[Optional[str], typer.Option("--asin", help="ASIN")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """流量来源分析"""
    kwargs = {}
    if asin:
        kwargs["asin"] = asin
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
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关联商品查询"""
    _print_result(_call_tool("traffic_listing", key, marketplace,
                             asin_list=[a.strip() for a in asin_list.split(",")],
                             relations=[r.strip() for r in relations.split(",")]))


@traffic_app.command("extend")
def traffic_extend(
    asin_list: Annotated[str, typer.Option("--asin-list", help="ASIN 列表 (逗号分隔)")],
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """关键词拓展"""
    _print_result(_call_tool("traffic_extend", key, marketplace,
                             asin_list=[a.strip() for a in asin_list.split(",")]))


# ── Market commands ───────────────────────────────────────────

@market_app.command("research")
def market_research(
    keyword: Annotated[Optional[str], typer.Option("--keyword", help="关键词")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """类目市场分析"""
    _print_result(_call_tool("market_research", key, marketplace, keyword=keyword))


def _make_market_command(tool_name: str, label: str):
    """Factory for market analysis commands that all take node_id_path."""
    def cmd(
        node_id_path: Annotated[str, typer.Option("--node-id-path", help="类目节点路径")],
        marketplace: MpOpt = "US",
        key: KeyOpt = None,
    ):
        _print_result(_call_tool(tool_name, key, marketplace, node_id_path=node_id_path))
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
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """ABA 周度趋势"""
    kwargs = {}
    if keyword_list:
        kwargs["keywordList"] = [k.strip() for k in keyword_list.split(",")]
    _print_result(_call_tool("aba_research_weekly", key, marketplace, **kwargs))


@trend_app.command("aba-monthly")
def trend_aba_monthly(
    keyword_list: Annotated[Optional[str], typer.Option("--keyword-list", help="关键词列表 (逗号分隔)")] = None,
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """ABA 月度趋势"""
    kwargs = {}
    if keyword_list:
        kwargs["keywordList"] = [k.strip() for k in keyword_list.split(",")]
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
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """Google 搜索趋势"""
    _print_result(_call_tool("google_trend", key, marketplace, keyword=keyword))


@trend_app.command("review")
def trend_review(
    asin: AsinArg,
    category_id: Annotated[str, typer.Argument(help="类目 ID")],
    marketplace: MpOpt = "US",
    key: KeyOpt = None,
):
    """买家评论查询"""
    _print_result(_call_tool("review", key, marketplace, asin=asin, categoryId=category_id))


# ── List command ──────────────────────────────────────────────

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
    console.print(f"[bold]共 {len(TOOLS)} 个工具[/bold]")


# ── Config command ────────────────────────────────────────────

@app.command("config")
def config_key(
    key: Annotated[Optional[str], typer.Option("--key", "-k", help="API 密钥")] = None,
):
    """配置 API 密钥（保存到 .env 文件）"""
    from rich.prompt import Prompt

    if not key:
        key = Prompt.ask("请输入你的 SellerSprite API 密钥", password=True)

    key = key.strip().strip("\"'")
    if not key:
        console.print("[red]密钥不能为空[/red]")
        raise typer.Exit(1)

    env_file = Path.cwd() / ".env"
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

    console.print(f"[green]密钥已保存到 {env_file}[/green]")

    # Show OS-specific hints
    sys_name = platform.system()
    console.print("\n[bold]你也可以通过环境变量临时设置：[/bold]")
    if sys_name == "Windows":
        console.print(f"  [cyan]CMD:[/cyan]    set SELLERSPRITE_KEY={key}")
        console.print(f"  [cyan]PowerShell:[/cyan] $env:SELLERSPRITE_KEY = \"{key}\"")
    elif sys_name == "Darwin":
        console.print(f"  [cyan]zsh/bash:[/cyan] export SELLERSPRITE_KEY=\"{key}\"")
    else:
        console.print(f"  [cyan]bash:[/cyan] export SELLERSPRITE_KEY=\"{key}\"")
    console.print("\n[dim]提示：.env 文件中的密钥会自动被 sellersprite 读取，无需每次 export[/dim]")


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

    unknown = [c for c in clients if c not in CLIENT_NAMES]
    if unknown:
        console.print(f"[red]未知客户端: {', '.join(unknown)}[/red]")
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
