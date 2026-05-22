# market_listing_trend_distribution

## 描述

用于分析指定 Amazon 市场类目节点下的商品上架时间分布与生命周期。
在指定样本商品范围内，按照商品的绝对上架时间进行区间划分，
统计各时间区间内的商品上架数量及其对应的销量占比，
并计算各区间的平均销量占比（该区间销量占比 / 该区间商品数量），
用于衡量不同上架时期产品的整体销售效率。
同时提供各时间区间商品的平均评分值，
用于评估不同产品生命周期阶段的用户认可度。
该指标可辅助分析产品生命周期特征，判断市场成熟度与长期畅销能力，
并识别新品期、成长期及长尾产品在市场中的相对竞争优势。

## MCP 调用名称

`mcp__sellersprite__market_listing_trend_distribution`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String |  | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String |  | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_listing_trend_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/listing-trend-distribution`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 2014 |
| 2 | year | String | 年份，yyyy格式 | 2014 |
| 3 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 4 | products | Integer | 产品数 | 1 |
| 5 | revenue | Float | 销售额 | 2515 |
| 6 | units | Integer | 销量 | 18837.35 |
| 7 | unitsRatio | Float | 销量占比 | 0.4478 |

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

