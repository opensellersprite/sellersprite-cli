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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_price_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/price-distribution`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 5-10 |
| 2 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 3 | products | Integer | 产品数 | 3 |
| 4 | revenue | Float | 销售额 | 33058.76 |
| 5 | units | Integer | 销量 | 4024 |
| 6 | unitsRatio | Float | 销量占比 | 0.7165 |

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

