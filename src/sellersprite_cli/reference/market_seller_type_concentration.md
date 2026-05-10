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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_seller_type_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-type-concentration`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| fbaRatio | Float | FBA 占比 |
| fbmRatio | Float | FBM 占比 |
| amzRatio | Float | 亚马逊自营占比 |
| sellerTypeList[].type | String | 卖家类型 |
| sellerTypeList[].ratio | Float | 占比 |
| sellerTypeList[].count | Integer | 卖家数 |

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

