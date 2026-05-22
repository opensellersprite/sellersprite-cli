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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_listing_date_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/listing-date-distribution`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 3年以上 |
| 2 | shelfTime | String | 上架时间 | 3年以上 |
| 3 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 4 | products | Integer | 产品数 | B07Z82895W |
| 5 | revenue | Float | 销售额 | 40846.76 |
| 6 | units | Integer | 销量 | 4684 |
| 7 | unitsRatio | Float | 销量占比 | 0.834 |

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

