# market_price_distribution

## 描述

用于分析指定 Amazon 市场类目节点下的商品价格区间分布与市场定价结构。
在指定样本商品范围内，基于商品价格进行区间化分析，
系统性刻画各价格区间的商品数量分布、销量占比及对应的平均销量占比（该区间销量占比 / 该区间商品数量），
用于衡量不同价格层级在市场中的需求集中度、销售效率及竞争密度。
该指标能够反映买家对不同价格区间的真实接受程度，
并揭示价格区间与销量贡献之间的结构性关系。
结合各价格区间内商品的评分表现，可进一步识别具备差异化空间的定价带，
其中评分水平相对较低但销量仍具支撑的价格区间，
通常代表存在通过产品优化、定价策略调整或定位重塑实现切入的潜在机会。

## MCP 调用名称

`mcp__sellersprite__market_price_distribution`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_price_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/price-distribution`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].range | String | 价格区间 |
| distribution[].minPrice | Float | 最低价 |
| distribution[].maxPrice | Float | 最高价 |
| distribution[].count | Integer | 商品数 |
| distribution[].ratio | Float | 占比 |
| distribution[].avgUnits | Integer | 平均销量 |

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

