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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_seller_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-concentration`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalSellers | Integer | 总卖家数 |
| top1SellerUnits | Float | TOP1 卖家销量占比 |
| top5SellersUnits | Float | TOP5 卖家销量占比 |
| top10SellersUnits | Float | TOP10 卖家销量占比 |

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

