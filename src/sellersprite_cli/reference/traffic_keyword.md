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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `asin` | string | 是 | asin |
| `badges` | array |  | 流量词类型 可选值(仅填写字段名): - naturalSearching: 自然搜索词 - amazonChoice: AC推荐词 - editorialRecommendations: ER推荐词 - fourStar: 四星推荐词 - highlyRated: HR推荐词 - sponsorBrand: 品牌推荐词 - sponsorVideo: 视频推荐词 - ads: SP广告词  |
| `conversionKeywordTypes` | array |  | 流量转化类型 可选值(仅填写字段名): - excellent: 转化优质词 - stable: 转化平稳词 - lost:转化流失词 - invalid:无效曝光词  |
| `keyword` | string |  | 关键词 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `order` | object |  | 排序（见[表2.3 流量词列表排序字段](./api_appendix.md#流量词列表排序字段表23)） |
| `page` | integer |  | 页码 |
| `size` | integer |  | 每页条数 |
| `trafficKeywordTypes` | array |  | 流量占比类型 可选值(仅填写字段名): - primary: 主要流量词 - precise: 精准流量词 - preciseLongTail: 转化流失词  |

## 基本信息

- **MCP Code**: `traffic_keyword`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace/asin/total | - | 基本信息 |
| items[].keyword/keywordCn | String | 关键词及翻译 |
| items[].searches/products/purchases/purchaseRate | - | 搜索/商品数/购买相关 |
| items[].bid/bidMin/bidMax | Float | PPC竞价 |
| items[].badges | List | 曝光位置（naturalSearching/sponsorVideo等） |
| items[].rankPosition.{page,pageSize,index,position,updatedTime} | - | 自然排名 |
| items[].adPosition.{...同上} | - | 广告排名 |
| items[].searchesRank | Integer | 周搜索量排名（ABA） |
| items[].latest1/7/30daysAds | Integer | 近1/7/30天广告竞品数 |
| items[].supplyDemandRatio | Float | 供需比 |
| items[].trafficPercentage | Float | 流量占比 |
| items[].trafficKeywordType | String | 流量占比类型 |
| items[].conversionKeywordType | String | 转化效果类型 |
| items[].calculatedWeeklySearches | Float | 预估周曝光量 |
| items[].impressions/clicks | - | 月展示/点击量 |
| items[].naturalRatio/adRatio | Float | 自然/广告流量占比 |
| stats[].{keywords,total} | - | 高频词统计 |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/keyword' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","asin":"B07Z82895W","page":1,"size":1}'
```

