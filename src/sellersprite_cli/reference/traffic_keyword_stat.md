# traffic_keyword_stat

## 描述

Amazon ASIN 流量关键词结构【概览统计】工具。

用于快速分析某个 ASIN 当前整体的流量关键词规模，
以及这些流量主要来源于：
- 自然搜索
- Amazon 官方推荐体系
- 各类广告（SP / 品牌广告 / 视频广告 / HR）

与“流量词明细接口”不同，
本工具只返回【统计级数据】，不返回具体关键词列表，
适合作为 AI 决策的第一步判断入口。

核心用途：
- 判断 ASIN 是否高度依赖广告获取流量
- 评估自然流量与广告流量的结构比例
- 快速对比多个 ASIN 的流量健康度
- 作为是否深入分析（调用明细接口）的前置筛选条件

典型可回答的问题：
- 这个 ASIN 的流量主要靠自然搜索还是广告？
- 广告流量词是否明显高于自然流量词？
- Amazon 官方推荐体系（AC / ER / 4星）是否友好？
- 该 ASIN 是否存在“广告堆量型”的风险？

## MCP 调用名称

`mcp__sellersprite__traffic_keyword_stat`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `asin` | string | 是 | ASIN |
| `month` | string |  | 查询月份, 格式: yyyyMM，不传默认近30天 |

## 基本信息

- **MCP Code**: `traffic_keyword_stat`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword-stat`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| total | Integer | 总流量词数 |
| items[].keyword | String | 关键词 |
| items[].keywordCn | String | 中文翻译 |
| items[].searches | Integer | 月搜索量 |
| items[].products | Integer | 商品数 |
| items[].purchases | Integer | 月购买量 |
| items[].purchaseRate | Float | 购买率 |
| items[].trafficPercentage | Float | 流量占比 |
| items[].trafficKeywordType | String | 流量类型 |
| items[].conversionKeywordType | String | 转化类型 |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/keyword-stat' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asin":"B07Z82895W"}'
```

