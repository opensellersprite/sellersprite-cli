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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asin | String | ✓ | B07Z82895W |
| 3 | month | String |  | 查询月份，202605 |

## 基本信息

- **MCP Code**: `traffic_keyword_stat`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword-stat`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | asin | String | asin | B07Z82895W |
| 3 | keywords | Integer | 全部流量词条数 | 2685 |
| 4 | ranks | Integer | 自然流量词条数 | 1848 |
| 5 | ads | Integer | 广告流量词条数 | 1414 |
| 6 | calcTime | Long | 最近计算时间 |  |
| 7 | badgeCount | Object | 流量词类型统计 |  |
| 8 | └ns | Integer | 自然搜索词数量 | 1070 |
| 9 | └ac | Integer | AC推荐词数量 | 0 |
| 10 | └er | Integer | ER推荐词数量 | 42 |
| 11 | └fs | Integer | 4星推荐词数量 | 0 |
| 12 | └hr | Integer | HR广告词数量 | 117 |
| 13 | └sb | Integer | 品牌广告词数量 | 334 |
| 14 | └sv | Integer | 视频广告词数量 | 208 |
| 15 | └ad | Integer | SP广告词数量 | 764 |
| 16 | └ns | Integer | 自然搜索词数量 | 1070 |
| 17 | └ac | Integer | AC推荐词数量 | 0 |
| 18 | └er | Integer | ER推荐词数量 | 42 |
| 19 | └fs | Integer | 4星推荐词数量 | 0 |
| 20 | └hr | Integer | HR广告词数量 | 117 |
| 21 | └sb | Integer | 品牌广告词数量 | 334 |
| 22 | └sv | Integer | 视频广告词数量 | 208 |
| 23 | └ad | Integer | SP广告词数量 | 764 |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/keyword-stat' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asin":"B07Z82895W"}'
```

