# market_research_statistics

## 描述

Amazon 类目结构与机会分析工具（节点级）。

用于在“已明确类目节点”的前提下，系统分析该类目的：
- 市场规模与成熟度
- 头部 Listing 的竞争强度与垄断程度
- 新品在该类目中的生存与成长能力
- 平均价格、利润率、销量是否具备商业价值

与“全类目筛选工具”不同，
本工具更适合在【已选定类目】后，做深入可行性验证。

该工具重点回答的问题包括：
- 这个具体类目现在是否已经过于成熟？
- 头部 Listing 是否形成强垄断？
- 新品是否还能在该类目中跑出来？
- 新品与头部商品在价格、销量、评价上的差距有多大？

典型使用场景：
- 选品前，对目标类目做深度市场验证
- 判断是否值得进入某一个细分节点
- 分析“做头部款”还是“做新品切入”

## MCP 调用名称

`mcp__sellersprite__market_research_statistics`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_research_statistics`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/research/statistics`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场标志 | US |
| 2 | currency | String | 该市场的货币类型 | USD |
| 3 | nodeIdPath | String | 节点ID路径 | 1064954:1069242:1069784:1069820:1069838:1069828 |
| 4 | nodeLabelPath | String | 节点名称路径 | Office Products:Office & School Supplies:Writing & Correction Supplies:Pens & Refills:Rollerball Pens:Gel Ink Rollerball Pens |
| 5 | nodeLabelLocale | String | 节点名称翻译 | 办公产品:办公室:写作:钢笔:滚珠笔:中性笔 |
| 6 | countryCode | String | 国家二简码 | US |
| 7 | totalProducts | Integer | 商品总数 | 5127 |
| 8 | products | Integer | 样品商品数 | 100 |
| 9 | brands | Integer | 品牌数 | 4 |
| 10 | sellers | Integer | 卖家数 | 58 |
| 11 | avgBsr | Integer | 平均BSR | 41970 |
| 12 | baseAvgVolume | Float | 平均体积(cm³) | 819942.68 |
| 13 | avgVolume | Float | 平均体积(in³) | 50035.97 |
| 14 | baseAvgWeight | Float | 平均重量(g) | 2460.95 |
| 15 | avgWeight | Float | 平均重量(pound) | 5.4255 |
| 16 | avgProfit | Float | 平均利润率 | 66.03 |
| 17 | avgUnits | Integer | 月均销量 | 26255 |
| 18 | avgRevenue | Float | 月均销售额 | 344369 |
| 19 | avgPrice | Float | 平均价格 | 13.91 |
| 20 | avgRatingsCv | Integer | 月评论平均增长数 | 0 |
| 21 | avgRatings | Integer | 平均评分数 | 19071 |
| 22 | avgRating | Float | 平均星级 | 4.7 |
| 23 | avgSellers | Float | 平均卖家数 | 5.2 |
| 24 | hlProducts | Integer | 头部Listing前N名商品样本数 | 5 |
| 25 | hlAvgBsr | Integer | 头部Listing前N名商品平均BSR | 13126 |
| 26 | hlAvgUnits | Integer | 头部Listing前N名商品月均销量 | 1123 |
| 27 | hlAvgRevenue | Float | 头部Listing前N名商品月均销售额 | 12342.85 |
| 28 | hlAvgPrice | Float | 头部Listing前N名商品平均价格 | 11.77 |
| 29 | hlAvgRatingsCv | Integer | 头部Listing前N名商品月评论平均增长数 | 0 |
| 30 | hlAvgRatings | Integer | 头部Listing前N名商品平均评论数 | 2794 |
| 31 | hlAvgRating | Float | 头部Listing前N名商品平均星级 | 4.7 |
| 32 | newProducts | Integer | 新品数量 | 67 |
| 33 | newProductProportion | Float | 新品数量占比 | 67 |
| 34 | newAvgPrice | Float | 新品平均价格 | 14.14 |
| 35 | newAvgRatings | Integer | 新品平均评分数 | 24295 |
| 36 | minNewRatings | Integer | 最低新品评分数 | 24 |
| 37 | maxNewRatings | Integer | 最高新品评分数 | 6432 |
| 38 | newAvgRating | Float | 新品平均星级 | 4.7 |
| 39 | newAvgUnits | Integer | 新品月均销量 | 26425 |
| 40 | newAvgRevenue | Float | 新品月均销售额 | 350209.91 |
| 41 | firstShelfDate | String | 商品首次上架日期 | 2014-10-30 |
| 42 | lastShelfDate | String | 商品最新上架日期 | 2021-04-28 |

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "month": "202604",
    "newProduct": 6,
    "nodeIdPath": "2619525011:3741271",
    "topN": 10
  }
}
```

