# market_research_statistics

## 描述

Amazon 类目结构与机会分析工具（节点级）。

用于在“已明确类目节点”的前提下，系统分析该类目的：
- 市场规模与成熟度
- 头部 Listing 的竞争强度与垄断程度
- 新品在该类目中的生存与成长能力
- 平均价格、利润率、销量是否具备商业价值

与“全类目筛选工具”不同，
本工具更适合在【已选定类目】后，做深入可行性验证。

该工具重点回答的问题包括：
- 这个具体类目现在是否已经过于成熟？
- 头部 Listing 是否形成强垄断？
- 新品是否还能在该类目中跑出来？
- 新品与头部商品在价格、销量、评价上的差距有多大？

典型使用场景：
- 选品前，对目标类目做深度市场验证
- 判断是否值得进入某一个细分节点
- 分析“做头部款”还是“做新品切入”

## MCP 调用名称

`mcp__sellersprite__market_research_statistics`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_research_statistics`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/research/statistics`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalProducts | Integer | 总商品数 |
| totalUnits | Integer | 总销量 |
| totalRevenue | Float | 总销售额 |
| avgPrice | Float | 平均价格 |
| avgRating | Float | 平均评分 |
| avgUnits | Integer | 平均销量 |
| newProducts | Integer | 新品数 |
| topProducts[].{asin,title,units,revenue} | - | TOP 商品 |

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

