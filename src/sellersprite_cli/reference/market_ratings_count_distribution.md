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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_ratings_count_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ratings-count-distribution`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 500以上 |
| 2 | asins | List | 包含的asin列表 | 5 |
| 3 | products | Integer | 产品数 | ["B00P19MFYE"] |
| 4 | revenue | Float | 销售额 | 61714.24 |
| 5 | units | Integer | 销量 | 5616 |
| 6 | unitsRatio | Float | 销量占比 | 0.9743 |

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

