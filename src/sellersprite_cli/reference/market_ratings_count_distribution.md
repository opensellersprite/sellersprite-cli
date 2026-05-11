# market_ratings_count_distribution

## 描述

用于分析指定 Amazon 市场类目节点下的商品评分数区间分布与新品进入难度。
在指定样本商品范围内，按照商品评分数进行区间划分（区间跨度可配置），
统计各评分数区间内的商品数量分布及其对应的销量占比，
并计算各区间的平均销量占比（该区间销量占比 / 该区间商品数量），
用于衡量不同评分数层级商品的整体销售效率。
该指标可用于分析类目内商品评分数的整体分布结构，
并从评分积累难度的角度判断新品进入门槛，
识别低评分数区间与高评分数区间在市场竞争中的相对优势。

## MCP 调用名称

`mcp__sellersprite__market_ratings_count_distribution`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_ratings_count_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ratings-count-distribution`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].range | String | 评分数区间 |
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

