# market_rating_distribution

## 描述

用于分析指定 Amazon 市场类目节点下的商品评分值分布与市场成熟度评估。
在指定样本商品范围内，基于商品评分值进行区间划分，
系统性统计各评分值区间的商品数量分布、销量占比及评分数总量，
并计算各区间的平均销量占比（该区间销量占比 / 该区间商品数量），
用于衡量不同质量层级商品在市场中的销售效率与真实需求承载能力。
该指标能够刻画类目内商品被市场认可的整体结构，
通过评分值分布判断市场成熟度及产品质量集中程度：
高评分值商品占比较高通常意味着类目成熟、用户认知稳定；
低评分值商品占比较高则可能反映市场仍处于优化空间较大的阶段，
适合具备产品改进与供应链整合能力的卖家进行差异化切入与升级。

## MCP 调用名称

`mcp__sellersprite__market_rating_distribution`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_rating_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/rating-distribution`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].rating | Float | 评分值 |
| distribution[].count | Integer | 商品数 |
| distribution[].ratio | Float | 占比 |

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

