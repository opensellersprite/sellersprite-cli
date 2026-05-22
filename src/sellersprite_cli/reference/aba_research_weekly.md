# aba_research_weekly

## 描述

用于在指定 Amazon 站点和时间点（按周），
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

`mcp__sellersprite__aba_research_weekly`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | date | String |  | 为空时，查最新周，20230610，限定为周六的日期） |
| 3 | departments | List |  | 类目列表，["automotive","baby-products"] |
| 4 | excludeKeywords | String |  | 排除关键词，portable |
| 5 | includeKeywords | String |  | 包含关键词 |
| 6 | exactFlag | Boolean |  | 是否精确匹配 |
| 7 | rankGrowthValue | Integer |  | 搜索增长量 |
| 8 | rankGrowthRate | Double |  | 搜索增长率 |
| 9 | minRankGrowthRate | Double |  | 最小排名增长率 |
| 10 | maxRankGrowthRate | Double |  | 最大排名增长率 |
| 11 | minSearchRank | Integer |  | 最小排名 |
| 12 | maxSearchRank | Integer |  | 最大排名 |
| 13 | minSearches | Integer |  | 最小搜索量 |
| 14 | maxSearches | Integer |  | 最大搜索量 |
| 15 | minMonopolyClickRate | Double |  | 最小点击集中度 |
| 16 | maxMonopolyClickRate | Double |  | 最大点击集中度 |
| 17 | minConversionRate | Double |  | 最小转化占比 |
| 18 | maxConversionRate | Double |  | 最大转化占比 |
| 19 | minWordCount | Integer |  | 最小单词数 |
| 20 | maxWordCount | Integer |  | 最大单词数 |
| 21 | minSPR | Integer |  | 最小SPR |
| 22 | maxSPR | Integer |  | 最大SPR |
| 23 | minTitleDensity | Integer |  | 最小标题密度 |
| 24 | maxTitleDensity | Integer |  | 最大标题密度 |
| 25 | minClicks | Integer |  | 最小点击量，1 |
| 26 | maxClicks | Integer |  | 最大点击量，10000 |
| 27 | minImpressions | Integer |  | 最小展示量，10000 |
| 28 | maxImpressions | Integer |  | 最大展示量，20000 |
| 29 | searchModel | Integer |  | 搜索模式：1：热门市场2：异动市场3：持续增长市场4：快速飙升市场5：潜力市场6：长尾市场，1 |
| 30 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 31 | size | Integer |  | 每页条数，最大40，默认：40 |
| 32 | order | Object |  | 排序 |
| 33 | └field | String |  | 排序字段，见表2.4 |
| 34 | └desc | boolean |  | true为降序 false为升序，默认降序 |

## 基本信息

- **MCP Code**: `aba_research_weekly`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/aba/research/weekly`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | date | String | 查询日期 | 20230610，限定为周六的日期 |
| 3 | keyword | String | 关键词 | portable charger |
| 4 | keywordCn | Integer | 关键词中文 | 便携式充电器 |
| 5 | keywordJp | String | 关键词日文 |  |
| 6 | departments | List | 类目 | ["Cell Phones & Accessories"] |
| 7 | searchRank | Integer | 搜索排名 | 62 |
| 8 | searchRankCv | Integer | 排名增长量 | 19 |
| 9 | searchRankCr | Double | 排名增长率 | 0.2346 |
| 10 | searches | Integer | 搜索量 | 46147979 |
| 11 | purchases | Integer | 购买量 | 2492 |
| 12 | purchaseRate | Double | 购买率 | 0.0054 |
| 13 | clicks | Integer | 点击量 | 1380 |
| 14 | impressions | BigInteger | 展示量 | 73560 |
| 15 | titleDensityExact | Integer | 首页商品标题中包含该关键词的商品数(精确匹配) |  |
| 16 | cprExact | Integer | 精确 CPR（8天内确保关键词上首页的销量数） |  |
| 17 | w1SearchRank | Integer | 上周的排名 |  |
| 18 | w1RankGrowthValue | Integer | 上周的排名变化值 |  |
| 19 | w1RankGrowthRate | Double | 上周的排名变化率 |  |
| 20 | w4SearchRank | Integer | 4周前的排名 |  |
| 21 | w4RankGrowthValue | Integer | 4周前的排名变化值 |  |
| 22 | w4RankGrowthRate | Double | 4周前的排名变化率 |  |
| 23 | w12SearchRank | Integer | 12周前的排名 |  |
| 24 | w12RankGrowthValue | Integer | 12周前的排名变化值 |  |
| 25 | w12RankGrowthRate | Double | 12周前的排名变化率 |  |
| 26 | top3Brands | List | 点击前三品牌 |  |
| 27 | bid | Float | ppc竞价 |  |
| 28 | bidMax | Float | 最大ppc竞价 |  |
| 29 | bidMin | Float | 最小ppc竞价 |  |
| 30 | top3AsinDtoList | List | 前三点击asin |  |
| 31 | └asin | String | asin |  |
| 32 | └imageUrl | String | 图片URL |  |
| 33 | └clickRate | Double | 点击集中度 |  |
| 34 | └conversionRate | Double | 转化率 |  |
| 35 | clickShareRate | Double | 前三点击比 | 54.2 |
| 36 | cvsShareRate | Double | 前三转化总比 | 43.5 |

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

