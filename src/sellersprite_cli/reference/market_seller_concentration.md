# market_seller_concentration

## 描述

用于分析指定 Amazon 市场类目节点下的卖家集中度情况。
在指定样本商品范围内，计算头部卖家（如销量排名前 N 位卖家）的总销量 U，
并与样本商品总销量 A 进行对比，卖家集中度 = U / A。
该指标用于衡量类目销量是否高度集中在少数头部卖家手中，
比例越高，说明头部卖家垄断程度越强，市场竞争壁垒越高。
同时支持同级类目卖家集中度对比，用于判断当前类目相对于同级类目的竞争集中程度是否偏高或偏低。

## MCP 调用名称

`mcp__sellersprite__market_seller_concentration`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_seller_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-concentration`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | name | String | 卖家名称 | JA Wholesale LLC |
| 2 | ranking | Integer | 排名 | 1 |
| 3 | asinSet | List | 包含的商品ASIN集合 | ["B00P19MFYE"] |
| 4 | products | Integer | 商品数量，包含新品 | 4 |
| 5 | newProducts | Integer | 新品数量 | 1 |
| 6 | newUnits | Integer | 新品销量 | 45 |
| 7 | newRevenue | Float | 新品销售额 | 2342 |
| 8 | newUnitsRatio | Float | 新品销量占比 | 4.3 |
| 9 | newRevenueRatio | Float | 新品销售额占比 | 4 |
| 10 | avgPrice | Float | 平均价格 | 6.19 |
| 11 | ratings | Integer | 评分数 | 5695 |
| 12 | rating | Float | 评分值 | 4.8 |
| 13 | reviews | Integer | 评论数 | 234 |
| 14 | totalUnits | Integer | 总销量 | 32342 |
| 15 | totalRevenue | Float | 总销额 | 18837.35 |
| 16 | totalUnitsRatio | Float | 总销量占比 | 0.4478 |
| 17 | totalRevenueRatio | Float | 总销额占比 | 0.3052 |

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

