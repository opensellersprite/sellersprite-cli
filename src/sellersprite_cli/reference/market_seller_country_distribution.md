# market_seller_country_distribution

## 描述

用于分析指定 Amazon 市场类目节点下的卖家所属地分布情况。
在指定样本商品范围内，按照卖家所属国家或地区进行分组，
统计各地区卖家的商品数量及其销量/销售额占比。
常用于判断市场是否由本土卖家或中国卖家占据主导地位，
或呈现多国卖家均衡竞争格局，
从而辅助评估市场竞争激烈程度、卖家集中度及潜在市场风险。

## MCP 调用名称

`mcp__sellersprite__market_seller_country_distribution`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_seller_country_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-country-distribution`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 美国 |
| 2 | country | String | 国家 | 美国 |
| 3 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 4 | products | Integer | 产品数 | 3 |
| 5 | revenue | Float | 销售额 | 47492.83 |
| 6 | units | Integer | 销量 | 4107 |
| 7 | unitsRatio | Float | 销量占比 | 0.7313 |

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

