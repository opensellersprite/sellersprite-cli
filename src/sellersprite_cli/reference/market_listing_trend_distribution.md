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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_listing_trend_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/listing-trend-distribution`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| trends[].month | String | 月份 |
| trends[].newListings | Integer | 新增 listing 数 |
| trends[].removedListings | Integer | 下架 listing 数 |
| trends[].netGrowth | Integer | 净增长 |

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

