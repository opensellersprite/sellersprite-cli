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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `departments` | array |  | 查询类目，见关键词选品类目接口，传递code |
| `excludeKeywords` | string |  | 排除的关键字 |
| `keywords` | string |  | 关键词 |
| `marketPeriod` | string |  | 市场周期 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `maxAraClickRate` | number |  | 最大点击集中度 |
| `maxAvgPrice` | number |  | 最大均价 |
| `maxBid` | number |  | 最大PPC竞价 |
| `maxGoodsValue` | number |  | 最大货流值 |
| `maxProducts` | integer |  | 最大商品数 |
| `maxPurchaseRate` | number |  | 最大购买率 |
| `maxPurchases` | integer |  | 最大购买量 |
| `maxRating` | number |  | 最大评分值 |
| `maxRatings` | integer |  | 最大评分数 |
| `maxSearchMonthCr` | number |  | 最大月搜索量同比增长率 |
| `maxSearchMonthCv` | integer |  | 最大月搜索量同比增长值 |
| `maxSearchNearlyCr` | number |  | 最大月搜索量近3个月增长率 |
| `maxSearchNearlyCv` | integer |  | 最大月搜索量近3个月增长值 |
| `maxSearches` | integer |  | 最大月搜索量 |
| `maxSearchesCr` | number |  | 最大月搜索量增长率 |
| `maxSupplyDemandRatio` | number |  | 最大供需比 |
| `maxWordCount` | integer |  | 最大单词个数 |
| `minAraClickRate` | number |  | 最小点击集中度 |
| `minAvgPrice` | number |  | 最小均价 |
| `minBid` | number |  | 最小PPC竞价 |
| `minGoodsValue` | number |  | 最小货流值 |
| `minProducts` | integer |  | 最小商品数 |
| `minPurchaseRate` | number |  | 最小购买率 |
| `minPurchases` | integer |  | 最小购买量 |
| `minRating` | number |  | 最小评分值 |
| `minRatings` | integer |  | 最小评分数 |
| `minSearchMonthCr` | number |  | 最小月搜索量同比增长率 |
| `minSearchMonthCv` | integer |  | 最小月搜索量同比增长值 |
| `minSearchNearlyCr` | number |  | 最小月搜索量近3个月增长率 |
| `minSearchNearlyCv` | integer |  | 最小月搜索量近3个月增长值 |
| `minSearches` | integer |  | 最小月搜索量 |
| `minSearchesCr` | number |  | 最小月搜索量增长率 |
| `minSupplyDemandRatio` | number |  | 最小供需比 |
| `minWordCount` | integer |  | 最小单词个数 |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `order` | object |  | 排序 |
| `page` | integer |  | 页码 |
| `size` | integer |  | 每页条数 |
| `withYearlyGrowth` | boolean |  | 新细分市场 |

## 基本信息

- **MCP Code**: `keyword_research`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-research`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace/keywords/keywordCn | - | 市场/关键词/中文 |
| searches/clicks/impressions/purchases | - | 搜索/点击/展示/购买 |
| growth/purchaseRate/products/supplyDemandRatio | - | 增长率/购买率/产品数/供需比 |
| searchDepartments[].{code,label,total,ratio} | - | 类目分布 |
| month/supplement/marketPeriod | - | 月份/补充/市场周期 |
| searchMonthlyCv/Cr | - | 同比增长值/率 |
| searchNearlyCv/Cr | - | 近3月增长值/率 |
| currency | String | 货币 |
| avgPrice/avgRatings/avgRating | - | 平均价格/评分数/值 |
| relationAsinList[].{price,ratings,rating} | - | 关联ASIN |
| bid/bidMin/bidMax | Float | 竞价 |
| araClickRate/araShareRate | Float | 点击垄断率/共享转化率 |
| araAsinList[].{asin,title,imageUrl,clickRate,conversionShareRate} | - | 点击前三ASIN |
| goodsValue | Float | 货流值 |
| brands/categories | List | TOP3 品牌/类目 |
| titleDensityExact | String | 标题密度 |
| brand/hasBrandWord | - | 品牌/是否品牌词 |

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

