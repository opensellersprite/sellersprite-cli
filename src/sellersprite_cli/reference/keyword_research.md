# keyword_research

## 描述

专业级 Amazon 关键词市场与选品分析工具。

本工具用于从真实卖家视角，综合评估某个关键词或关键词市场
是否具备进入价值、扩展潜力或投放价值。

工具基于以下核心维度进行分析：
- 市场需求：月搜索量、购买量、搜索增长趋势
- 市场竞争：商品数量、供需比、头部垄断程度
- 转化能力：购买率、点击集中度、共享转化率
- 成本结构：平均售价、PPC 竞价区间
- 成熟度判断：市场周期、新兴或成熟细分市场

适合在以下场景调用：
- 判断某个关键词是否值得进入或重点布局
- 筛选高需求 / 低竞争 / 高增长的潜力关键词
- 进行新品选品前的市场可行性验证
- 对比多个关键词，选择更优的投放或开发方向

返回结果应从「卖家决策角度」进行解读：
- 搜索量高 + 供需比高：代表需求强且竞争相对可控
- 搜索增长率为正：代表市场处于上升期
- 购买率高：代表关键词具备真实成交能力
- PPC 竞价低 + 售价合理：代表广告和利润空间友好
- 点击集中度低：代表头部卖家垄断程度较弱，更易切入

当需要基于数据做出选品、投放或市场进入决策时，
优先使用该工具获取客观量化依据。

## MCP 调用名称

`mcp__sellersprite__keyword_research`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | month | String |  | 筛选日期,yyyyMM格式，支持近24个月的，202203 |
| 3 | departments | List |  | 查询类目，见关键词选品类目接口，传递code，["automotive","baby-products"] |
| 4 | keywords | String |  | 关键词，N95 |
| 5 | excludeKeywords | String |  | 排除的关键字，portable |
| 6 | minSearches | Integer |  | 最小月搜索量，100 |
| 7 | maxSearches | Integer |  | 最大月搜索量，300 |
| 8 | minSearchesCr | Float |  | 最小月搜索量增长率，10 |
| 9 | maxSearchesCr | Float |  | 最大月搜索量增长率，50.8 |
| 10 | minProducts | Integer |  | 最小商品数，10 |
| 11 | maxProducts | Integer |  | 最大商品数，90 |
| 12 | minPurchases | Integer |  | 最小购买量，100 |
| 13 | maxPurchases | Integer |  | 最大购买量，500 |
| 14 | minPurchaseRate | Float |  | 最小购买率，3.2 |
| 15 | maxPurchaseRate | Float |  | 最大购买率，10.5 |
| 16 | withYearlyGrowth | Boolean |  | 新细分市场，false |
| 17 | minSearchMonthCv | Integer |  | 最小月搜索量同比增长值，1000 |
| 18 | maxSearchMonthCv | Integer |  | 最大月搜索量同比增长值，3000 |
| 19 | minSearchMonthCr | Float |  | 最小月搜索量同比增长率，5.3 |
| 20 | maxSearchMonthCr | Float |  | 最大月搜索量同比增长率，30.1 |
| 21 | minSearchNearlyCv | Integer |  | 最小月搜索量近3个月增长值，6000 |
| 22 | maxSearchNearlyCv | Integer |  | 最大月搜索量近3个月增长值，20000 |
| 23 | minSearchNearlyCr | Float |  | 最小月搜索量近3个月增长率，10.3 |
| 24 | maxSearchNearlyCr | Float |  | 最大月搜索量近3个月增长率，20.4 |
| 25 | marketPeriod | String |  | 市场周期，见表1.7 |
| 26 | minAvgPrice | Float |  | 最小均价，20 |
| 27 | maxAvgPrice | Float |  | 最大均价，30.3 |
| 28 | minRatings | Integer |  | 最小评分数，2000 |
| 29 | maxRatings | Integer |  | 最大评分数，3000 |
| 30 | minRating | Float |  | 最小评分值，3.2 |
| 31 | maxRating | Float |  | 最大评分值，4.1 |
| 32 | minBid | Float |  | 最小PPC竞价，6.2 |
| 33 | maxBid | Float |  | 最大PPC竞价，10.6 |
| 34 | minAraClickRate | Float |  | 最小点击集中度，20.1 |
| 35 | maxAraClickRate | Float |  | 最大点击集中度，56.4 |
| 36 | minGoodsValue | Float |  | 最小货流值，10.1 |
| 37 | maxGoodsValue | Float |  | 最大货流值，41.1 |
| 38 | minSupplyDemandRatio | Float |  | 最小供需比，5.6 |
| 39 | maxSupplyDemandRatio | Float |  | 最大供需比，10.4 |
| 40 | minWordCount | Integer |  | 最小单词个数，1 |
| 41 | maxWordCount | Integer |  | 最大单词个数，3 |
| 42 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 43 | size | Integer |  | 每页条数，默认15，最大：15 |
| 44 | order | Object |  | 排序 |
| 45 | └field | String |  | 排序字段，见表1.8 |
| 46 | └desc | boolean |  | true为降序 false为升序，默认降序 |

## 基本信息

- **MCP Code**: `keyword_research`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-research`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | keywords | String | 关键词 | polaroid cameras |
| 3 | searches | Integer | 搜索量 | 141356 |
| 4 | clicks | Integer | 点击量 | 在某个关键词搜索结果页中被点击的总次数非单个ASIN在关键词下的点击量 |
| 5 | impressions | Long | 展示量 | 在某个关键词搜索结果页中所有ASIN的总展示次数非单个ASIN在关键词下的曝光量 |
| 6 | purchases | Integer | 月购买量 | 4029 |
| 7 | growth | Float | 增长率 | -25.482092 |
| 8 | purchaseRate | Float | 月购买率 | 0.0285 |
| 9 | products | Integer | 产品数 | 173 |
| 10 | supplyDemandRatio | Float | 供需比 | 817.09 |
| 11 | searchDepartments | List | 类目 |  |
| 12 | └code | String | 类目代码 | electronics |
| 13 | └label | String | 类目名称 | Electronics |
| 14 | └total | Integer | 类目总计 | 141356 |
| 15 | └ratio | Float | 类目占比 | 1 |
| 16 | month | String | 查询月份 | 2022.01 |
| 17 | supplement | String | 是否属于补充关键词 | N |
| 18 | searchMonthlyCv | Integer | 关键词同比增长 | 139749 |
| 19 | searchMonthlyCr | Float | 关键词同比增长率 | 8696.27 |
| 20 | searchNearlyCv | Integer | 关键词近3个月增长值 | -48338 |
| 21 | searchNearlyCr | Float | 关键词近3个月增长率 | -25.48 |
| 22 | currency | String | 货币 | $ |
| 23 | avgPrice | Float | 平均价格 | 116.24 |
| 24 | avgRatings | Integer | 平均评分数 | 2584 |
| 25 | avgRating | Float | 平均评论数 | 4.5 |
| 26 | relationAsinList | List | 关键词关联asin | 4.8 |
| 27 | └price | Float | 价格 | 59.95 |
| 28 | └ratings | Integer | 评分数 | 20115 |
| 29 | └rating | Float | 评分 | 4.7 |
| 30 | bidMin | Float | bid最小价格 | 0.987 |
| 31 | bidMax | Float | bid最大价格 | 2.54 |
| 32 | bid | Float | bid价格 | 1.26 |
| 33 | araClickRate | Float | 点击垄断率 | 0.2633 |
| 34 | araShareRate | Float | 共享转化率 | 0.2633 |
| 35 | araAsinList | List | 点击前三ASIN |  |
| 36 | └asin | String | asin | B099VDRGG1 |
| 37 | └title | String | title | Fujifilm Instax Mini 9 |
| 38 | └imageUrl | String | 图片 | https://m.media-amazon.com/images/I/51aZiZaicYL._AC_US200_.jpg |
| 39 | └clickRate | Double | 点击率 | 0.116 |
| 40 | └conversionShareRate | Double | 转化率 | 0.1217 |
| 41 | goodsValue | Float | 货流值 | 0.0108 |
| 42 | brands | List | TOP3 品牌 | ["LEGO","Jorumo","Nifeliz"] |
| 43 | categories | List | TOP3 类目 | ["Toys","Home","Mobile_Apps"] |
| 44 | titleDensityExact | String | 标题密度首页商品包含该关键词的数量（不含广告位） | 21 |
| 45 | marketPeriod | String | 市场周期 | S11,S12 |
| 46 | brand | String | 品牌 | Fujifilm |
| 47 | hasBrandWord | Boolean | 是否存在品牌词 | false |
| 48 | keywordCn | String | 中文翻译 | 宝丽来相机 |

## 请求示例

```json
{
  "request": {
    "departments": [
      "wireless"
    ],
    "keywords": "wireless earbuds",
    "marketplace": "US",
    "month": "202604",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "size": 20
  }
}
```

