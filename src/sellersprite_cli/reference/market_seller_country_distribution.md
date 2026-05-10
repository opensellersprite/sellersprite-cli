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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_seller_country_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-country-distribution`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| countries[].code | String | 国家代码 |
| countries[].label | String | 国家名称 |
| countries[].ratio | Float | 占比 |
| countries[].count | Integer | 卖家数 |

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

