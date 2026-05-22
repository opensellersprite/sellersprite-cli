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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_rating_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/rating-distribution`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 4.5以上 |
| 2 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 3 | products | Integer | 产品数 | 5 |
| 4 | revenue | Float | 销售额 | 59934.22 |
| 5 | units | Integer | 销量 | 5418 |
| 6 | unitsRatio | Float | 销量占比 | 0.9647 |

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

