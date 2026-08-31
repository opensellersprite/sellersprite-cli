# keyword_conversion

## 描述

关键字转化率分析工具，围绕单个关键词及其相关词组，
给出从搜索到点击、再到购买的完整转化漏斗数据。

该工具回答以下关键问题：
- 一个关键词的搜索量、点击量、购买量分别是多少？
- 搜索转化率、点击转化率处于什么水平？
- 各匹配方式（词组 / 精准 / 广泛）的 PPC 竞价、CPA、ACOS、广告预算大概是多少？
- 该关键词下表现最好的商品（Top3 / Top10 ASIN）有哪些？

适用于：
- 广告投放前的关键词转化能力评估
- PPC 竞价与预算规划
- 关键词选词 / 否词
- 竞品词的转化漏斗拆解

## MCP 调用名称

`mcp__sellersprite__keyword_conversion`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点，见表 1.2 |
| 2 | keyword | String | ✓ | 关键词 |
| 3 | timeType | String |  | 时间类型，WEEK: 按周；90D：近90天 |
| 4 | minSearches | Integer |  | 最小搜索量 |
| 5 | maxSearches | Integer |  | 最大搜索量 |
| 6 | minClicks | Integer |  | 最小点击量 |
| 7 | maxClicks | Integer |  | 最大点击量 |
| 8 | minPurchases | Integer |  | 最小购买量 |
| 9 | maxPurchases | Integer |  | 最大购买量 |
| 10 | minSearchConvRate | Float |  | 最小搜索转化率 |
| 11 | maxSearchConvRate | Float |  | 最大搜索转化率 |
| 12 | minClickConvRate | Float |  | 最小点击转化率 |
| 13 | maxClickConvRate | Float |  | 最大点击转化率 |
| 14 | minPpc | Float |  | 最小PPC竞价 |
| 15 | maxPpc | Float |  | 最大PPC竞价 |
| 16 | minCpa | Float |  | 最小CPA |
| 17 | maxCpa | Float |  | 最大CPA |
| 18 | minProductPrice | Float |  | 最小产品均价 |
| 19 | maxProductPrice | Float |  | 最大产品均价 |
| 20 | minAcos | Float |  | 最小ACOS |
| 21 | maxAcos | Float |  | 最大ACOS |
| 22 | minClickingRate | Float |  | 最小前三点击率 |
| 23 | maxClickingRate | Float |  | 最大前三点击率 |
| 24 | minConversionRate | Float |  | 最小前三转化率 |
| 25 | maxConversionRate | Float |  | 最大前三转化率 |
| 26 | minPhraseCount | Integer |  | 最小词组数 |
| 27 | maxPhraseCount | Integer |  | 最大词组数 |
| 28 | minBudget | Float |  | 最小广告预算 |
| 29 | maxBudget | Float |  | 最大广告预算 |
| 30 | matchType | Integer |  | 包含词匹配方式 |
| 31 | includeKeywords | List |  | 包含词 |
| 32 | excludeKeywords | List |  | 排除词 |
| 33 | customAvgProductPrice | Double |  | 自定义均价 |

## 基本信息

- **MCP Code**: `keyword_conversion`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword/conversion`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | keyword | String | 关键词 |  |
| 2 | keywordCn | String | 中文关键词 |  |
| 3 | keywordJp | String | 日文关键词 |  |
| 4 | searches | Integer | 搜索量 |  |
| 5 | clicks | Integer | 点击量 |  |
| 6 | purchases | Integer | 购买量 |  |
| 7 | searchConvRate | Double | 搜索转化率 |  |
| 8 | clickConvRate | Double | 点击转化率 |  |
| 9 | searchesTrend | String | 搜索量趋势 |  |
| 10 | clickTrend | String | 点击量趋势 |  |
| 11 | purchaseTrend | String | 购买量趋势 |  |
| 12 | clickingRate | Double | 前三点击率 |  |
| 13 | conversionRate | Double | 前三转化率 |  |
| 14 | phraseCount | int | 词组数量 |  |
| 15 | phrasePpc | ValueItem | 词组PPC竞价 |  |
| 16 | └min | Double | 最小 |  |
| 17 | └max | Double | 最大 |  |
| 18 | └value | Double | 中位数 |  |
| 19 | exactPpc | ValueItem | 精确PPC竞价 |  |
| 20 | └min | Double | 最小 |  |
| 21 | └max | Double | 最大 |  |
| 22 | └value | Double | 中位数 |  |
| 23 | broadPpc | ValueItem | 广泛PPC竞价 |  |
| 24 | └min | Double | 最小 |  |
| 25 | └max | Double | 最大 |  |
| 26 | └value | Double | 中位数 |  |
| 27 | phraseCpa | ValueItem | 词组CPA |  |
| 28 | └min | Double | 最小 |  |
| 29 | └max | Double | 最大 |  |
| 30 | └value | Double | 中位数 |  |
| 31 | exactCpa | ValueItem | 精确CPA |  |
| 32 | └min | Double | 最小 |  |
| 33 | └max | Double | 最大 |  |
| 34 | └value | Double | 中位数 |  |
| 35 | broadCpa | ValueItem | 广泛CPA |  |
| 36 | └min | Double | 最小 |  |
| 37 | └max | Double | 最大 |  |
| 38 | └value | Double | 中位数 |  |
| 39 | phraseBudget | ValueItem | 词组广告预算 |  |
| 40 | └min | Double | 最小 |  |
| 41 | └max | Double | 最大 |  |
| 42 | └value | Double | 中位数 |  |
| 43 | exactBudget | ValueItem | 精确广告预算 |  |
| 44 | └min | Double | 最小 |  |
| 45 | └max | Double | 最大 |  |
| 46 | └value | Double | 中位数 |  |
| 47 | broadBudget | ValueItem | 广泛广告预算 |  |
| 48 | └min | Double | 最小 |  |
| 49 | └max | Double | 最大 |  |
| 50 | └value | Double | 中位数 |  |
| 51 | phraseAcos | ValueItem | 词组ACOS |  |
| 52 | └min | Double | 最小 |  |
| 53 | └max | Double | 最大 |  |
| 54 | └value | Double | 中位数 |  |
| 55 | exactAcos | ValueItem | 精确ACOS |  |
| 56 | └min | Double | 最小 |  |
| 57 | └max | Double | 最大 |  |
| 58 | └value | Double | 中位数 |  |
| 59 | broadAcos | ValueItem | 广泛ACOS |  |
| 60 | └min | Double | 最小 |  |
| 61 | └max | Double | 最大 |  |
| 62 | └value | Double | 中位数 |  |
| 63 | avgProductPrice | ValueItem | 产品均价 |  |
| 64 | └min | Double | 最小 |  |
| 65 | └max | Double | 最大 |  |
| 66 | └value | Double | 中位数 |  |
| 67 | top3Asins | List | 前三ASIN列表 |  |
| 68 | top10Asins | List | 前10ASIN列表 |  |

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "keyword": "lunch box",
    "timeType": "WEEK",
    "page": 1,
    "size": 2
  }
}
```

