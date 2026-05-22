# traffic_source

## 描述

Amazon 流量关键词结构分析工具（ASIN / 关键词维度）。

用于分析某个 ASIN 或关键词在指定月份内：
- 实际带来流量的关键词总量
- 不同来源（自然搜索 / 官方推荐 / 广告）的流量词分布
- 广告词、品牌词、推荐词在整体流量中的占比
- ASIN 当前的基础商品信息与类目背景

该工具的核心价值在于：
【理解一个 ASIN 或关键词"流量是从哪里来的"】【而不是只有搜索量】

典型可回答的问题包括：
- 这个 ASIN 主要吃的是自然流量，还是广告流量？
- 有多少流量词是 Amazon 官方体系推荐出来的？
- 广告词在整体流量中占比高不高？
- 这个 ASIN 是否已经形成稳定的自然搜索词池？
- 竞品是否严重依赖 SP / 视频广告获客？

适用场景：
- 竞品流量结构分析
- 判断 ASIN 是否"靠广告堆起来"
- 广告投放与自然 SEO 策略制定
- 流量词挖掘与优先级判断

## MCP 调用名称

`mcp__sellersprite__traffic_source`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | q | String | ✓ | asin 或者 关键词，B07Z82895W |
| 3 | month | String | ✓ | 筛选日期,yyyyMM格式，202203 |
| 4 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 5 | size | Integer |  | 每页条数，默认：50最大： 100 |
| 6 | order | Object |  | 排序 |
| 7 | └field | String |  | 排序字段，见表2.4 |
| 8 | └desc | boolean |  | true为降序 false为升序，默认降序 |

## 基本信息

- **MCP Code**: `traffic_source`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/source`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | keywords | Integer | 全部流量词 | 1 |
| 2 | searchKeywords | Integer | 自然搜索词 | 12 |
| 3 | acKeywords | String | AC推荐词 | 13 |
| 4 | editorialKeywords | Integer | ER推荐词 | 13 |
| 5 | fourStarsKeywords | Integer | 4星推荐词 | 14 |
| 6 | hrKeywords | Integer | HR推荐词 | 1 |
| 7 | adKeywords | Integer | SP广告词 | 3 |
| 8 | videoKeywords | Integer | 视频广告词 | 4 |
| 9 | brandKeywords | Integer | 品牌广告词 | 5 |
| 10 | badgeLabels | List | 流量来源概览 | [“SEARCH”, “OFFICIAL”, “AD”] |
| 11 | badgeDetails | Map | 流量来源明细 | {“SEARCH”: [“NATURAL_SEARCHING”],”OFFICIAL”: [“AMAZON_CHOICE”],”AD”: [“SPONSOR_BRAND”,”SPONSOR_VIDEO”,”HIGHLY_RATED”,”ADS”]} |
| 12 | asinInfo | Object | Asin相关信息 |  |
| 13 | └asin | String | asin | B078J8VPVW |
| 14 | └asinUrl | String | 该asin对应亚马逊地址 | https://www.amazon.com/dp/B08GHW4TBS |
| 15 | └currency | String | 货币code | $ |
| 16 | └price | Float | 价格 | 23 |
| 17 | └rating | Float | 评分 | 234 |
| 18 | └reviews | Integer | 评分数 | 23 |
| 19 | └title | String | 标题 | Diapers Size 2, 186 Count - Pampers Swaddlers Disposable Baby Diapers, ONE MONTH SUPPLY |
| 20 | └sku | String | sku | ["Color: Beige","Size: 47 inches"] |
| 21 | └variations | Integer | 变体数 | 2 |
| 22 | └nodeId | Long | 类目ID | 12097479011 |
| 23 | └nodeIdPath | String | 类目ID路径 | 172282:24046923011:172541:12097479011 |
| 24 | └nodeLabelPath | String | 类目路径 | Electronics:Headphones, Earbuds & Accessories:Headphones & Earbuds:Over-Ear Headphones |
| 25 | └bsrRank | Long | 大类排名(BSR) | 175204 |

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "month": "202604",
    "q": "B07Z82895W",
    "page": 1,
    "size": 50
  }
}
```

