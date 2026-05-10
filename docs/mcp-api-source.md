# SellerSprite MCP API 文档

> 卖家精灵开放平台 38 个 MCP 接口完整文档。来源：[https://open.sellersprite.com/api](https://open.sellersprite.com/api)

## 通用说明

- **认证**：所有请求需在 Header 中携带 `secret-key`，密钥在 [open.sellersprite.com](https://open.sellersprite.com) 控制台获取
- **Base URL**: `https://api.sellersprite.com`
- **市场代码**：`US` / `JP` / `UK` / `DE` / `FR` / `IT` / `ES` / `CA` / `IN`
- **请求/响应格式**：`Content-Type: application/json`

---

## 目录

### ASIN 分析 (5)
- [3. ASIN 详情](#3-asin-详情) (`asin_detail`)
- [27. ASIN 销量预测](#27-asin-销量预测) (`asin_prediction`)
- [56. ASIN优惠趋势](#56-asin优惠趋势) (`asin_coupon_trend`)
- [57. ASIN详情及优惠趋势](#57-asin详情及优惠趋势) (`asin_detail_with_coupon_trend`)
- [22. 商品趋势详情(keepa)](#22-商品趋势详情keepa) (`keepa_info`)

### 商品与竞品 (3)
- [1. 查竞品](#1-查竞品) (`competitor_lookup`)
- [2. 选产品](#2-选产品) (`product_research`)
- [9. 查产品类目](#9-查产品类目) (`product_node`)

### 关键词 (5)
- [6. 关键词挖掘](#6-关键词挖掘) (`keyword_miner`)
- [10. 关键词选品](#10-关键词选品) (`keyword_research`)
- [11. 关键词选品-趋势数据](#11-关键词选品-趋势数据) (`keyword_research_trends`)
- [24. 出单词反查](#24-出单词反查) (`keyword_order`)
- [26. BSR销量预测](#26-bsr销量预测) (`bsr_prediction`)

### 流量 (6)
- [14. 关键词反查(流量词列表)](#14-关键词反查流量词列表) (`traffic_keyword`)
- [13. 流量词统计](#13-流量词统计) (`traffic_keyword_stat`)
- [17. 查流量来源(关键词流向)](#17-查流量来源关键词流向) (`traffic_source`)
- [15. 关联流量统计](#15-关联流量统计) (`traffic_listing_stat`)
- [16. 关联流量列表](#16-关联流量列表) (`traffic_listing`)
- [46. 拓展流量词](#46-拓展流量词) (`traffic_extend`)

### 市场分析 (14)
- [29. 选市场列表](#29-选市场列表) (`market_research`)
- [30. 选市场-统计](#30-选市场-统计) (`market_research_statistics`)
- [41. 选市场-价格分布](#41-选市场-价格分布) (`market_price_distribution`)
- [32. 选市场-品牌集中度](#32-选市场-品牌集中度) (`market_brand_concentration`)
- [31. 选市场-商品集中度](#31-选市场-商品集中度) (`market_product_concentration`)
- [33. 选市场-卖家集中度](#33-选市场-卖家集中度) (`market_seller_concentration`)
- [40. 选市场-评分值分布](#40-选市场-评分值分布) (`market_rating_distribution`)
- [39. 选市场-评分数分布](#39-选市场-评分数分布) (`market_ratings_count_distribution`)
- [37. 选市场-上架时间分布](#37-选市场-上架时间分布) (`market_listing_date_distribution`)
- [38. 选市场-上架趋势分布](#38-选市场-上架趋势分布) (`market_listing_trend_distribution`)
- [35. 选市场-卖家所属地分布](#35-选市场-卖家所属地分布) (`market_seller_country_distribution`)
- [34. 选市场-卖家类型分布](#34-选市场-卖家类型分布) (`market_seller_type_concentration`)
- [42. 选市场-A+视频分布](#42-选市场-a视频分布) (`market_ebc_distribution`)
- [36. 选市场-商品需求趋势](#36-选市场-商品需求趋势) (`market_product_demand_trend`)

### ABA / 趋势 (5)
- [19. ABA 数据选品-按周](#19-aba-数据选品-按周) (`aba_research_weekly`)
- [20. ABA 数据选品-按月](#20-aba-数据选品-按月) (`aba_research_monthly`)
- [60. ABA 数据选品-关键词趋势](#60-aba-数据选品-关键词趋势) (`aba_research_trend`)
- [12. 谷歌趋势](#12-谷歌趋势) (`google_trend`)
- [25. 查评论](#25-查评论) (`review`)

---

## 1. 查竞品

### 基本信息
- **MCP Code**: `competitor_lookup`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/product/competitor-lookup`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场编码 |
| 2 | month | String | | 查询月份，格式：yyyyMM |
| 3 | brand | String | | 品牌（如 WWDOLL） |
| 4 | sellerName | String | | 卖家（如 Apple） |
| 5 | asins | List | | asin 的 list 字符串，最多支持40个ASIN |
| 6 | nodeIdPath | String | | 类目节点字符串 |
| 7 | nodeIdPathEqual | boolean | | true: 类目精确查询, false: 当前及子类目；默认 false |
| 8 | keyword | String | | 关键字 |
| 9 | matchType | Integer | | 1：词组匹配，2：模糊匹配，3：精准匹配；默认 2 |
| 10 | variation | String | | N: 含变体, Y: 不含变体 |
| 11 | page | Integer | | 页码，默认 1 |
| 12 | size | Integer | | 每页条数，默认 50，最大 100 |
| 13 | order.field | String | | 排序字段，默认 total_units |
| 14 | order.desc | boolean | | true=desc, false=asc；默认 true |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | asin |
| brand | String | 品牌 |
| brandUrl | String | 品牌 URL |
| imageUrl | String | 图片 URL |
| title | String | 商品标题 |
| parent | String | 父体 |
| nodeId/nodeIdPath/nodeLabelPath | - | 节点信息 |
| bsr/bsrCr/bsrCv | - | BSR 排名/增长率/增长数 |
| units/unitsGr | - | 月销量(父体)/增长率 |
| amzUnit/amzSales/amzUnitDate | - | 子体近30日销量/销售额/更新日期 |
| revenue | Float | 月销售额(父体) |
| price/primePrice/profit/fba | - | 价格/Prime价/利润率/FBA运费 |
| ratings/ratingsRate/rating/ratingsCv/ratingDelta | - | 评分相关 |
| lqs | Float | listing 质量得分 |
| availableDate | Long | 上架时间 |
| fulfillment | String | 配送方式：AMZ / FBA / FBM |
| variations/sellers | - | 变体数/卖家数 |
| sellerId/sellerName/sellerNation | - | BuyBox 卖家信息 |
| badge.{bestSeller,amazonChoice,newRelease,ebc,video} | String | 各类标识 (Y/N) |
| weight/dimension/dimensionsType | - | 重量/尺寸 |
| pkgWeight/pkgDimensions/pkgDimensionType | - | 包装信息 |
| sku | String | sku |
| subcategories[].{code,rank,label} | - | 子类目信息 |
| deliveryPrice | Float | 卖家运费，-1表示没有 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/product/competitor-lookup' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","brand":"apple","variation":"N","page":1,"size":1}'
```

---

## 2. 选产品

### 基本信息
- **MCP Code**: `product_research`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/product/research`

### 请求参数（核心）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场编码 |
| month | String | | 查询月份 yyyyMM |
| keyword | String | | 关键字 |
| includeSellers/excludeSellers | String | | 包含/排除卖家 |
| matchType | Integer | | 1词组 2模糊 3精准；默认2 |
| excludeKeywords | String | | 排除关键字 |
| minPrice/maxPrice | Float | | 价格区间 |
| minRating/maxRating | Float | | 评分值区间 |
| minRatings/maxRatings | Integer | | 评分数区间 |
| minRatingsCv/maxRatingsCv | Integer | | 月新增评分数区间 |
| minSellers/maxSellers | Integer | | 卖家数量区间 |
| minProfit/maxProfit | Float | | 毛利率区间 |
| minBsr/maxBsr | Integer | | 大类BSR排名区间 |
| minBsrCv/maxBsrCv | Integer | | BSR增长数区间 |
| minBsrCr/maxBsrCr | Float | | BSR增长率区间 |
| minUnits/maxUnits | Integer | | 月销量区间 |
| minAmzUnit/maxAmzUnit | Integer | | 月子体销量区间 |
| minRevenue/maxRevenue | Float | | 月销售额区间 |
| minRevenueCr/maxRevenueCr | Float | | 销售额增长率区间 |
| minUnitsCr/maxUnitsCr | Float | | 销量增长率区间 |
| weightUnit | String | | 重量单位，默认g |
| minWeights/maxWeights | Float | | 重量区间 |
| minVariations/maxVariations | Integer | | 变体数区间 |
| filterSub | String | | Y=筛选子类目（需指定类目） |
| minSubBsrRank/maxSubBsrRank | Integer | | 子类排名区间 |
| includeBrands/excludeBrands | String | | 包含/排除品牌 |
| nodeIdPaths | List | | 类目节点字符串列表 |
| nodeIdPathEqual | boolean | | 默认false |
| availableMonth | Integer | | 上架月份 |
| dimensionType | String | | 尺寸类型集合 |
| minFba/maxFba | Float | | FBA运费区间 |
| minLqs/maxLqs | Float | | Listing质量分区间 |
| sellerNation | String | | 卖家所属地，逗号分隔 |
| badgeBS/badgeAC/badgeNR | String | | Best Seller/Amazon's Choice/New Release 标识 (Y) |
| fulfillment | String | | AMZ/FBA/FBM |
| variation | String | | N=含变体, Y=不含变体 |
| page | Integer | | 默认1，总条数限制2000 |
| size | Integer | | 默认50，最大100 |
| order.field | String | | 默认 total_units |
| order.desc | boolean | | 默认 true |

### 响应参数
返回字段与 `competitor_lookup` 一致（见上）。

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/product/research' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","minPrice":100,"maxPrice":101,"variation":"N","page":1,"size":1}'
```

---

## 3. ASIN 详情

### 基本信息
- **MCP Code**: `asin_detail`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}`

### 请求参数（路径）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN，例：B08GHW4TBS |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin/asinUrl | String | ASIN 及其链接 |
| availableDate | Long | 上架日期（时间戳） |
| brand/brandUrl | String | 品牌信息 |
| bsrId/bsrLabel/bsrRank | - | BSR 信息 |
| createdTime/updatedTime | Long | 创建/更新时间 |
| dimensions/weight | String | 尺寸/重量 |
| firstRatingDate | Long | 第一次评论时间 |
| imageUrl/zoomImageUrl | String | 图片链接 |
| lqs | Integer | Listing 质量得分 |
| nodeId/nodeIdPath/nodeLabelPath/nodeLabelPathLocale | - | 类目节点信息 |
| parent | String | 父 asin |
| price/primePrice/deliveryPrice | Float | 价格信息 |
| coupon | String | 优惠卷 |
| questions | Integer | 问题数量 |
| rating/ratings/reviews | - | 评分相关 |
| variantRatings/variantReviews | Integer | 子体评分/评论数 |
| sellerId/sellerName/sellers/fulfillment | - | 卖家信息 |
| skuList | List | SKU 列表 |
| marketplace/title | String | 市场/标题 |
| features | List | 五点描述 |
| overviews | String | 详情 JSON |
| variationList[].{asin,attribute} | - | 变体列表 |
| variations | Integer | 变体数量 |
| badge.{bestSeller,amazonChoice,newRelease,ebc,video} | String | 标识 (Y/N) |
| subcategories[].{rank,code,label} | - | 子类目信息 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/asin/US/B0DRVKZHK9' \
  -H 'secret-key: Your Secret'
```

---

## 6. 关键词挖掘

### 基本信息
- **MCP Code**: `keyword_miner`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword/miner`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| historyDate | String | | yyyyMM格式，最近30天不传或传空 |
| keyword | String | ✓ | 关键词 |
| keywordList | List | | 批量查询关键词 |
| minSearch/maxSearch | Integer | | 搜索量区间 |
| minPurchases/maxPurchases | Integer | | 购买量区间 |
| minPurchasesRate/maxPurchasesRate | Float | | 购买率区间 |
| minSPR/maxSPR | Integer | | SPR 区间 |
| minTitleDensity/maxTitleDensity | Integer | | 标题密度区间 |
| minRelevancy/maxRelevancy | Float | | 相关度区间 (0-100) |
| minSearchRank/maxSearchRank | Integer | | 搜索排名区间 |
| minProducts/maxProducts | Integer | | 商品数区间 |
| minSupplyDemandRatio/maxSupplyDemandRatio | Float | | 供需比区间 |
| minAdProducts/maxAdProducts | Integer | | 广告竞品数区间 |
| minWordCount/maxWordCount | Integer | | 单词个数区间 |
| minMonopolyClickRate/maxMonopolyClickRate | Float | | 点击集中度区间 |
| minBid/maxBid | Float | | PPC竞价区间 |
| minPrice/maxPrice | Float | | 均价区间 |
| minRatings/maxRatings | Integer | | 评分数区间 |
| minRating/maxRating | Float | | 评分值区间 |
| amazonChoice | Boolean | | 亚马逊推荐词 |
| filterRootWord | Integer | | 0=包含所有 1=只包含词根 |
| matchType | Integer | | 2=广泛匹配, 3=词组匹配 |
| includeKeywords/excludeKeywords | List | | 包含/排除词 |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100 |
| order.field | String | | 排序字段 |
| order.desc | boolean | | 默认 true |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| keyword/keywordCn/keywordJp | String | 关键词及其翻译 |
| departments[].{code,label} | - | 类目 |
| month | String | 搜索月份 |
| supplement | String | 是否补充关键词 |
| searches/purchases/purchaseRate | - | 搜索/购买相关 |
| monopolyClickRate | Float | 点击垄断率 |
| products/adProducts | Integer | 商品数/广告竞品数 |
| supplyDemandRatio | Float | 供需比 |
| avgPrice/avgRatings/avgRating | - | 平均价格/评分数/评分值 |
| bidMin/bidMax/bid | Float | PPC价格 |
| cvsShareRate | Float | 转化共享率 |
| wordCount | Integer | 单词个数 |
| titleDensity | Integer | 标题密度 |
| spr | Integer | SPR |
| relevancy | Double | 相关度 |
| amazonChoice | Boolean | 亚马逊推荐词 |
| searchRank | Integer | 搜索排名 |
| clicks/impressions | - | 点击量/展示量 |

---

## 9. 查产品类目

### 基本信息
- **MCP Code**: `product_node`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/product/node`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | | 类目节点 id 字符串，例：2619525011:3741271:3741281 |
| keyword | String | | 搜索关键字（nodeId或类目名称） |
| month | String | | 查询历史月份，yyyyMM |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目 id 字符串 |
| nodeLabelPath | String | 类目英文名称（冒号分隔） |
| nodeLabelLocale | String | 类目节点中文名 |
| nodeLabelPathLocale | String | 类目所属节点中文名 |
| products | Integer | 类目下产品数 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/product/node?marketplace=US&month=202507&nodeIdPath=2619525011:3741271' \
  -H 'secret-key: Your Secret'
```

---

## 56. ASIN优惠趋势

### 基本信息
- **MCP Code**: `asin_coupon_trend`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/coupon-trend`

### 请求参数（路径）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| asin | String | ASIN |
| date | String | 日期 |
| type | String | 优惠类型：M=减免金额, P=百分比折扣 |
| asinPrice | Float | ASIN 价格 |
| couponPrice | Float | 优惠金额 |
| finalPrice | Float | 实际价格 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/asin/US/B0DXTMS9NF/coupon-trend' \
  -H 'secret-key: Your Secret'
```

---

## 57. ASIN详情及优惠趋势

### 基本信息
- **MCP Code**: `asin_detail_with_coupon_trend`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/with-coupon-trend`

### 请求参数（路径）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |

### 响应参数

返回 `asin` 对象（结构同 [ASIN 详情](#3-asin-详情)） + `couponTrends` 数组（结构同 [ASIN优惠趋势](#56-asin优惠趋势)）。

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/asin/US/B0DXTMS9NF/with-coupon-trend' \
  -H 'secret-key: Your Secret'
```

---

## 27. ASIN 销量预测

### 基本信息
- **MCP Code**: `asin_prediction`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/asin`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场代码 |
| asin | String | ✓ | ASIN |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asinDetail.{asin,title,brand,availableDate,category,categoryId,imageUrl,ratings,rating} | - | ASIN 明细 |
| dailyItemList[].{date,bsr,sales,amount,price} | - | 日销量预测 |
| monthItemList[].{date,sales,amount,price} | - | 月销量预测 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/sales/prediction/asin?marketplace=US&asin=B0DBY873G7' \
  -H 'secret-key: Your Secret'
```

---

## 26. BSR销量预测

### 基本信息
- **MCP Code**: `bsr_prediction`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/bsr`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| bsr | Integer | ✓ | 大类排名 |
| categoryId | String | ✓ | 一级类目节点ID |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| bsr | Integer | BSR 排名 |
| categoryLabel | String | 类目名称 |
| estDailySales | Integer | 预测日销量 |
| estMonthSales | Integer | 预测30天销量 |
| itemList[].{bsr,estDailySales,estMonthSales} | - | 类目内排名靠前的BSR销量明细 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/sales/prediction/bsr?marketplace=US&categoryId=11260432011&bsr=2' \
  -H 'secret-key: Your Secret'
```

---

## 14. 关键词反查(流量词列表)

### 基本信息
- **MCP Code**: `traffic_keyword`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |
| keyword | String | | 关键词 |
| month | String | | 历史月份 yyyyMM，不传默认最近30天 |
| badges | List | | 流量词类型 |
| trafficKeywordTypes | List | | 流量占比类型 |
| conversionKeywordTypes | List | | 流量转化类型 |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100，最多查2000条 |
| order.field | String | | 默认 rankPosition |
| order.desc | Boolean | | 默认 false |

### 响应参数

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

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/keyword' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","asin":"B07Z82895W","page":1,"size":1}'
```

---

## 22. 商品趋势详情(keepa)

### 基本信息
- **MCP Code**: `keepa_info`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/keepa/{marketplace}/{asin}`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |
| startTimestamp | Long | | 趋势起始时间戳 |
| endTimestamp | Long | | 趋势结束时间戳 |
| dailyLatest | Boolean | | 是否仅获取每日最新数据 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace/asin/dataAsin/parentAsin/variationAsins | - | 基本ASIN信息 |
| rootCategory/rootCategoryLabel | - | BSR大类信息 |
| salesRankReference/salesRankReferenceHistory | - | 排名节点变动历史 |
| nodeIdPath/nodeLabelPath | - | 上架类目全路径 |
| productStatus | String | STANDARD/DOWNLOADABLE/EBOOK等 |
| availabilityAmazon | String | 亚马逊跟卖状态 |
| title/brand/asinUrl/brandUrl | - | 标题品牌链接 |
| imageUrl/zoomImageUrl/imageUrls | - | 商品图片 |
| dimensions/weight/weightGram | - | 净尺寸/重量 |
| pkgDimensions/pkgDimensionsSize/pkgWeight/pkgWeightGram | - | 打包尺寸/重量 |
| fbaFees/fbaItems | - | FBA费用 |
| numberOfPages/numberOfItems | - | 页数/商品数 |
| price[].{timePoint,value} | - | 价格趋势 |
| dealPrice/buyBox/priceList | - | 各种价格趋势 |
| buyBoxSellerIdHistory | List | 黄金购物车卖家历史 |
| bsr[].{timePoint,value} | - | BSR排名趋势 (-1表示无效) |
| subSalesRank[].{nodeId,node,ranks} | - | 小类排名趋势 |
| reviews/rating/sellers | List | 评分数/值/卖家数趋势 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/keepa/US/B0DYL2DHVV' \
  -H 'secret-key: Your Secret'
```

> **趋势数据格式**：`{timePoint(毫秒时间戳), value}` 键值对；`-1` 表示该时间点无有效数据；空列表表示无趋势数据。

---

## 10. 关键词选品

### 基本信息
- **MCP Code**: `keyword_research`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-research`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| month | String | | 筛选日期 yyyyMM(近24个月) |
| departments | List | | 查询类目（传 code） |
| keywords | String | | 关键词 |
| excludeKeywords | String | | 排除关键字 |
| min/maxSearches | Integer | | 月搜索量范围 |
| min/maxSearchesCr | Float | | 月搜索量增长率 |
| min/maxProducts | Integer | | 商品数范围 |
| min/maxPurchases | Integer | | 购买量范围 |
| min/maxPurchaseRate | Float | | 购买率范围 |
| withYearlyGrowth | Boolean | | 新细分市场 |
| min/maxSearchMonthCv | Integer | | 月搜索量同比增长值 |
| min/maxSearchMonthCr | Float | | 月搜索量同比增长率 |
| min/maxSearchNearlyCv | Integer | | 近3月增长值 |
| min/maxSearchNearlyCr | Float | | 近3月增长率 |
| marketPeriod | String | | 市场周期 |
| min/maxAvgPrice | Float | | 均价范围 |
| min/maxRatings | Integer | | 评分数范围 |
| min/maxRating | Float | | 评分值范围 |
| min/maxBid | Float | | PPC竞价范围 |
| min/maxAraClickRate | Float | | 点击集中度 |
| min/maxGoodsValue | Float | | 货流值 |
| min/maxSupplyDemandRatio | Float | | 供需比 |
| min/maxWordCount | Integer | | 单词个数 |
| page | Integer | | 默认1 |
| size | Integer | | 最大15 |
| order.field/order.desc | - | | 排序 |

### 响应参数

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

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword-research' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","keywords":"child","page":1,"size":1}'
```

---

## 11. 关键词选品-趋势数据

### 基本信息
- **MCP Code**: `keyword_research_trends`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-research/trends`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| keyword | String | ✓ | 关键词 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| time | String | 时间（按月，从2017年01月起） |
| keywrod | String | 关键词（注意原始拼写有误） |
| keywrodCn/keywrodJp | String | 中文/日文翻译 |
| search | Integer | 搜索量 |
| purchase | BigDecimal | 购买量 |
| purchaseRate | BigDecimal | 购买率 |
| yearlyGrowth | BigDecimal | 同比增长率 |
| chainGrowth | BigDecimal | 环比增长率 |
| threeMonthGrowth | BigDecimal | 三个月增长率 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword-research/trends' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keyword":"test"}'
```

---

## 13. 流量词统计

### 基本信息
- **MCP Code**: `traffic_keyword_stat`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword-stat`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |
| month | String | | 历史月份 yyyyMM |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| total | Integer | 总流量词数 |
| items[].keyword | String | 关键词 |
| items[].keywordCn | String | 中文翻译 |
| items[].searches | Integer | 月搜索量 |
| items[].products | Integer | 商品数 |
| items[].purchases | Integer | 月购买量 |
| items[].purchaseRate | Float | 购买率 |
| items[].trafficPercentage | Float | 流量占比 |
| items[].trafficKeywordType | String | 流量类型 |
| items[].conversionKeywordType | String | 转化类型 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/keyword-stat' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asin":"B07Z82895W"}'
```

---

## 15. 关联流量统计

### 基本信息
- **MCP Code**: `traffic_listing_stat`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/traffic/listing-stat/{marketplace}/{asin}`

### 请求参数（路径）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| marketplace | String | 市场 |
| totalTraffic | Integer | 总流量 |
| organicTraffic | Integer | 自然流量 |
| sponsoredTraffic | Integer | 广告流量 |
| searchTraffic | Integer | 搜索流量 |
| recommendTraffic | Integer | 推荐流量 |
| displayTraffic | Integer | 展示广告流量 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/traffic/listing-stat/US/B07Z82895W' \
  -H 'secret-key: Your Secret'
```

---

## 16. 关联流量列表

### 基本信息
- **MCP Code**: `traffic_listing`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/traffic/listing`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asinList | List | ✓ | ASIN 列表 |
| relations | List | | 关联类型 |
| trafficSourceTypes | List | | 流量来源类型 |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| relations[].{asin,title,imageUrl,brand} | - | 关联 ASIN 信息 |
| relations[].trafficSourceType | String | 流量来源 |
| relations[].trafficCount | Integer | 流量数 |
| relations[].conversionCount | Integer | 转化数 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/listing' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asinList":["B07Z82895W"],"relations":["also_viewed"],"page":1,"size":1}'
```

---

## 17. 查流量来源(关键词流向)

### 基本信息
- **MCP Code**: `traffic_source`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/traffic/source`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |
| month | String | | 历史月份 yyyyMM |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| trafficSources[].type | String | 流量来源类型 |
| trafficSources[].percentage | Float | 占比 |
| trafficSources[].count | Integer | 流量数 |
| trafficSources[].keywords | List | 关键词列表 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/source' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asin":"B07Z82895W"}'
```

---

## 19. ABA 数据选品-按周

### 基本信息
- **MCP Code**: `aba_research_weekly`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/aba/research/weekly`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| keywordList | List | | 关键词列表 |
| departments | List | | 类目 code |
| includeKeywords | String | | 包含关键词 |
| excludeKeywords | String | | 排除关键词 |
| minSearchRank/maxSearchRank | Integer | | 搜索排名区间 |
| minSearches/maxSearches | Integer | | 搜索量区间 |
| minClicks/maxClicks | Integer | | 点击量区间 |
| minCtr/maxCtr | Float | | 点击率区间 |
| minCvShareRate/maxCvShareRate | Float | | 转化共享率区间 |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100 |
| order.field/order.desc | - | | 排序 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 关键词 |
| searches | Integer | 周搜索量 |
| clicks | Integer | 周点击量 |
| ctr | Float | 点击率 |
| cvShareRate | Float | 转化共享率 |
| cvShareAsins | List | TOP3 转化 ASIN |
| asins | List | 相关 ASIN |
| rank | Integer | 排名 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/aba/research/weekly' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","page":1,"size":1}'
```

---

## 20. ABA 数据选品-按月

### 基本信息
- **MCP Code**: `aba_research_monthly`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/aba/research/monthly`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| keywordList | List | | 关键词列表 |
| departments | List | | 类目 code |
| includeKeywords | String | | 包含关键词 |
| excludeKeywords | String | | 排除关键词 |
| minSearches/maxSearches | Integer | | 月搜索量区间 |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100 |
| order.field/order.desc | - | | 排序 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 关键词 |
| searches | Integer | 月搜索量 |
| clicks | Integer | 月点击量 |
| ctr | Float | 点击率 |
| cvShareRate | Float | 转化共享率 |
| cvShareAsins | List | TOP3 转化 ASIN |
| asins | List | 相关 ASIN |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/aba/research/monthly' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","page":1,"size":1}'
```

---

## 24. 出单词反查

### 基本信息
- **MCP Code**: `keyword_order`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/keyword/order`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asins | List | ✓ | ASIN 列表（最多40个） |
| matchType | Integer | | 1=词组 2=模糊 3=精准；默认2 |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| keyword | String | 出单关键词 |
| keywordCn | String | 中文翻译 |
| searchRank | Integer | 搜索排名 |
| orderCount | Integer | 出单数 |
| orderRate | Float | 出单率 |
| page | Integer | 页码 |
| size | Integer | 每页条数 |
| total | Integer | 总条数 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword/order' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asins":["B07Z82895W"],"page":1,"size":1}'
```

---

## 25. 查评论

### 基本信息
- **MCP Code**: `review`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/review/{marketplace}/{asin}`

### 请求参数（路径）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asin | String | ✓ | ASIN |
| categoryId | String | | 类目节点 |
| star | Integer | | 星级筛选 |
| hasImage | Boolean | | 仅含图片评论 |
| hasVideo | Boolean | | 仅含视频评论 |
| hasComment | Boolean | | 仅含文字评论 |
| page | Integer | | 默认1 |
| size | Integer | | 默认20，最大50 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| asin | String | ASIN |
| totalReviews | Integer | 总评论数 |
| positiveRate | Float | 好评率 |
| neutralRate | Float | 中评率 |
| negativeRate | Float | 差评率 |
| reviews[].id | String | 评论ID |
| reviews[].rating | Integer | 星级 |
| reviews[].title | String | 评论标题 |
| reviews[].content | String | 评论内容 |
| reviews[].author | String | 评论者 |
| reviews[].date | String | 评论日期 |
| reviews[].helpful | Integer | 有帮助数 |
| reviews[].verified | Boolean | 是否已验证购买 |
| reviews[].images | List | 评论图片 |
| reviews[].videos | List | 评论视频 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/review/US/B07Z82895W?size=1' \
  -H 'secret-key: Your Secret'
```

---

## 29. 选市场列表

### 基本信息
- **MCP Code**: `market_research`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/research`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | | 类目节点 |
| nodeIdPathEqual | Boolean | | true=精确 false=含子类目 |
| minPrice/maxPrice | Float | | 价格区间 |
| minRatings/maxRatings | Integer | | 评分数区间 |
| minRating/maxRating | Float | | 评分值区间 |
| minUnits/maxUnits | Integer | | 销量区间 |
| minSellers/maxSellers | Integer | | 卖家数区间 |
| minRevenue/maxRevenue | Float | | 销售额区间 |
| minNewProductRatio/maxNewProductRatio | Float | | 新品占比区间 |
| minBrandConcentration/maxBrandConcentration | Float | | 品牌集中度区间 |
| fulfillment | String | | AMZ/FBA/FBM |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100 |
| order.field/order.desc | - | | 排序 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| nodeLabelPath | String | 类目标签 |
| totalProducts | Integer | 商品总数 |
| avgPrice | Float | 平均价格 |
| avgRating | Float | 平均评分 |
| avgRatings | Float | 平均评分数 |
| avgUnits | Integer | 平均销量 |
| avgRevenue | Float | 平均销售额 |
| newProductRatio | Float | 新品占比 |
| brandConcentration | Float | 品牌集中度 |
| topBrands | List | 头部品牌 |
| topSellers | List | 头部卖家 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/research' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011","page":1,"size":1}'
```

---

## 30. 选市场-统计

### 基本信息
- **MCP Code**: `market_research_statistics`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/research/statistics`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |
| month | String | | 查询月份 yyyyMM |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalProducts | Integer | 总商品数 |
| totalUnits | Integer | 总销量 |
| totalRevenue | Float | 总销售额 |
| avgPrice | Float | 平均价格 |
| avgRating | Float | 平均评分 |
| avgUnits | Integer | 平均销量 |
| newProducts | Integer | 新品数 |
| topProducts[].{asin,title,units,revenue} | - | TOP 商品 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/research/statistics' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 31. 选市场-商品集中度

### 基本信息
- **MCP Code**: `market_product_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/product-concentration`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalProducts | Integer | 总商品数 |
| top10Units | Float | TOP10 销量占比 |
| top20Units | Float | TOP20 销量占比 |
| top50Units | Float | TOP50 销量占比 |
| top100Units | Float | TOP100 销量占比 |
| concentrationLevel | String | 集中度等级 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/product-concentration' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 32. 选市场-品牌集中度

### 基本信息
- **MCP Code**: `market_brand_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/brand-concentration`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalBrands | Integer | 总品牌数 |
| top1BrandUnits | Float | TOP1 品牌销量占比 |
| top3BrandsUnits | Float | TOP3 品牌销量占比 |
| top10BrandsUnits | Float | TOP10 品牌销量占比 |
| hhi | Float | 赫芬达尔指数 |
| concentrationLevel | String | 集中度等级 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/brand-concentration' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 33. 选市场-卖家集中度

### 基本信息
- **MCP Code**: `market_seller_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-concentration`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalSellers | Integer | 总卖家数 |
| top1SellerUnits | Float | TOP1 卖家销量占比 |
| top5SellersUnits | Float | TOP5 卖家销量占比 |
| top10SellersUnits | Float | TOP10 卖家销量占比 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/seller-concentration' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 34. 选市场-卖家类型分布

### 基本信息
- **MCP Code**: `market_seller_type_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-type-concentration`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| fbaRatio | Float | FBA 占比 |
| fbmRatio | Float | FBM 占比 |
| amzRatio | Float | 亚马逊自营占比 |
| sellerTypeList[].type | String | 卖家类型 |
| sellerTypeList[].ratio | Float | 占比 |
| sellerTypeList[].count | Integer | 卖家数 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/seller-type-concentration' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 35. 选市场-卖家所属地分布

### 基本信息
- **MCP Code**: `market_seller_country_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller-country-distribution`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| countries[].code | String | 国家代码 |
| countries[].label | String | 国家名称 |
| countries[].ratio | Float | 占比 |
| countries[].count | Integer | 卖家数 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/seller-country-distribution' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 36. 选市场-商品需求趋势

### 基本信息
- **MCP Code**: `market_product_demand_trend`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/product-demand-trend`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |
| month | String | | 起始月份 yyyyMM |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| trends[].month | String | 月份 |
| trends[].units | Integer | 销量 |
| trends[].revenue | Float | 销售额 |
| trends[].products | Integer | 商品数 |
| trends[].avgPrice | Float | 平均价格 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/product-demand-trend' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 37. 选市场-上架时间分布

### 基本信息
- **MCP Code**: `market_listing_date_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/listing-date-distribution`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].range | String | 时间范围 |
| distribution[].count | Integer | 商品数 |
| distribution[].ratio | Float | 占比 |
| distribution[].avgUnits | Integer | 平均销量 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/listing-date-distribution' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 38. 选市场-上架趋势分布

### 基本信息
- **MCP Code**: `market_listing_trend_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/listing-trend-distribution`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |
| month | String | | 查询月份 yyyyMM |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| trends[].month | String | 月份 |
| trends[].newListings | Integer | 新增 listing 数 |
| trends[].removedListings | Integer | 下架 listing 数 |
| trends[].netGrowth | Integer | 净增长 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/listing-trend-distribution' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 39. 选市场-评分数分布

### 基本信息
- **MCP Code**: `market_ratings_count_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ratings-count-distribution`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].range | String | 评分数区间 |
| distribution[].count | Integer | 商品数 |
| distribution[].ratio | Float | 占比 |
| distribution[].avgUnits | Integer | 平均销量 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/ratings-count-distribution' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 40. 选市场-评分值分布

### 基本信息
- **MCP Code**: `market_rating_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/rating-distribution`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].rating | Float | 评分值 |
| distribution[].count | Integer | 商品数 |
| distribution[].ratio | Float | 占比 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/rating-distribution' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 41. 选市场-价格分布

### 基本信息
- **MCP Code**: `market_price_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/price-distribution`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| distribution[].range | String | 价格区间 |
| distribution[].minPrice | Float | 最低价 |
| distribution[].maxPrice | Float | 最高价 |
| distribution[].count | Integer | 商品数 |
| distribution[].ratio | Float | 占比 |
| distribution[].avgUnits | Integer | 平均销量 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/price-distribution' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 42. 选市场-A+视频分布

### 基本信息
- **MCP Code**: `market_ebc_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ebc-distribution`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| nodeIdPath | String | ✓ | 类目节点 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| hasEbc | Integer | 有 A+ 的商品数 |
| hasEbcRatio | Float | A+ 占比 |
| hasVideo | Integer | 有视频的商品数 |
| hasVideoRatio | Float | 视频占比 |
| hasAplusVideo | Integer | 有 A++ 的商品数 |
| hasAplusVideoRatio | Float | A++ 占比 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/market/ebc-distribution' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","nodeIdPath":"2619525011"}'
```

---

## 46. 拓展流量词

### 基本信息
- **MCP Code**: `traffic_extend`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/traffic/extend`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| asinList | List | ✓ | ASIN 列表 |
| matchType | Integer | | 匹配类型：1=模糊 2=宽泛 3=精准 |
| minSearches | Integer | | 最小搜索量 |
| includeKeywords | String | | 包含关键词 |
| excludeKeywords | String | | 排除关键词 |
| page | Integer | | 默认1 |
| size | Integer | | 默认50，最大100 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 拓展关键词 |
| keywordCn | String | 中文翻译 |
| searches | Integer | 搜索量 |
| products | Integer | 商品数 |
| purchaseRate | Float | 购买率 |
| avgPrice | Float | 平均价格 |
| sourceAsins | List | 来源 ASIN |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/extend' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asinList":["B07Z82895W"],"page":1,"size":1}'
```

---

## 60. ABA 数据选品-关键词趋势

### 基本信息
- **MCP Code**: `aba_research_trend`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/aba/research/trend`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| keyword | String | ✓ | 关键词 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 关键词 |
| time | String | 时间 |
| searches | Integer | 搜索量 |
| clicks | Integer | 点击量 |
| ctr | Float | 点击率 |
| cvShareRate | Float | 转化共享率 |
| rank | Integer | 排名 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/aba/research/trend' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keyword":"wireless earbuds"}'
```

---

## 12. 谷歌趋势

### 基本信息
- **MCP Code**: `google_trend`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/google/trend`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| marketplace | String | ✓ | 市场 |
| keywords | List | | 关键词列表 |
| startDate | String | | 开始日期 yyyy-MM-dd |
| endDate | String | | 结束日期 yyyy-MM-dd |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 关键词 |
| timeline[].date | String | 日期 |
| timeline[].value | Integer | 搜索指数 |
| timeline[].category | Integer | 类别 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/google/trend' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keywords":["earbuds"],"startDate":"2024-01-01","endDate":"2024-12-31"}'
```

---

## 错误码

| 错误码 | 说明 |
|--------|------|
| 400 | 请求参数错误 |
| 401 | 认证失败，secret-key 无效 |
| 403 | 无权限访问 |
| 429 | 请求过于频繁，触发限流 |
| 500 | 服务器内部错误 |
| 503 | 服务暂不可用 |
