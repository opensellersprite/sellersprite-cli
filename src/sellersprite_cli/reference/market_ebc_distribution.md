# market_ebc_distribution

## 描述

用于分析指定 Amazon 市场类目节点下的A+视频分布
A+ 页面与商品视频内容对销量影响的内容配置效应评估。
在指定样本商品范围内，基于商品是否配置 A+ 页面及 Listing 主图下方的视频介绍进行组合分组，
系统性刻画四种内容配置状态下的商品数量结构及其对应的销量占比，
用于量化富内容展示在不同配置组合下对销量承载能力与转化效率的实际贡献。
该指标能够揭示 A+ 页面与视频内容在提升商品表现方面的边际效应及协同关系，
区分单一内容配置与组合配置对销量提升的差异影响，
从而辅助卖家判断内容投入的优先级与回报预期，
为 Listing 内容优化与资源投入决策提供结构化依据。

## MCP 调用名称

`mcp__sellersprite__market_ebc_distribution`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_ebc_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ebc-distribution`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 有A+有视频 |
| 2 | products | Integer | 产品数 | 1 |
| 3 | productsRatio | Float | 类目名称产品占比 | 20 |
| 4 | units | Integer | 销量 | 1311 |
| 5 | unitsRatio | Float | 销量占比 | 23.34 |

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

