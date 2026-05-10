# market_product_concentration

## 描述

用于分析指定 Amazon 市场类目节点下的商品集中度情况。

通过传入对应站点（国家编码）、类目节点路径及筛选条件，返回该类目中头部 Listing 的
排名、价格、品牌、卖家类型、上架时间、评分、评论数、销量、销售额
以及对应的销量占比与销额占比等核心指标。

头部商品的总销量T，占样本范围内商品总销量A的比例，即商品集中度=T/A
头部商品在整个市场中占比越大，说明头部商品垄断越明显，市场竞争度越大

可用于判断：
- 类目内销量与销售额是否高度集中
- 头部商品的市场主导程度
- 市场竞争强度与进入机会
- 新品在该类目下的潜在生存空间

## MCP 调用名称

`mcp__sellersprite__market_product_concentration`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `asins` | array |  | 过滤 ASIN |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_product_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/product-concentration`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalProducts | Integer | 总商品数 |
| top10Units | Float | TOP10 销量占比 |
| top20Units | Float | TOP20 销量占比 |
| top50Units | Float | TOP50 销量占比 |
| top100Units | Float | TOP100 销量占比 |
| concentrationLevel | String | 集中度等级 |

## 请求示例

```json
{
  "request": {
    "asins": [
      "B0XXX1",
      "B0XXX2"
    ],
    "marketplace": "US",
    "month": "202604",
    "newProduct": 6,
    "nodeIdPath": "2619525011:3741271",
    "topN": 10
  }
}
```

