# market_listing_date_distribution

## 描述

用于分析指定 Amazon 市场类目节点下的商品上架时间分布与新品接受度。
在指定样本商品范围内，按照商品上架距今的时间区间进行分组，
统计各时间区间内的商品数量分布及其对应的销量占比，
并计算各区间的平均销量占比（该区间销量占比 / 该区间商品数量），
用于衡量不同上架周期商品的整体销售效率。
该指标可用于判断市场中新品与老品的销量贡献结构，
评估买家对新品的接受程度及新品打造难度，
并辅助卖家选择合适的产品生命周期切入策略。

## MCP 调用名称

`mcp__sellersprite__market_listing_date_distribution`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_listing_date_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/listing-date-distribution`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].range | String | 时间范围 |
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

