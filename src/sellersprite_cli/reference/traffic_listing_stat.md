# traffic_listing_stat

## 描述

Amazon ASIN 流量来源结构分析工具（免费 / 付费 + 关联类型分布）。

本工具用于统计某个 ASIN 当前所获得的全部流量来源，
并从两个核心维度进行拆解：
1. 免费流量 vs 付费流量的整体占比
2. 不同流量“关联类型”（relation）的数量分布

这是一个【结构型统计接口】，不返回具体关键词或 ASIN 明细，
只用于判断“流量是如何被获取的”。

核心用途：
- 判断 ASIN 是否高度依赖广告或付费引流
- 分析免费流量（自然、关联、推荐）的贡献程度
- 快速识别 ASIN 的主要流量获取模式
- 辅助评估投放策略是否健康、是否具备自然增长能力

典型可回答的问题：
- 这个 ASIN 的流量主要来自免费还是付费？
- 广告投放是否是当前的主要流量来源？
- 不同关联流量类型各占多少？
- 是否存在“流量结构失衡”的风险？

## MCP 调用名称

`mcp__sellersprite__traffic_listing_stat`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asinList | List |  | asin列表，["B07Z82895W"] |

## 基本信息

- **MCP Code**: `traffic_listing_stat`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/traffic/listing-stat/{marketplace}/{asin}`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | asin | String | asin | B07Z82895W |
| 3 | relations | Integer | 全部流量 | 1848 |
| 4 | freeRelations | Integer | 免费流量 | 1414 |
| 5 | paidRelations | Integer | 付费流量 | 286 |
| 6 | calcTime | Long | 最近计算时间 |  |
| 7 | items | List | 统计概要 |  |
| 8 | └relation | String | 关联类型，见表2.2,忽略大小写 | vav |
| 9 | └count | Integer | 数量 | 3 |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

