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
| 13 | order.field | String | | 排序字段，默认 total_units（表1.6 选产品排序字段） |
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
| weightUnit | String | | 重量单位，默认g（表2.7 商品重量单位） |
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
| sellerNation | String | | 卖家所属地，逗号分隔（表1.5 卖家所属地） |
| badgeBS/badgeAC/badgeNR | String | | Best Seller/Amazon's Choice/New Release 标识 (Y) |
| fulfillment | String | | AMZ/FBA/FBM |
| variation | String | | N=含变体, Y=不含变体 |
| page | Integer | | 默认1，总条数限制2000 |
| size | Integer | | 默认50，最大100 |
| order.field | String | | 排序字段，默认 total_units（表1.6 选产品排序字段） |
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
| order.field | String | | 排序字段（表1.8 关键词选品排序字段） |
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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | asin | String | ✓ | ASIN |
| 3 | keyword | String | | 关键词，留空返回所有流量词 |
| 4 | month | String | | 历史月份 yyyyMM，不传默认最近30天 |
| 5 | badges | List | | 流量词类型（附录表1.10） |
| 6 | trafficKeywordTypes | List | | 流量占比类型（附录表2.0） |
| 7 | conversionKeywordTypes | List | | 流量转化类型（附录表2.1） |
| 8 | page | Integer | | 当前页，默认1 |
| 9 | size | Integer | | 每页条数，默认50，最大100，最多查2000条 |
| 10 | order.field | String | | 排序字段，默认 rankPosition（表2.3 流量词列表排序字段） |
| 11 | order.desc | Boolean | | true=降序 false=升序，默认false |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场编码 |
| asin | String | ASIN |
| total | Integer | 总条数 |
| items | List | 词条列表 |
| items[].keyword | String | 关键词 |
| items[].keywordCn | String | 中文翻译 |
| items[].searches | Integer | 月搜索量 |
| items[].products | Integer | 搜索结果商品数 |
| items[].purchases | Integer | 月购买量 |
| items[].purchaseRate | Float | 购买率 |
| items[].bid/bidMax/bidMin | Float | PPC竞价 |
| items[].badges | List | 曝光位置标记 |
| items[].searchesRank | Integer | 搜索频率排名 |
| items[].trafficPercentage | Float | 流量占比 |
| items[].naturalRatio | Float | 自然流量占比 |
| items[].adRatio | Float | 广告流量占比 |
| items[].clicks | Integer | 点击量 |
| items[].impressions | Long | 展示量 |
| stats | List | 高频词统计 |

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
| marketPeriod | String | | 市场周期（表1.7 市场周期） |
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
| order.field/order.desc | - | | 排序（表2.4 ABA选品排序字段） |

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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | keyword | String | ✓ | 关键词 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| time | String | 时间（按月，从2017年01月起） |
| keyword | String | 关键词 |
| keywordCn | String | 中文翻译 |
| keywordJp | String | 日文翻译 |
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
| marketplace | String | ✓ | 市场，见附录表1.2 |
| asin | String | ✓ | ASIN |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| asin | String | ASIN编码 |
| relations | Integer | 全部流量数 |
| freeRelations | Integer | 免费流量数 |
| paidRelations | Integer | 付费流量数 |
| calcTime | Long | 最近计算时间 |
| items | List | 统计概要列表 |
| items[].relation | String | 关联类型（mib/fbt/csi/cob/mie/bab/vav/avp/bav/bca/sp/fsa） |
| items[].count | Integer | 数量 |

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
- **URL**: `https://api.sellersprite.com/v1/traffic/listing/page`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | asinList | List | ✓ | ASIN列表，例：["B07Z82895W"] |
| 3 | relations | List | ✓ | 关联类型（表2.2 关联流量关联类型） |
| 4 | variations | Boolean | | 是否查询变体，默认 false |
| 5 | page | Integer | | 当前页，默认1 |
| 6 | size | Integer | | 每页条数，默认50，最大100 |
| 7 | order.field | String | | 排序字段（表2.5 关联流量排序字段） |
| 8 | order.desc | Boolean | | true=降序 false=升序，默认 true |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| brand | String | 品牌 |
| brandUrl | String | 品牌 URL |
| imageUrl | String | 图片 URL |
| title | String | 标题 |
| parent | String | 父体 |
| nodeId | String | 节点ID |
| nodeIdPath | String | 节点路径 |
| nodeLabelPath | String | 节点名称 |
| bsrId | String | BSR ID |
| bsr | Integer | BSR排名 |
| units | Integer | 月销量 |
| unitsCr | Float | 销量增长率 |
| revenue | Float | 月销售额 |
| price | Float | 价格 |
| profit | Float | 利润率 |
| fba | Float | FBA运费 |
| ratings | Integer | 评分数 |
| ratingsRate | Float | 评分增长率 |
| rating | Float | 评分值 |
| ratingsCv | Integer | 月新增评分数 |
| ratingDelta | Float | 评分变化 |
| availableDate | Long | 上架时间 |
| fulfillment | String | 配送方式 |
| variations | Integer | 变体数 |
| sellers | Integer | 卖家数 |
| sellerId | String | 卖家ID |
| sellerName | String | 卖家名称 |
| sellerNation | String | 卖家所属地 |
| badge | Object | 标识（bestSeller, amazonChoice, newRelease, ebc, video） |
| weight | Float | 重量 |
| dimension | String | 尺寸 |
| dimensionType | String | 尺寸类型 |
| sku | String | SKU |
| subcategories | List | 子类目 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/listing/page' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asinList":["B07Z82895W"],"relations":["also_viewed"],"variations":false,"page":1,"size":50}'
```

---

## 17. 查流量来源(关键词流向)

### 基本信息
- **MCP Code**: `traffic_source`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/traffic/source`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | q | String | ✓ | ASIN 或关键词 |
| 3 | month | String | ✓ | 筛选日期，yyyyMM 格式 |
| 4 | page | Integer | | 当前页，默认1 |
| 5 | size | Integer | | 每页条数，默认50，最大100 |
| 6 | order.field | String | | 排序字段（表2.4 流量来源排序字段） |
| 7 | order.desc | Boolean | | true=降序 false=升序，默认true |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keywords | Integer | 全部流量词数量 |
| searchKeywords | Integer | 自然搜索词 |
| acKeywords | Integer | AC推荐词 |
| editorialKeywords | Integer | ER推荐词 |
| fourStarsKeywords | Integer | 4星推荐词 |
| hrKeywords | Integer | HR推荐词 |
| adKeywords | Integer | SP广告词 |
| videoKeywords | Integer | 视频广告词 |
| brandKeywords | Integer | 品牌广告词 |
| badgeLabels | List | 流量来源概览 |
| badgeDetails | Map | 流量来源明细 |
| asinInfo | Object | ASIN 相关信息 |

### ASIN 信息字段

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| asinUrl | String | ASIN 链接 |
| currency | String | 货币 |
| price | Float | 价格 |
| rating | Float | 评分 |
| reviews | Integer | 评分数 |
| title | String | 标题 |
| sku | String | SKU |
| variations | Integer | 变体数 |
| nodeId | String | 节点ID |
| nodeIdPath | String | 节点路径 |
| nodeLabelPath | String | 节点名称 |
| bsrRank | Integer | BSR排名 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/traffic/source' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","q":"B07Z82895W","month":"202604","page":1,"size":50}'
```

---

## 19. ABA 数据选品-按周

### 基本信息
- **MCP Code**: `aba_research_weekly`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/aba/research/weekly`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | date | String | | 查询日期，为空时查最新周 |
| 3 | departments | List | | 类目列表 |
| 4 | excludeKeywords | String | | 排除关键词 |
| 5 | includeKeywords | String | | 包含关键词 |
| 6 | exactFlag | Boolean | | 是否精确匹配 |
| 7 | rankGrowthValue | Integer | | 搜索增长量 |
| 8 | rankGrowthRate | Double | | 搜索增长率 |
| 9 | minRankGrowthRate | Double | | 最小排名增长率 |
| 10 | maxRankGrowthRate | Double | | 最大排名增长率 |
| 11 | minSearchRank | Integer | | 最小排名 |
| 12 | maxSearchRank | Integer | | 最大排名 |
| 13 | minSearches | Integer | | 最小搜索量 |
| 14 | maxSearches | Integer | | 最大搜索量 |
| 15 | minMonopolyClickRate | Double | | 最小点击集中度 |
| 16 | maxMonopolyClickRate | Double | | 最大点击集中度 |
| 17 | minConversionRate | Double | | 最小转化占比 |
| 18 | maxConversionRate | Double | | 最大转化占比 |
| 19 | minWordCount | Integer | | 最小单词数 |
| 20 | maxWordCount | Integer | | 最大单词数 |
| 21 | minSPR | Integer | | 最小SPR |
| 22 | maxSPR | Integer | | 最大SPR |
| 23 | minTitleDensity | Integer | | 最小标题密度 |
| 24 | maxTitleDensity | Integer | | 最大标题密度 |
| 25 | minClicks | Integer | | 最小点击量 |
| 26 | maxClicks | Integer | | 最大点击量 |
| 27 | minImpressions | Integer | | 最小展示量 |
| 28 | maxImpressions | Integer | | 最大展示量 |
| 29 | searchModel | Integer | | 搜索模式：1热门 2异动 3持续增长 4快速飙升 5潜力 6长尾 |
| 30 | page | Integer | | 当前页，默认1 |
| 31 | size | Integer | | 每页条数，默认40，最大40 |
| 32 | order.field | String | | 排序字段（表2.4 ABA选品排序字段） |
| 33 | order.desc | Boolean | | true=降序 false=升序，默认true |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| date | String | 查询日期 |
| keyword | String | 关键词 |
| keywordCn | String | 关键词中文 |
| keywordJp | String | 关键词日文 |
| departments | List | 类目 |
| searchRank | Integer | 搜索排名 |
| searchRankCv | Integer | 排名增长量 |
| searchRankCr | Double | 排名增长率 |
| searches | Integer | 搜索量 |
| clicks | Integer | 点击量 |
| impressions | Long | 展示量 |
| purchaseRate | Double | 购买率 |
| titleDensityExact | Integer | 首页商品标题中包含该关键词的商品数 |
| clickShareRate | Double | 前三点击比 |
| cvsShareRate | Double | 前三转化总比 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/aba/research/weekly' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","page":1,"size":40}'
```

---

## 20. ABA 数据选品-按月

### 基本信息
- **MCP Code**: `aba_research_monthly`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/aba/research/monthly`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | date | String | | 查询月份，为空时查最近30天 |
| 3 | departments | List | | 类目列表 |
| 4 | excludeKeywords | String | | 排除关键词 |
| 5 | includeKeywords | String | | 包含关键词 |
| 6 | exactFlag | Boolean | | 是否精确匹配 |
| 7 | minRankGrowthRate | Double | | 最小排名增长率 |
| 8 | maxRankGrowthRate | Double | | 最大排名增长率 |
| 9 | minSearchRank | Integer | | 最小搜索排名 |
| 10 | maxSearchRank | Integer | | 最大搜索排名 |
| 11 | minSearches | Integer | | 最小搜索量 |
| 12 | maxSearches | Integer | | 最大搜索量 |
| 13 | minMonopolyClickRate | Double | | 最小点击集中度 |
| 14 | maxMonopolyClickRate | Double | | 最大点击集中度 |
| 15 | minConversionRate | Double | | 最小转化占比 |
| 16 | maxConversionRate | Double | | 最大转化占比 |
| 17 | minWordCount | Integer | | 最小单词数 |
| 18 | maxWordCount | Integer | | 最大单词数 |
| 19 | minSPR | Integer | | 最小SPR |
| 20 | maxSPR | Integer | | 最大SPR |
| 21 | minTitleDensity | Integer | | 最小标题密度 |
| 22 | maxTitleDensity | Integer | | 最大标题密度 |
| 23 | minClicks | Integer | | 最小点击量 |
| 24 | maxClicks | Integer | | 最大点击量 |
| 25 | minImpressions | Integer | | 最小展示量 |
| 26 | maxImpressions | Integer | | 最大展示量 |
| 27 | searchModel | Integer | | 搜索模式：1热门 2异动 3持续增长 4快速飙升 5潜力 6长尾 |
| 28 | page | Integer | | 当前页，默认1 |
| 29 | size | Integer | | 每页条数，最大15 |
| 30 | order.field | String | | 排序字段（表2.4 ABA选品排序字段） |
| 31 | order.desc | Boolean | | true=降序 false=升序，默认true |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| date | String | 查询月份 |
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
  -d '{"marketplace":"US","page":1,"size":15}'
```

---

## 24. 出单词反查

### 基本信息
- **MCP Code**: `keyword_order`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/keyword-order`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表1.2 |
| 2 | asins | List | ✓ | ASIN列表，最大20个 |
| 3 | reverseType | String | ✓ | 反查模式：W=周，M=月 |
| 4 | date | String | | 查询日期。周格式 yyyyMMdd(当周周六)，月格式 yyyyMM |
| 5 | conversionType | List | | 转化类型：E=优质词 S=平稳词 L=流失词 I=无效曝光词 |
| 6 | variation | List | | 是否查询变体：Y=否，N=是 |
| 7 | page | Integer | | 当前页，默认1 |
| 8 | size | Integer | | 每页条数，默认50 |
| 9 | order.field | String | | 排序字段（表2.6 出单词排序字段） |
| 10 | order.desc | Boolean | | 是否倒序，默认 false |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| keyword | String | 关键词 |
| keywordCn | String | 中文翻译 |
| keywordJp | String | 日文翻译 |
| asin | String | 所属ASIN |
| searches | Integer | 搜索量 |
| monopolyClickRate | Float | 点击垄断率 |
| cvsShareRate | Float | 转化共享率 |
| searchRank | Integer | 搜索排名 |
| searchRankGv | Integer | 搜索量变化 |
| searchRankGr | Double | 搜索量变化率 |
| top3ClickingRate | Float | 前三点击占比 |
| top3ConversionRate | Float | 前三转化占比 |
| conversionType | String | 转化类型：E=优质 S=平稳 L=流失 I=无效 |
| pages | Integer | 总页数 |
| page | Integer | 当前页 |
| size | Integer | 每页条数 |
| total | Integer | 总条数 |
| took | Integer | 耗时(毫秒) |
| order | Object | 当前排序信息 |

### 请求示例
```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword-order' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","asins":["B07Z82895W"],"reverseType":"M","date":"202412","page":1,"size":50}'
```

---

## 25. 查评论

### 基本信息
- **MCP Code**: `review`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/review/{marketplace}/{asin}`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | asin | String | ✓ | ASIN |
| 3 | starList | List | | 评论星级（1-5星） |
| 4 | typeList | List | | 评论类型：1=图片 2=视频 3=VP 4=VINE |
| 5 | page | Integer | | 当前页，默认1 |
| 6 | size | Integer | | 每页条数，默认5，最大10 |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| author | String | 评论用户 |
| title | String | 评论标题 |
| content | String | 评论内容 |
| date | Long | 日期时间戳 |
| star | Integer | 星级 |
| authorLabels | List | 评论人标签 |
| skus | List | SKU信息 |
| images | List | 图片链接 |
| videos | List | 视频链接 |
| likes | Integer | 点赞数 |
| image | Boolean | 是否图片评论 |
| video | Boolean | 是否视频评论 |
| verified | Boolean | 是否VP购买评论 |
| vine | Boolean | 是否VINE评论 |
| free | Boolean | 是否免费评论 |
| experience | Boolean | 是否抢先体验评论 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/review/US/B07Z82895W?starList=4,5&typeList=1&page=1&size=10' \
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
| order.field/order.desc | - | | 排序（表1.6 选产品排序字段） |

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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | asinList | List | ✓ | ASIN列表，最多20个 |
| 3 | historyDate | String | | 历史日期，yyyyMM格式 |
| 4 | queryType | Integer | | 查询方式：0=所有变体 1=畅销变体 2=当前变体，默认2 |
| 5 | minSearches | Integer | | 最小月搜索量 |
| 6 | maxSearches | Integer | | 最大月搜索量 |
| 7 | minSearchRank | Integer | | 最小搜索排名 |
| 8 | maxSearchRank | Integer | | 最大搜索排名 |
| 9 | minPurchases | Integer | | 最小购买量 |
| 10 | maxPurchases | Integer | | 最大购买量 |
| 11 | minPurchaseRate | Float | | 最小购买率 |
| 12 | maxPurchaseRate | Float | | 最大购买率 |
| 13 | minProducts | Integer | | 最小商品数 |
| 14 | maxProducts | Integer | | 最大商品数 |
| 15 | minSupplyDemandRatio | Float | | 最小供需比 |
| 16 | maxSupplyDemandRatio | Float | | 最大供需比 |
| 17 | minBid | Float | | 最小PPC竞价 |
| 18 | maxBid | Float | | 最大PPC竞价 |
| 19 | minAdProducts | Integer | | 最小广告竞品数 |
| 20 | maxAdProducts | Integer | | 最大广告竞品数 |
| 21 | minAvgPrice | Float | | 最小均价 |
| 22 | maxAvgPrice | Float | | 最大均价 |
| 23 | minWordCount | Integer | | 最小单词个数 |
| 24 | maxWordCount | Integer | | 最大单词个数 |
| 25 | includeKeywords | List | | 包含的词 |
| 26 | excludeKeywords | List | | 排除的词 |
| 27 | minSPR | Integer | | 最小SPR |
| 28 | maxSPR | Integer | | 最大SPR |
| 29 | minTitleDensity | Integer | | 最小标题密度 |
| 30 | maxTitleDensity | Integer | | 最大标题密度 |
| 31 | minMonopolyClickRate | Float | | 最小点击集中度 |
| 32 | maxMonopolyClickRate | Float | | 最大点击集中度 |
| 33 | minTrafficPercentage | Float | | 最小流量占比 |
| 34 | maxTrafficPercentage | Float | | 最大流量占比 |
| 35 | minConversionRate | Float | | 最小转化率 |
| 36 | maxConversionRate | Float | | 最大转化率 |
| 37 | amazonChoice | Boolean | | 亚马逊推荐词 |
| 38 | page | Integer | | 当前页，默认1 |
| 39 | size | Integer | | 每页条数，默认50，最大50 |
| 40 | order.field | String | | 排序字段（表2.5 关联流量排序字段） |
| 41 | order.desc | Boolean | | true=降序 false=升序，默认true |

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
  -d '{"marketplace":"US","asinList":["B07Z82895W"],"page":1,"size":50}'
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
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/google/trends`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见附录表1.2 |
| 2 | keyword | String | | 关键字 |
| 3 | googleProp | String | | 类别：web=Google网页搜索，shoppingCart=Google购物搜索 |
| 4 | monthly | Boolean | | 是否按月份，默认 false |

### 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| keyword | String | 关键字 |
| link | String | Google趋势链接 |
| items | List | 趋势数据明细 |
| items[].time | Long | 时间戳（毫秒） |
| items[].value | Integer | 趋势指数值 |

### 请求示例
```bash
curl -X GET 'https://api.sellersprite.com/v1/google/trends?marketplace=US&keyword=iphone+stand' \
  -H 'secret-key: Your Secret'
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
