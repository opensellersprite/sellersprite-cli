# market_product_demand_trend

## 描述

用于分析指定 Amazon 市场类目节点下的商品需求趋势情况。
基于指定细分类目节点，提供该类目的核心市场指标，包括页面浏览量、商品总数、
退货率（市场平均值与同类目平均值）以及搜索购买比（市场平均值与同类目平均值）。
用于评估该细分类目的真实需求规模、用户购买转化效率及退货风险水平，
并通过与同类型类目的对比，判断当前类目在市场吸引力与竞争质量上的相对位置，
辅助卖家进行选品决策与类目进入可行性评估。

## MCP 调用名称

`mcp__sellersprite__market_product_demand_trend`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场 id，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，最早查询时间为2021年7月份，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_product_demand_trend`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/performance`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asinCount | String | asin数量 | 22187 |
| 2 | returnRatio | String | 退货率，百分比 | 1.38 |
| 3 | searchToPurchaseRatio | List | 搜索购买比，千分比 | 3.17875 |
| 4 | avgReturnRatio | Integer | 类目平均退货率，百分比 | 2.72 |
| 5 | avgSearchToPurchaseRatio | Float | 类目平均搜索购买比，千分比 | 2.6 |
| 6 | items | List | 月浏览趋势 |  |
| 7 | └date | String | 时间，yyyy-MM-dd格式 | 2022-09-10 |
| 8 | └glanceViews | Integer | 浏览量 | 2 |

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

