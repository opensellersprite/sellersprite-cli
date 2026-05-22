# traffic_extend

## 描述

用于在指定 Amazon 站点中，根据 ASIN、时间范围及多维筛选条件，
批量搜索并分析高价值关键词的工具。

该工具适用于：
- 关键词拓展与筛选
- 广告投放关键词决策（PPC）
- 市场需求与竞争强度评估
- 选品或Listing优化前的关键词调研

返回结果包含：搜索量、购买量、转化率、PPC竞价、供需比、
广告竞争度、点击集中度、关联ASIN等核心商业指标，
可直接用于“是否值得投放 / 是否值得进入”的判断。

## MCP 调用名称

`mcp__sellersprite__traffic_extend`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | historyDate | String |  | 历史日期，yyyyMM格式，最近30天不传或传空字符串，202201 |
| 3 | asinList | List | ✓ | asin列表(最多20)，["B07Z82895W"] |
| 4 | queryType | Integer |  | 查询方式 0 所有变体 1畅销变体 2当前变体，默认2，2 |
| 5 | minSearches | Integer |  | 最小月搜索量，100 |
| 6 | maxSearches | Integer |  | 最大月搜索量，300 |
| 7 | minSearchRank | Integer |  | 最小搜索排名，33 |
| 8 | maxSearchRank | Integer |  | 最大搜索排名，3223 |
| 9 | minPurchases | Integer |  | 最小购买量，6 |
| 10 | maxPurchases | Integer |  | 最大购买量，34 |
| 11 | minPurchaseRate | Float |  | 最小购买率，3 |
| 12 | maxPurchaseRate | Float |  | 最大购买率，43 |
| 13 | minProducts | Integer |  | 最小商品数，10 |
| 14 | maxProducts | Integer |  | 最大商品数，90 |
| 15 | minSupplyDemandRatio | Float |  | 最小供需比，11.2 |
| 16 | maxSupplyDemandRatio | Float |  | 最大供需比，45.2 |
| 17 | minBid | Float |  | 最小ppc竞价，10.2 |
| 18 | maxBid | Float |  | 最大ppc竞价，23.1 |
| 19 | minAdProducts | Integer |  | 最小广告竞品数，123 |
| 20 | maxAdProducts | Integer |  | 最大广告竞品数，345 |
| 21 | minAvgPrice | Float |  | 最小均价，20 |
| 22 | maxAvgPrice | Float |  | 最大均价，30.3 |
| 23 | minWordCount | Integer |  | 最小单词个数，2 |
| 24 | maxWordCount | Integer |  | 最大单词个数，4 |
| 25 | includeKeywords | List |  | 包含的词，["phone stand"] |
| 26 | excludeKeywords | List |  | 排除的词，["phone stand"] |
| 27 | minSPR | Integer |  | 最小SPR，2 |
| 28 | maxSPR | Integer |  | 最大SPR，16 |
| 29 | minTitleDensity | Integer |  | 最小标题密度，2 |
| 30 | maxTitleDensity | Integer |  | 最大标题密度，23 |
| 31 | minMonopolyClickRate | Float |  | 最小点击集中度，23.4 |
| 32 | maxMonopolyClickRate | Float |  | 最大点击集中度，53.1 |
| 33 | minTrafficPercentage | Float |  | 最小流量占比，45 |
| 34 | maxTrafficPercentage | Float |  | 最大流量占比，23 |
| 35 | minConversionRate | Float |  | 最小转化率，0.23 |
| 36 | maxConversionRate | Float |  | 最大转化率，1.4 |
| 37 | minCompetitors | Integer |  | 最小asin数，4 |
| 38 | maxCompetitors | Integer |  | 最大asin数，23 |
| 39 | amazonChoice | Boolean |  | 亚马逊推荐词，TRUE |
| 40 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 41 | size | Integer |  | 每页条数，最大50，默认：50 |
| 42 | order | Object |  | 排序 |
| 43 | └field | String |  | 排序字段，见表2.5 |
| 44 | └desc | boolean |  | true为降序 false为升序，默认降序 |

## 基本信息

- **MCP Code**: `traffic_extend`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/extend`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | keyword | String | 关键字 | N95 |
| 2 | keywordCn | String | 关键词中文翻译 | 用于录音的电话支架 |
| 3 | searches | Integer | 搜索量 | 21582 |
| 4 | purchases | Integer | 月购买量 | 1996 |
| 5 | purchaseRate | Float | 月购买率 | 0.0925 |
| 6 | products | Integer | 商品数 | 1645 |
| 7 | bidMin | Float | 最小PPC价格 | 1.34 |
| 8 | bidMax | Float | 最大PPC价格 | 3.21 |
| 9 | bid | Float | PPC价格 | 1.6 |
| 10 | badges | List | 流量词类型 | 见表1.10 |
| 11 | updatedTime | long | 更新时间 |  |
| 12 | searchesRank | Integer | 周搜索量排名 | 25 |
| 13 | searchesRankTimeFrom | Long | 周搜索量排名时间范围 |  |
| 14 | searchesRankTimeTo | Long | searchesRankTimeTo |  |
| 15 | latest1daysAds | Integer | 最近1天广告竞品数 | 70 |
| 16 | latest7daysAds | Integer | 最近7天广告竞品数 | 100 |
| 17 | latest30daysAds | Integer | 最近30天广告竞品数 | 280 |
| 18 | supplyDemandRatio | Float | 供需比 | 3.8 |
| 19 | trafficPercentage | Float | 流量占比 | 0.015 |
| 20 | calculatedWeeklySearches | Float | 预估周搜索量 | 40 |
| 21 | avgPrice | Float | 平均价格 | 36.14 |
| 22 | avgRatings | Integer | 平均评分数 | 12223 |
| 23 | avgRating | Float | 平均评分值 | 4.5 |
| 24 | titleDensity | Integer | 标题密度 | 42.9 |
| 25 | spr | Integer | SPR | 6 |
| 26 | monopolyClickRate | Float | 点击垄断率 | 0.3 |
| 27 | top3ClickingRate | Float | 前三点击 | 0.0813 |
| 28 | top3ConversionRate | Float | 前三转化 | 0.2011 |
| 29 | relationVariationsItems | List | 来自于哪些变体 |  |
| 30 | └marketplace | String | 站点 | 3 |
| 31 | └asin | String | asin | B08P6SC34B |
| 32 | └imageUrl | String | 图片链接 | 10 |
| 33 | └trafficPercentage | Float | 流量占比 | 54.6 |
| 34 | └title | String | 标题 |  |
| 35 | └price | Float | 价格 | 60 |
| 36 | └reviews | Float | 评论数 | 10 |
| 37 | └rating | Float | 评分 | 4.5 |
| 38 | └marketplace | String | 站点 | 3 |
| 39 | └asin | String | asin | B08P6SC34B |
| 40 | └imageUrl | String | 图片链接 | 10 |
| 41 | └trafficPercentage | Float | 流量占比 | 54.6 |
| 42 | └title | String | 标题 |  |
| 43 | └price | Float | 价格 | 60 |
| 44 | └reviews | Float | 评论数 | 10 |
| 45 | └rating | Float | 评分 | 4.5 |

## 请求示例

```json
{
  "request": {
    "amazonChoice": false,
    "asinList": [
      "B0XXX1",
      "B0XXX2"
    ],
    "excludeKeywords": [
      "keyword1"
    ],
    "historyDate": "202604",
    "includeKeywords": [
      "keyword1"
    ],
    "marketplace": "US",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "queryType": 2,
    "size": 20
  }
}
```

