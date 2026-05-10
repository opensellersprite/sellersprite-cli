# aba_research_monthly

## 描述

用于在指定 Amazon 站点和时间点（按月），
系统性发现【热门 / 异动 / 增长 / 潜力】关键词的分析工具。

该工具以“关键词趋势变化”为核心，
结合搜索排名变化、搜索量、点击、转化、PPC竞价、
以及头部ASIN与品牌集中度等指标，
帮助 AI 判断：

- 当前市场有哪些正在上升或爆发的关键词
- 哪些关键词存在流量红利或增长机会
- 哪些关键词已被头部品牌高度垄断
- 是否适合新进入、广告投放或加大预算

适用场景：
- 市场趋势监控
- 选品前的关键词机会发现
- 广告投放关键词挖掘（PPC）
- 判断“增长中关键词 vs 已饱和关键词”

## MCP 调用名称

`mcp__sellersprite__aba_research_monthly`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `date` | string |  | 查询月份, 格式: yyyyMM |
| `departments` | array |  | 类目列表 |
| `excludeKeywords` | string |  | 排除关键词 |
| `includeKeywords` | string |  | 包含关键词 |
| `keywordList` | array |  | 关键词列表 |
| `marketplace` | string | 是 | country code |
| `maxClicks` | integer |  | 最大点击量 |
| `maxConversionRate` | number |  | 最大转化占比 |
| `maxImpressions` | integer |  | 最大展示量 |
| `maxMonopolyClickRate` | number |  | 最大点击集中度 |
| `maxRankGrowthRate` | number |  | 最大排名增长率 |
| `maxSPR` | integer |  | 最大SPR |
| `maxSearchRank` | integer |  | 最大排名 |
| `maxSearches` | integer |  | 最大搜索量 |
| `maxTitleDensity` | integer |  | 最大标题密度 |
| `maxWordCount` | integer |  | 最大单词数 |
| `minClicks` | integer |  | 最小点击量 |
| `minConversionRate` | number |  | 最小转化占比 |
| `minImpressions` | integer |  | 最小展示量 |
| `minMonopolyClickRate` | number |  | 最小点击集中度 |
| `minRankGrowthRate` | number |  | 最小排名增长率 |
| `minSPR` | integer |  | 最小SPR |
| `minSearchRank` | integer |  | 最小排名 |
| `minSearches` | integer |  | 最小搜索量 |
| `minTitleDensity` | integer |  | 最小标题密度 |
| `minWordCount` | integer |  | 最小单词数 |
| `order` | object |  | 排序 |
| `page` | integer |  | 页码 |
| `searchModel` | integer |  | 查询方式, 默认: 2 可选值(必须严格使用下列数字值之一): 1: 热门市场 2: 异动市场 3: 持续增长市场 4: 快速飙升市场 5: 潜力市场 6: 长尾市场  禁止使用未列出的值。  |
| `size` | integer |  | 每页条数 |

## 基本信息

- **MCP Code**: `aba_research_monthly`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/aba/research/monthly`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 关键词 |
| searches | Integer | 月搜索量 |
| clicks | Integer | 月点击量 |
| ctr | Float | 点击率 |
| cvShareRate | Float | 转化共享率 |
| cvShareAsins | List | TOP3 转化 ASIN |
| asins | List | 相关 ASIN |

## 请求示例

```json
{
  "request": {
    "date": "20260425",
    "departments": [
      "wireless"
    ],
    "marketplace": "US",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "searchModel": 1,
    "size": 20
  }
}
```

