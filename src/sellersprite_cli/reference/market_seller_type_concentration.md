# market_seller_type_concentration

## 描述

用于分析指定 Amazon 市场类目节点下的卖家发货类型竞争情况。
在指定样本商品范围内，按照卖家发货类型（如 Amazon 自营、FBA、FBM 等）进行分组，
统计各发货类型的 ASIN 数量占比及其对应的月销量占比，
用于判断不同发货方式在市场中的商品覆盖度与销量贡献度。
同时统计各发货类型商品的平均评分数及平均评分值，
用于评估不同发货方式在用户口碑与竞争力方面的表现。
该指标可辅助卖家选择合适的发货方式，并判断 Amazon 自营或特定发货类型带来的竞争压力。

## MCP 调用名称

`mcp__sellersprite__market_seller_type_concentration`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_seller_type_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-type-concentration`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | Amazon自营 |
| 2 | asinNum | Integer | ASIN数量 | 4 |
| 3 | asinRatio | Float | ASIN数量占比 | 0.03 |
| 4 | units | Integer | 月销量 | 79875 |
| 5 | unitsRatio | Float | 月销量占比 | 0.0345 |
| 6 | ratings | Integer | 评分数 | 6607 |
| 7 | rating | Float | 评分值 | 4.7 |
| 8 | productNum | Integer | 商品总数 | 3 |

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

