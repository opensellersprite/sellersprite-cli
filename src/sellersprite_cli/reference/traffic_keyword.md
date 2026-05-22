# traffic_keyword

## 描述

查询指定 ASIN 在 Amazon 指定市场下的搜索关键词表现数据，
支持近 30 天或指定历史月份，
返回 ASIN 实际获得曝光和流量的关键词列表，
包含搜索量、自然排名、广告排名、流量占比、转化表现及 PPC 竞价参考，
用于关键词挖掘、Listing 优化和广告投放分析。

## MCP 调用名称

`mcp__sellersprite__traffic_keyword`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asin | String | ✓ | B07Z82895W |
| 3 | keyword | String |  | 关键词，phone stand |
| 4 | month | String |  | 历史月份，不传默认最近30天，202308 |
| 5 | badges | List |  | 流量词类型，见表1.10 |
| 6 | trafficKeywordTypes | List |  | 流量占比类型，见表2.0 |
| 7 | conversionKeywordTypes | List |  | 流量转化类型，见表2.1 |
| 8 | page | Integer |  | 当前页，默认1 |
| 9 | size | Integer |  | 每页显示多少条，默认50，最大100，最多查询2000条数据 |
| 10 | order | Object |  | 排序 |
| 11 | └field | String |  | 排序字段，默认：rankPosition见表2.3 |
| 12 | └desc | Boolean |  | 是否倒序，false |

## 基本信息

- **MCP Code**: `traffic_keyword`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场编码 | 见表 1.2 |
| 2 | asin | String | asin | B07Z82895W |
| 3 | total | Integer | 总条数 | 2685 |
| 4 | items | List | 词条 | 1848 |
| 5 | └keyword | String | 关键词 | 该ASIN近30天或某个自然月进入过亚马逊搜索结果前3页的词 |
| 6 | └keywordCn | String | 关键词中文翻译 | 手机支架 |
| 7 | └searches | Integer | 月搜索量 | 指的是一个自然月的月搜索量，比如2025年8月，该关键词在亚马逊站内的搜索总次数 |
| 8 | └products | Integer | 商品数 | 指搜索该关键词后出现了多少个相关的产品 |
| 9 | └purchases | Integer | 月购买量 | 在亚马逊站内搜索该关键词后产生购买的次数，比如：某用户搜索iphone charger，然后1次购买了1个iphone充电器，2条数据线(关联推荐的商品)，则购买量=1 |
| 10 | └purchaseRate | Float | 购买率 | 指买家输入该搜索词并点击此细分市场中的任意商品后，买家的购买次数占买家输入该搜索词总次数的比例 |
| 11 | └bid | Float | PPC竞价 | 亚马逊站内广告Bid价格，系统提供【词组匹配】的Bid建议价格以及范围 |
| 12 | └bidMax | Float | PPC竞价范围 |  |
| 13 | └bidMin | Float | PPC竞价范围 |  |
| 14 | └badges | List | 曝光位置 | ASIN在对应关键词的搜索结果下曝光的具体位置， 见表1.10 |
| 15 | └rankPosition | RankPosition | 自然排名 |  |
| 16 | └└page | Integer | 第几页 | 3 |
| 17 | └└pageSize | Integer | 每页多少条数据 | 60 |
| 18 | └└index | Integer | 当前页排第几 | 10 |
| 19 | └└position | Integer | 总结果中排第几 | 106 |
| 20 | └└updatedTime | long | 排名时间 |  |
| 21 | └adPosition | AdPosition | 广告排名 |  |
| 22 | └└page | Integer | 第几页 | 2 |
| 23 | └└pageSize | Integer | 每页多少条数据 | 63 |
| 24 | └└index | Integer | 当前页排第几 | 37 |
| 25 | └└position | Integer | 总结果中排第几 | 85 |
| 26 | └└updatedTime | long | 排名时间 |  |
| 27 | └searchesRank | Integer | 周搜索量排名 | 数据来源于亚马逊ABA数据的关键词搜索频率排名（Search Frequency Rank），数字越小表示排名越靠前，搜索量越高 |
| 28 | └searchesRankTimeFrom | Long | 周搜索量排名时间范围 |  |
| 29 | └searchesRankTimeTo | Long | searchesRankTimeTo |  |
| 30 | └latest1daysAds | Integer | 最近1天广告竞品数 | 表示近1天内进入过该关键词搜索结果前3页的广告产品总数，包括SP广告、HR广告、品牌广告和视频广告 |
| 31 | └latest7daysAds | Integer | 最近7天广告竞品数 | 表示近7天内进入过该关键词搜索结果前3页的广告产品总数，包括SP广告、HR广告、品牌广告和视频广告 |
| 32 | └latest30daysAds | Integer | 最近30天广告竞品数 | 表示近30天内进入过该关键词搜索结果前3页的广告产品总数，包括SP广告、HR广告、品牌广告和视频广告 |
| 33 | └supplyDemandRatio | Float | 供需比 | 搜索量(需求) / 商品数(供应)，在同类市场中，需供比值越高，则代表该市场需求越强劲 |
| 34 | └trafficPercentage | Float | 流量占比 | 指的是产品通过不同流量词获得的曝光量占比 |
| 35 | └trafficKeywordType | String | 流量占比类型 | 见表2.0 |
| 36 | └conversionKeywordType | String | 转换效果类型 | 见表2.1 |
| 37 | └calculatedWeeklySearches | Float | 预估周曝光量 | 指的是该关键词本周内给产品带来的预估曝光量，非该词在亚马逊的总搜索量 |
| 38 | └impressions | Long | 展示量 | 指一个自然月，比如2024年3月，在某个关键词搜索结果页中所有ASIN的总展示次数，非单个ASIN在关键词下的曝光量 |
| 39 | └updatedTime | Long | 更新时间 |  |
| 40 | └clicks | Integer | 点击量 | 指一个自然月，比如2024年3月，在某个关键词搜索结果页中被点击的总次数，非单个ASIN在关键词下的点击量 |
| 41 | └naturalRatio | Float | 流量分布-自然占比 | 0.9312 |
| 42 | └adRatio | Float | 流量分布-广告占比 | 0.0688 |
| 43 | stats | List | 高频词 |  |
| 44 | └keywords | String | 词 | phone |
| 45 | └total | Integer | 总条数 | 90 |
| 46 | └└page | Integer | 第几页 | 3 |
| 47 | └└pageSize | Integer | 每页多少条数据 | 60 |
| 48 | └└index | Integer | 当前页排第几 | 10 |
| 49 | └└position | Integer | 总结果中排第几 | 106 |
| 50 | └└updatedTime | long | 排名时间 |  |
| 51 | └└page | Integer | 第几页 | 2 |
| 52 | └└pageSize | Integer | 每页多少条数据 | 63 |
| 53 | └└index | Integer | 当前页排第几 | 37 |
| 54 | └└position | Integer | 总结果中排第几 | 85 |
| 55 | └└updatedTime | long | 排名时间 |  |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/keyword' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","asin":"B07Z82895W","page":1,"size":1}'
```

