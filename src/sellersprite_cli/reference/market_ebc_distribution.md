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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_ebc_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ebc-distribution`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| hasEbc | Integer | 有 A+ 的商品数 |
| hasEbcRatio | Float | A+ 占比 |
| hasVideo | Integer | 有视频的商品数 |
| hasVideoRatio | Float | 视频占比 |
| hasAplusVideo | Integer | 有 A++ 的商品数 |
| hasAplusVideoRatio | Float | A++ 占比 |

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

