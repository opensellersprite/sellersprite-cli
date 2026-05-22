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
| 1 | marketplace | String | ✓ | 市场编码，见表 1.2 |
| 2 | month | String |  | 查询月份，格式：yyyyMM，示例：202507，见表 1.1 |
| 3 | brand | String |  | 品牌，WWDOLL |
| 4 | sellerName | String |  | 卖家，Apple |
| 5 | asins | List |  | asin 的 list 字符串，最多支持40个ASIN |
| 6 | nodeIdPath | String |  | 类目节点字符串，见查产品类目 |
| 7 | nodeIdPathEqual | boolean |  | 类目节点查询方式，true: 为类目精确查询, false: 为查询当前及子类目; 默认：false |
| 8 | keyword | String |  | 关键字 |
| 9 | matchType | Integer |  | 关键词匹配方式，1：词组匹配，2：模糊匹配，3：精准匹配；默认：2 |
| 10 | variation | String |  | 是否查询变体ASIN，N: 含变体, Y: 不含变体 |
| 11 | page | Integer |  | 页码，Default: 1 |
| 12 | size | Integer |  | 每页条数，Default：50，Max: 100 |
| 13 | order | Object |  | 排序对象 |
| 14 | └field | String |  | 排序字段，默认：total_units，见表1.6 |
| 15 | └desc | boolean |  | 排序方式，true：desc，false：asc；Default：true |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asin | String | asin | B078J8VPVW |
| 2 | brand | String | 品牌 | Pampers |
| 3 | brandUrl | String | 品牌 URL | https://www.amazon.com/s?k=HP |
| 4 | imageUrl | String | 图片 URL | https://images-na.ssl-images-amazon.com/images/I/51axlzme6aL .AC_US200.jpg |
| 5 | title | String | 商品标题 | Diapers Size …… |
| 6 | parent | String | 父体 | B081RGNL17 |
| 7 | nodeId | Long | 节点 id | 3741281 |
| 8 | nodeIdPath | String | 节点 id 路径字符串 | 2619525011:3741271:3741281 |
| 9 | nodeLabelPath | String | 类目 | Baby Products:Diapering:Disposable Diapers |
| 10 | symbol | String | 是否畅销 | Y |
| 11 | bsrId | String | BSRid | office-products |
| 12 | bsr | Integer | BSR 排名 | 1 |
| 13 | bsrCr | Float | BSR 增长率 | 926.67 |
| 14 | bsrCv | Integer | BSR 增长数 | 10 |
| 15 | units | Integer | 月销量(父体) | 26289 |
| 16 | unitsGr | Float | 月销量增长率(父体) | -46.3 |
| 17 | amzUnit | Integer | 子体近30日销量 | 4000 |
| 18 | amzSales | Float | 销售额(子体) | 235000 |
| 19 | amzUnitDate | Date | 子体销量更新日期 | 1702476590000 |
| 20 | revenue | Float | 月销售额(父体) | 1693537.4 |
| 21 | price | Float | 价格 | 64.42 |
| 22 | primePrice | Float | prime价格，-1表示没有 | 56.6 |
| 23 | profit | Float | 利润率 | 63.92 |
| 24 | fba | Float | fba 运费 | 13.58 |
| 25 | ratings | Integer | 评分数 | 32004 |
| 26 | ratingsRate | Float | 留评率 | 40.57 |
| 27 | rating | Float | 评分 | 4.8 |
| 28 | ratingsCv | Integer | 月度增长数 | 10666 |
| 29 | ratingDelta | Integer | 留评数：近 30 天新增评论数 | 0 |
| 30 | lqs | Float | listing质量得分 |  |
| 31 | availableDate | Long | 上架时间 | 1454083200000 |
| 32 | fulfillment | String | 配送方式 | AMZ or FBA or FBM |
| 33 | variations | Integer | 变体数 | 7 |
| 34 | sellers | Integer | 卖家数 | 7 |
| 35 | sellerId | String | BuyBox 卖家 id | A1Y8BVAASXO4R7 |
| 36 | sellerName | String | BuyBox 卖家 | Amazon |
| 37 | sellerNation | String | BuyBox 卖家国籍 | 见表 1.5 |
| 38 | badge | Badge | 标识 | 包括了下面 5 个标识 |
| 39 | └bestSeller | String | Best Seller 标识 | Y / N |
| 40 | └amazonChoice | String | amazon choice 标识 | Y / N |
| 41 | └amazonChoice | String | amazon choice 标识 | Y / N |
| 42 | └newRelease | String | release 标识 | Y / N |
| 43 | └ebc | String | A+页面 | Y / N |
| 44 | └video | String | 视频介绍 | Y / N |
| 45 | weight | String | 重量 | 8.88 pounds |
| 46 | dimension | String | 尺寸 | 13.3 x 15.8 x 10.6 inches |
| 47 | dimensionsType | String | 尺寸类型 | ST,0V |
| 48 | pkgDimensions | String | 包装尺寸 | 14.3 x 16.8 x 12.6 inches |
| 49 | pkgDimensionType | String | 包装尺寸类型 |  |
| 50 | pkgWeight | String | 包装重量 | 18.88 pounds |
| 51 | sku | String | sku | ["Color: Beige","Size: 47 inches"] |
| 52 | subcategories | List | 子类目 |  |
| 53 | └code | String | 类目code | 1063242 |
| 54 | └rank | Integer | 排名 | 1 |
| 55 | └label | String | 名称 | Bath Rugs |
| 56 | deliveryPrice | Float | 卖家运费,-1表示没有 | 4 |
| 57 | primePrice | Float | prime价格，-1表示没有 | 42 |

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

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场编码，见表 1.2 |
| 2 | month | String |  | 查询月份，格式：yyyyMM，示例：202507，见表 1.1 |
| 3 | keyword | String |  | 关键字，N95 |
| 4 | includeSellers | String |  | 包含卖家 |
| 5 | excludeSellers | String |  | 排除卖家 |
| 6 | matchType | Integer |  | 匹配方式，1词组匹配 2模糊匹配 3精准匹配；默认2，2 |
| 7 | excludeKeywords | String |  | 排除的关键字，portable |
| 8 | minPrice | Float |  | 最低价格，10 |
| 9 | maxPrice | Float |  | 最高价格，30 |
| 10 | minRating | Float |  | 最低评分值，1 |
| 11 | maxRating | Float |  | 最高评分值，5 |
| 12 | minRatings | Integer |  | 最低评分数，1 |
| 13 | maxRatings | Integer |  | 最高评分数，90 |
| 14 | minRatingsCv | Integer |  | 最低月新增评分数，1 |
| 15 | maxRatingsCv | Integer |  | 最高月新增评分数，5 |
| 16 | minSellers | Integer |  | 最小卖家数量，3 |
| 17 | maxSellers | Integer |  | 最大卖家数量，10 |
| 18 | minProfit | Float |  | 最小毛利率，10 |
| 19 | maxProfit | Float |  | 最大毛利率，20 |
| 20 | minBsr | Integer |  | 大类 BSR 最高排名，1 |
| 21 | maxBsr | Integer |  | 大类 BSR 最低排名，100 |
| 22 | minBsrCv | Integer |  | BSR 最低增长数，3 |
| 23 | maxBsrCv | Integer |  | BSR 最高增长数，5 |
| 24 | minBsrCr | Float |  | BSR 最低增长率，30 |
| 25 | maxBsrCr | Float |  | BSR 最高增长率，60 |
| 26 | minUnits | Integer |  | 最低月销量，20 |
| 27 | maxUnits | Integer |  | 最高月销量，50 |
| 28 | minAmzUnit | Integer |  | 最低月子体销量，20 |
| 29 | maxAmzUnit | Integer |  | 最高月子体销量，50 |
| 30 | minRevenue | Float |  | 最低月销售额，60 |
| 31 | maxRevenue | Float |  | 最高月销售额，200 |
| 32 | minRevenueCr | Float |  | 月销售额最低增长率，20 |
| 33 | maxRevenueCr | Float |  | 月销售额最高增长率，30 |
| 34 | minUnitsCr | Float |  | 月销量最低增长率，20 |
| 35 | maxUnitsCr | Float |  | 月销量最高增长率，30 |
| 36 | weightUnit | String |  | 重量单位，默认：g，见表2.7 |
| 37 | minWeights | Float |  | 最小重量，20 |
| 38 | maxWeights | Float |  | 最大重量，30 |
| 39 | minVariations | Integer |  | 最低变体数，1 |
| 40 | maxVariations | Integer |  | 最高变体数，3 |
| 41 | filterSub | String |  | 是否筛选子类目，Y：是，只有在指定类目时才会生效 |
| 42 | minSubBsrRank | Integer |  | 最小子类排名，只有参数 filterSub=Y 时才生效 |
| 43 | maxSubBsrRank | Integer |  | 最大子类排名，只有参数 filterSub=Y 时才生效 |
| 44 | includeBrands | String |  | 包含品牌，Apple |
| 45 | excludeBrands | String |  | 排除品牌，Apple |
| 46 | nodeIdPaths | List |  | 类目节点字符串列表，见查产品类目接口 |
| 47 | nodeIdPathEqual | boolean |  | true为类目精确查询 false为查询当前及子类目，默认false |
| 48 | availableMonth | Integer |  | 上架月份，见表 1.3，默认不限制 |
| 49 | dimensionType | String |  | 尺寸类型集合,逗号分隔，默认不限制，见表 1.4 |
| 50 | minFba | Float |  | FBA 最低运费，10 |
| 51 | maxFba | Float |  | FBA 最高运费，20 |
| 52 | minLqs | Float |  | 最低 Listing 页面质量分，0 |
| 53 | maxLqs | Float |  | 最高 Listing 页面质量分，10 |
| 54 | sellerNation | String |  | 卖家所属地，默认不限制，多条件查询用逗号隔开，见表 1.5 |
| 55 | badgeBS | String |  | 是否有热销标识 Best Seller，Y:是 |
| 56 | badgeAC | String |  | 是否有热销标识 Amazon's Choice，Y:是 |
| 57 | badgeNR | String |  | 是否有新品标识 New Release，Y:是 |
| 58 | fulfillment | String |  | 配送方式，多条件查询用逗号隔开，AMZ or FBA or FBM |
| 59 | variation | String |  | 是否查询变体 asin，N: 含变体, Y: 不含变体 |
| 60 | page | Integer |  | 页码，从 1 开始，默认：1，总条数限制2000条，可以细分条件拉取整个类目数据 |
| 61 | size | Integer |  | 每页条数，默认：50，最大：100 |
| 62 | order | Object |  | 排序 |
| 63 | └field | String |  | 排序字段，默认：total_units，见表1.6 |
| 64 | └desc | boolean |  | 排序方式，true：desc，false：asc；Default：true |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asin | String | asin | B078J8VPVW |
| 2 | brand | String | 品牌 | Pampers |
| 3 | brandUrl | String | 品牌 URL | https://www.amazon.com/s?k=HP |
| 4 | imageUrl | String | 图片 URL | https://images-na.ssl-images-amazon.com/images/I/51axlzme6aL .AC_US200.jpg |
| 5 | title | String | 商品标题 | Diapers Size 2, 186 Count - Pampers Swaddlers Disposable Baby Diapers, ONE MONTH SUPPLY |
| 6 | parent | String | 父体 | B081RGNL17 |
| 7 | nodeId | Long | 节点 id | 3741281 |
| 8 | nodeIdPath | String | 节点 id 路径字符串 | 2619525011:3741271:3741281 |
| 9 | nodeLabelPath | String | 类目 | Baby Products:Diapering:Disposable Diapers |
| 10 | symbol | String | 是否畅销 | Y |
| 11 | bsrId | String | BSRid | office-products |
| 12 | bsr | Integer | BSR 排名 | 1 |
| 13 | bsrCr | Float | BSR 增长率 | 926.67 |
| 14 | bsrCv | Integer | BSR 增长数 | 10 |
| 15 | units | Integer | 月销量(父) | 26289 |
| 16 | unitsGr | Float | 月销量增长率 | -46.3 |
| 17 | amzUnit | Integer | 子体近30日销量(仅近30日查询支持) | 4000 |
| 18 | amzUnitDate | Date | 子体销量更新日期 | 1.70248E+12 |
| 19 | revenue | Float | 月销售额(父体) | 1693537.4 |
| 20 | price | Float | 价格 | 64.42 |
| 21 | primePrice | Float | prime价格，-1表示没有 | 56.6 |
| 22 | profit | Float | 利润率 | 63.92 |
| 23 | fba | Float | fba 运费 | 13.58 |
| 24 | ratings | Integer | 评分数 | 32004 |
| 25 | ratingsRate | Float | 留评率 | 40.57 |
| 26 | rating | Float | 评分 | 4.8 |
| 27 | ratingsCv | Integer | 月度增长数 | 10666 |
| 28 | ratingDelta | Integer | 留评数：近 30 天新增评论数 | 0 |
| 29 | lqs | Float | listing质量得分 |  |
| 30 | availableDate | Long | 上架时间，时间戳格式 | 1.45408E+12 |
| 31 | fulfillment | String | 配送方式 | AMZ or FBA or FBM |
| 32 | variations | Integer | 变体数 | 7 |
| 33 | sellers | Integer | 卖家数 | 7 |
| 34 | sellerId | String | BuyBox 卖家 id | A1Y8BVAASXO4R7 |
| 35 | sellerName | String | BuyBox 卖家 | Amazon |
| 36 | sellerNation | String | BuyBox 卖家国籍 | 见表 1.5 |
| 37 | badge | Badge | 标识 | 包括了下面 5 个标识 |
| 38 | └bestSeller | String | Best Seller 标识 | Y 或者 N |
| 39 | └amazonChoice | String | amazon choice 标识 | Y 或者 N |
| 40 | └newRelease | String | release 标识 | Y 或者 N |
| 41 | └ebc | String | A+页面 | Y 或者 N |
| 42 | └video | String | 视频介绍 | Y 或者 N |
| 43 | weight | String | 重量 | 8.88 pounds |
| 44 | dimension | String | 尺寸 | 13.3 x 15.8 x 10.6 inches |
| 45 | dimensionsType | String | 尺寸类型 | ST,0V |
| 46 | pkgDimensions | String | 包装尺寸 | 14.3 x 16.8 x 12.6 inches |
| 47 | pkgDimensionType | String | 包装尺寸类型 |  |
| 48 | pkgWeight | String | 包装重量 | 18.88 pounds |
| 49 | subcategories | List | 子类目 |  |
| 50 | └code | String | 类目code | 1063242 |
| 51 | └rank | Integer | 排名 | 1 |
| 52 | └label | String | 名称 | Bath Rugs |
| 53 | sku | String | sku | ["Color: Beige","Size: 47 inches"] |
| 54 | deliveryPrice | Float | 卖家运费,-1表示没有 | 4 |
| 55 | primePrice | Float | prime价格，-1表示没有 | 42 |
| 56 | └amazonChoice | String | amazon choice 标识 | Y 或者 N |
| 57 | primePrice | Float | prime价格，-1表示没有 | 42 |

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

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asin | String | asin | B08GHW4TBS |
| 2 | asinUrl | String | asin url | https://www.amazon.com/dp/B08GHW4TBS |
| 3 | availableDate | Long | 上架日期 | 1609059137000 |
| 4 | badge | Badge | 标识 | 包括了下面 5 个标识 |
| 5 | └bestSeller | String | Best Seller 标识 | Y 或者 N |
| 6 | └amazonChoice | String | amazon choice 标识 | Y 或者 N |
| 7 | └newRelease | String | release 标识 | Y 或者 N |
| 8 | └ebc | String | A+页面 | Y 或者 N |
| 9 | └video | String | 视频介绍 | Y 或者 N |
| 10 | brand | String | 品牌 | mermaker |
| 11 | brandUrl | String | 品牌 URL | /stores/Mermaker/page/984A6448-1C68-4CCA-AD5A-D574EA2D65D5?ref_=ast_bln |
| 12 | bsrId | String | bsr id | home-garden |
| 13 | bsrLabel | String | bsr 标签 | Home & Kitchen |
| 14 | bsrRank | Integer | bsr 排名 | 1006 |
| 15 | createdTime | Long | 创建时间 | 1606467137000 |
| 16 | dimensions | String | 尺寸 | 7 x 6 x 0.6 inches |
| 17 | firstRatingDate | Long | 第一次评论时间 | 1609059137000 |
| 18 | imageUrl | String | 图片链接 | https://images-na.ssl-images-amazon.com/images/I/412616zl5YL .AC_US200.jpg |
| 19 | lqs | Integer | Listing 页面质量得分 | 97 |
| 20 | nodeId | String | 节点 id | 1063280 |
| 21 | nodeIdPath | String | 节点 id 串 | 1055398:1063252:1063280 |
| 22 | nodeLabelPath | String | 类目名称串 | Home & Kitchen:Bedding:Blankets & Throws |
| 23 | nodeLabelPathLocale | String | 类目名称串中文 | 家居厨房用品:床上用品:毯子、盖毯 |
| 24 | parent | String | 父 asin | B07V5GB9B5 |
| 25 | price | Float | 价格 | 21.99 |
| 26 | questions | Integer | 问题数量 | 5 |
| 27 | rating | Float | 评分 | 4.8 |
| 28 | ratings | Integer | 评分数 | 29229 |
| 29 | reviews | Integer | 评论数 | 9229 |
| 30 | variantRatings | Integer | 子体评分数 | 12454 |
| 31 | variantReviews | Integer | 子体评论数 | 3211 |
| 32 | sellerId | String | 卖家 id | A13AJ1GXFINAZ |
| 33 | sellerName | String | 卖家名称 | Mermaker |
| 34 | fulfillment | String | 配送方式 | FBA |
| 35 | sellers | Integer | 卖家数 | 1 |
| 36 | skuList | List | sku | ["Color: Beige","Size: 47 inches"] |
| 37 | marketplace | String | String | 见表 1.2 |
| 38 | title | String | 标题 | mermaker Burritos Tortilla Blanket 2.0 Double Sided 47 inches for Adult and Kids,Giant Funny Realistic Food Throw Blanket,285 GSM Novelty Soft Flannel Taco Blanket (Yellow Blanket-Double Sided) |
| 39 | features | List | 五点描述 |  |
| 40 | overviews | String | 详情，json格式字符串 |  |
| 41 | updatedTime | Long | 更新时间 | 1609059137000 |
| 42 | variationList | List | 变体 | [{"asin":"B07V5GB9B5","attribute":"Beige"},{"asin":"B08H86SSSF","attribute":"Cookie"}] |
| 43 | variations | Integer | 变体数量 | 14 |
| 44 | weight | String | 重量 | 15.2 ounces |
| 45 | zoomImageUrl | String | 大图 URL | https://images-na.ssl-images-amazon.com/images/I/412616zl5YL .AC_US600.jpg |
| 46 | subcategories | Object | 子类目信息 |  |
| 47 | └rank | Integer | 子类目排名 | 1 |
| 48 | └code | String | 子类目code | 17874234011 |
| 49 | └label | String | 子类目标签 | Kids' Throw Blankets |
| 50 | deliveryPrice | Float | 卖家运费,-1表示没有 | 4 |
| 51 | primePrice | Float | prime价格，-1表示没有 | 42 |
| 52 | coupon | String | 优惠卷 | [save $20] |
| 53 | └amazonChoice | String | amazon choice 标识 | Y 或者 N |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/asin/{marketplace}/{asin}' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US&asin=B08GHW4TBS'
```

---

## 6. 关键词挖掘

### 基本信息
- **MCP Code**: `keyword_miner`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/keyword/miner`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | historyDate | String |  | 历史日期，yyyyMM格式，最近30天不传或传空字符串，202201 |
| 3 | keyword | String | ✓ | 关键词 |
| 4 | keywordList | List |  | 批量查询关键词，["phone stand"] |
| 5 | minSearch | Integer |  | 最小搜索量，543 |
| 6 | maxSearch | Integer |  | 最大搜索量，23453 |
| 7 | minPurchases | Integer |  | 最小购买量，6 |
| 8 | maxPurchases | Integer |  | 最大购买量，34 |
| 9 | minPurchasesRate | Float |  | 最小购买率，3 |
| 10 | maxPurchasesRate | Float |  | 最大购买率，43 |
| 11 | minSPR | Integer |  | 最小SPR，2 |
| 12 | maxSPR | Integer |  | 最大SPR，16 |
| 13 | minTitleDensity | Integer |  | 最小标题密度，2 |
| 14 | maxTitleDensity | Integer |  | 最大标题密度，23 |
| 15 | minRelevancy | Float |  | 最小相关度，23，最小0 |
| 16 | maxRelevancy | Float |  | 最大相关度，90，最大100 |
| 17 | minSearchRank | Integer |  | 最小搜索排名，33 |
| 18 | maxSearchRank | Integer |  | 最大搜索排名，3223 |
| 19 | minProducts | Integer |  | 最小商品数，54 |
| 20 | maxProducts | Integer |  | 最大商品数，324 |
| 21 | minSupplyDemandRatio | Float |  | 最小供需比，11.2 |
| 22 | maxSupplyDemandRatio | Float |  | 最大供需比，45.2 |
| 23 | minAdProducts | Integer |  | 最小广告竞品数，123 |
| 24 | maxAdProducts | Integer |  | 最大广告竞品数，345 |
| 25 | minWordCount | Integer |  | 最小单词个数，2 |
| 26 | maxWordCount | Integer |  | 最大单词个数，4 |
| 27 | minMonopolyClickRate | Float |  | 最小点击集中度，23.4 |
| 28 | maxMonopolyClickRate | Float |  | 最大点击集中度，53.1 |
| 29 | minBid | Float |  | 最小ppc竞价，10.2 |
| 30 | maxBid | Float |  | 最大ppc竞价，23.1 |
| 31 | minPrice | Float |  | 最小均价，43.3 |
| 32 | maxPrice | Float |  | 最大均价，234.2 |
| 33 | minRatings | Integer |  | 最小评分数，100 |
| 34 | maxRatings | Integer |  | 最大评分数，399 |
| 35 | minRating | Float |  | 最小评分值，3 |
| 36 | maxRating | Float |  | 最大评分值，4.9 |
| 37 | amazonChoice | Boolean |  | 亚马逊推荐词，true |
| 38 | filterRootWord | Integer |  | 过滤词根 0包含所有 1只包含词根，0 |
| 39 | matchType | Integer |  | 2: 广泛匹配, 3: 词组匹配，2 |
| 40 | includeKeywords | List |  | 包含的词，["phone stand"] |
| 41 | excludeKeywords | List |  | 排除的词，["phone stand"] |
| 42 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 43 | size | Integer |  | 每页条数，默认：50，最大：100 |
| 44 | order | Object |  | 排序 |
| 45 | └field | String |  | 排序字段，加入筛序条件之后，不能以相关度排序，见表2.4 |
| 46 | └desc | boolean |  | true为降序 false为升序，默认降序 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场，见表 1.2 | US |
| 2 | keyword | String | 关键词 | phone stand for recording |
| 3 | keywordCn | String | 关键词中文翻译 | 用于录音的电话支架 |
| 4 | keywordJp | String | 关键词英文翻译 | 録音用電話スタンド |
| 5 | departments | List | 类目 |  |
| 6 | └code | String | 类目代码 | electronics |
| 7 | └label | String | 类目名称 | Electronics |
| 8 | month | String | 搜索月份 | 2022.01 |
| 9 | supplement | String | 是否属于补充关键词（无当前月搜索量） | N |
| 10 | searches | Integer | 搜索量 | 21582 |
| 11 | purchases | Integer | 月购买量 | 1996 |
| 12 | purchaseRate | Float | 月购买率 | 0.0925 |
| 13 | monopolyClickRate | Float | 点击垄断率 | 0.3 |
| 14 | products | Integer | 商品数 | 1645 |
| 15 | adProducts | Integer | 广告竞品数 | 34 |
| 16 | supplyDemandRatio | Float | 供需比 | 13.12 |
| 17 | avgPrice | Float | 平均价格 | 36.14 |
| 18 | avgRatings | Integer | 平均评分数 | 12223 |
| 19 | avgRating | Float | 平均评分值 | 4.5 |
| 20 | bidMin | Float | 最小PPC价格 | 1.34 |
| 21 | bidMax | Float | 最大PPC价格 | 3.21 |
| 22 | bid | Float | PPC价格 | 1.6 |
| 23 | cvsShareRate | Float | 转化共享率 | 0.3084 |
| 24 | wordCount | Integer | 单词个数 | 4 |
| 25 | titleDensity | Integer | 标题密度 | 42.9 |
| 26 | spr | Integer | SPR | 6 |
| 27 | relevancy | Double | 相关度 | 28.6 |
| 28 | amazonChoice | Boolean | 亚马逊推荐词 true是的 false不是 | false |
| 29 | searchRank | Integer | 搜索排名 | 17910 |
| 30 | └code | String | 类目代码 | electronics |
| 31 | └label | String | 类目名称 | Electronics |
| 32 | clicks | Integer | 点击量 | 10 |
| 33 | impressions | Long | 展示量 | 20 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword/miner' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "keyword": "test"}'
```

## 9. 查产品类目

### 基本信息
- **MCP Code**: `product_node`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/product/node`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | nodeIdPath | String |  | 类目节点 id 字符串，2619525011:3741271:3741281 |
| 3 | keyword | String |  | 搜索关键字，nodeId或类目名称，Books 或者 4053 |
| 4 | month | String |  | 查询历史月份类目，格式yyyyMM，202502 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | nodeIdPath | String | 类目 id 字符串，即 nodeIdPath | 2619525011:3741271 |
| 2 | nodeLabelPath | String | 类目名称 | Appliances:Dishwashers |
| 3 | products | Integer | 类目下产品数 | 42 |
| 4 | nodeLabelLocale | String | 类目节点名称中文 | 洗碗机 |
| 5 | nodeLabelPathLocale | String | 类目所属所有节点名称中文 | 大家电:洗碗机 |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/product/node' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US'
```

---

## 56. ASIN优惠趋势

### 基本信息
- **MCP Code**: `asin_coupon_trend`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/coupon-trend`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | marketplace |  |
| 2 | asin | String | asin |  |
| 3 | date | String | 日期 |  |
| 4 | type | String | 优惠类型 | M: 减免金额, P: 百分比折扣 |
| 5 | asinPrice | Float | ASIN价格 |  |
| 6 | couponPrice | Float | 优惠金额 |  |
| 7 | finalPrice | Float | 实际价格 |  |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/coupon-trend' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US&asin=B08GHW4TBS'
```

---

## 57. ASIN详情及优惠趋势

### 基本信息
- **MCP Code**: `asin_detail_with_coupon_trend`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/with-coupon-trend`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asin | Object | Asin Object |  |
| 2 | └asin | String | asin | B08GHW4TBS |
| 3 | └asinUrl | String | asin url | https://www.amazon.com/dp/B08GHW4TBS |
| 4 | └availableDate | Long | 上架日期 | 1609059137000 |
| 5 | └badge | Badge | 标识 | 包括了下面 5 个标识 |
| 6 | └└bestSeller | String | Best Seller 标识 | Y 或者 N |
| 7 | └└amazonChoice | String | amazon choice 标识 | Y 或者 N |
| 8 | └└newRelease | String | release 标识 | Y 或者 N |
| 9 | └└ebc | String | A+页面 | Y 或者 N |
| 10 | └└video | String | 视频介绍 | Y 或者 N |
| 11 | └brand | String | 品牌 | mermaker |
| 12 | └brandUrl | String | 品牌 URL | /stores/Mermaker/page/984A6448-1C68-4CCA-AD5A-D574EA2D65D5?ref_=ast_bln |
| 13 | └bsrId | String | bsr id | home-garden |
| 14 | └bsrLabel | String | bsr 标签 | Home & Kitchen |
| 15 | └bsrRank | Integer | bsr 排名 | 1006 |
| 16 | └createdTime | Long | 创建时间 | 1606467137000 |
| 17 | └dimensions | String | 尺寸 | 7 x 6 x 0.6 inches |
| 18 | └firstRatingDate | Long | 第一次评论时间 | 1609059137000 |
| 19 | └imageUrl | String | 图片链接 | https://images-na.ssl-images-amazon.com/images/I/412616zl5YL .AC_US200.jpg |
| 20 | └lqs | Integer | Listing 页面质量得分 | 97 |
| 21 | └nodeId | String | 节点 id | 1063280 |
| 22 | └nodeIdPath | String | 节点 id 串 | 1055398:1063252:1063280 |
| 23 | └nodeLabelPath | String | 类目名称串 | Home & Kitchen:Bedding:Blankets & Throws |
| 24 | └nodeLabelPathLocale | String | 类目名称串中文 | 家居厨房用品:床上用品:毯子、盖毯 |
| 25 | └parent | String | 父 asin | B07V5GB9B5 |
| 26 | └price | Float | 价格 | 21.99 |
| 27 | └questions | Integer | 问题数量 | 5 |
| 28 | └rating | Float | 评分 | 4.8 |
| 29 | └ratings | Integer | 评分数 | 29229 |
| 30 | └reviews | Integer | 评论数 | 9229 |
| 31 | └variantRatings | Integer | 子体评分数 | 12454 |
| 32 | └variantReviews | Integer | 子体评论数 | 3211 |
| 33 | └sellerId | String | 卖家 id | A13AJ1GXFINAZ |
| 34 | └sellerName | String | 卖家名称 | Mermaker |
| 35 | └fulfillment | String | 配送方式 | FBA |
| 36 | └sellers | Integer | 卖家数 | 1 |
| 37 | └skuList | List | sku | ["Color: Beige","Size: 47 inches"] |
| 38 | └marketplace | String | String | 见表 1.2 |
| 39 | └title | String | 标题 | mermaker Burritos Tortilla Blanket 2.0 Double Sided 47 inches for Adult and Kids,Giant Funny Realistic Food Throw Blanket,285 GSM Novelty Soft Flannel Taco Blanket (Yellow Blanket-Double Sided) |
| 40 | └features | List | 五点描述 |  |
| 41 | └overviews | String | 详情，json格式字符串 |  |
| 42 | └updatedTime | Long | 更新时间 | 1609059137000 |
| 43 | └variationList | List | 变体 | [{"asin":"B07V5GB9B5","attribute":"Beige"},{"asin":"B08H86SSSF","attribute":"Cookie"}] |
| 44 | └variations | Integer | 变体数量 | 14 |
| 45 | └weight | String | 重量 | 15.2 ounces |
| 46 | └zoomImageUrl | String | 大图 URL | https://images-na.ssl-images-amazon.com/images/I/412616zl5YL .AC_US600.jpg |
| 47 | └subcategories | Object | 子类目信息 |  |
| 48 | └└rank | Integer | 子类目排名 | 1 |
| 49 | └└code | String | 子类目code | 17874234011 |
| 50 | └└label | String | 子类目标签 | Kids' Throw Blankets |
| 51 | └deliveryPrice | Float | 卖家运费,-1表示没有 | 4 |
| 52 | └primePrice | Float | prime价格，-1表示没有 | 42 |
| 53 | └coupon | String | 优惠卷 | [save $20] |
| 54 | couponTrends | List | Coupon Trends |  |
| 55 | └marketplace | String | marketplace | 见表 1.2 |
| 56 | └asin | String | asin | B08GHW4TBS |
| 57 | └date | String | 日期 |  |
| 58 | └type | String | 优惠类型 | M: 减免金额, P: 百分比折扣 |
| 59 | └asinPrice | Float | ASIN价格 |  |
| 60 | └couponPrice | Float | 优惠金额 |  |
| 61 | └finalPrice | Float | 实际价格 |  |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/with-coupon-trend' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US&asin=B08GHW4TBS'
```

---

## 27. ASIN 销量预测

### 基本信息
- **MCP Code**: `asin_prediction`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/asin`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asin | String | ✓ | B07Z82895W |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asinDetail | Object | asin明细 |  |
| 2 | └asin | String | asin | B00CFM8DI2 |
| 3 | └title | String | 标题 | Boot Bananas Original Shoe Deodorizer |
| 4 | └brand | String | 平台 | Boot Bananas |
| 5 | └availableDate | Long | 上架时间 | 1397001600000 |
| 6 | └category | String | 类目名称 | Clothing, Shoes & Jewelry |
| 7 | └categoryId | String | 类目id | 7141123011 |
| 8 | └imageUrl | String | 图片URL | https://images-na.ssl-images-amazon.com/images/I/41AGxmiW-vL._AC_US600_.jpg |
| 9 | └ratings | Integer | 评分数 | 32004 |
| 10 | └rating | Float | 评分值 | 4.6 |
| 11 | dailyItemList | List | 日销量预测明细 |  |
| 12 | └date | String | 日期 | 45035 |
| 13 | └bsr | Integer | bsr | 48614 |
| 14 | └sales | Integer | 销量 | 14 |
| 15 | └amount | Float | 销售额 | 200 |
| 16 | └price | Float | 单价 | 20 |
| 17 | monthItemList | List | 月销量预测明细 |  |
| 18 | └date | String | 日期 | 45017 |
| 19 | └sales | Integer | 销量 | 14 |
| 20 | └amount | Float | 销售额 | 200 |
| 21 | └price | Float | 单价 | 20 |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/sales/prediction/asin' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US&asin=B08GHW4TBS'
```

---

## 26. BSR销量预测

### 基本信息
- **MCP Code**: `bsr_prediction`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/bsr`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | bsr | Integer | ✓ | 大类排名，1024 |
| 3 | categoryId | String | ✓ | 一级类目节点，查产品类目返回，11260432011 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | bsr | Integer | 1 | B07Z82895W |
| 3 | categoryLabel | String | 类目名称 | 2685 |
| 4 | estDailySales | Integer | 预测日销量 | 99 |
| 5 | estMonthSales | Integer | 预测30天销量 | 2965 |
| 6 | itemList | List | 明细 |  |
| 7 | └bsr | Integer | bsr | 1 |
| 8 | └estDailySales | Integer | 预测日销量 | 99 |
| 9 | └estMonthSales | Integer | 预测30天销量 | 2965 |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/sales/prediction/bsr' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US&bsr=2&categoryId='
```

---

## 14. 关键词反查(流量词列表)

### 基本信息
- **MCP Code**: `traffic_keyword`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword`

### 请求参数

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

### 响应参数

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
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/keepa/{marketplace}/{asin}`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |
| 3 | startTimestamp | Long |  | Trend Data Start Timestamp |
| 4 | endTimestamp | Long |  | Trend Data End Timestamp |
| 5 | dailyLatest | Boolean |  | Only Get Daily Latest Data |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | 见表 1.2 |
| 2 | asin | String | asin | B07V34QQ3C |
| 3 | dataAsin | String | 实际返回Keepa数据的ASIN | B07V34QQ3C |
| 4 | parentAsin | String | 父体ASIN | B0CWW9N7QW |
| 5 | variationAsins | List | 变体ASIN列表 | ["B0CN2PBVNS","B0BT4PMNY4","B0C6FYKC3D","B0CSLMG2TF","B0CGGPC6G3","B0BXG8L46Y","B0CRSZGN9L","B07V34QQ3C"] |
| 6 | rootCategory | String | BSR大类节点ID | 172282 |
| 7 | rootCategoryLabel | String | 跟类目 | Electronics |
| 8 | salesRankReference | String | 排名节点ID | 541966 |
| 9 | salesRankReferenceHistory | List | 排名节点变动历史 | PairStrDto 趋势字符串数据结构 |
| 10 | nodeIdPath | String | 上架类目全路径 | 172282:541966:13896617011:565098:13896597011 |
| 11 | nodeLabelPath | String | 上架类目名称全路径 | Electronics:Computers & Accessories:Computers & Tablets:Desktops:Towers |
| 12 | productStatus | String | 商品状态 | STANDARD:everything accessibleDOWNLOADABLE:no marketplace/3rd party price dataEBOOK:no price data and sales rank accessibleINACCESSIBLE:no data accessibleINVALID:invalid or deprecated asinVARIATION_PARENT:product is a parent ASINUNKNOWN:null of status |
| 13 | availabilityAmazon | String | 亚马逊跟卖转态 | -1 |
| 14 | title | String | 标题 | iBUYPOWER Gaming PC Computer Desktop Element 9260 (Intel Core i7-9700F 3.0Ghz, NVIDIA GeForce GTX 1660 Ti 6GB, 16GB DDR4, 240GB SSD, 1TB HDD, Wi-Fi & Windows 10 Home) Black |
| 15 | brand | String | 品牌 | iBUYPOWER |
| 16 | asinUrl | String | ASIN链接 | https://www.amazon.com/dp/B07V34QQ3C |
| 17 | brandUrl | String | 品牌链接 | https://www.amazon.com/s?k=iBUYPOWER |
| 18 | salesRankUrl | String | 销售排名链接 | https://www.amazon.com/b/?node=541966 |
| 19 | imageUrl | String | 商品缩略图200*200 | https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US200_.jpg |
| 20 | zoomImageUrl | String | 商品大图600*600 | https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US600_.jpg |
| 21 | imageUrls | List | 商品图片列表 | ["https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US200_.jpg","https://images-na.ssl-images-amazon.com/images/I/61bpfnvHjqL._AC_US200_.jpg",......] |
| 22 | dimensions | String | 净尺寸 | 97 |
| 23 | weight | String | 净重量 | 1063280 |
| 24 | weightGram | Integer | 净重数值 单位统一为：克(g) | 1055398:1063252:1063280 |
| 25 | pkgDimensions | String | 打包尺寸 | 22 x 19.9 x 12.4 inches |
| 26 | pkgDimensionsSize | List | 打包尺寸 长/宽/高 单位统一为：厘米(cm) | [558,506,316] |
| 27 | pkgWeight | String | 打包重量 | 0.11 pounds |
| 28 | pkgWeightGram | Integer | 打包重量数值 单位统一为：克(g) | 13660 |
| 29 | fbaFees | Float | FBA总费用 | 26.11 |
| 30 | fbaItems | String | FBA费用项明细JSON串，包含：仓储费，仓储费税，运送打包费，运送打包费税 | "{\"pickAndPackFeeTax\":0,\"storageFee\":0,\"storageFeeTax\":0,\"pickAndPackFee\":26.11}" |
| 31 | numberOfPages | Integer | 在第几页 | -1 |
| 32 | numberOfItems | Integer | 在第几个 | 1 |
| 33 | price | List | 价格趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 34 | dealPrice | List | 成交价趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 35 | buyBox | List | 黄金购物车价格趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 36 | priceList | List | 划线价格 | 见 PairNumberDto 趋势数字数据结构 |
| 37 | buyBoxSellerIdHistory | List | 黄金购物车卖家Id历史趋势 | PairStrDto 趋势字符串数据结构 |
| 38 | bsr | List | 大类BSR排名历史趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 39 | subSalesRank | List | 小类排名趋势数据 | 见 SubRankTrendDto 小类排名趋势 |
| 40 | reviews | List | 评分数趋势数据 | 见 PairNumberDto 趋势数字数据结构 |
| 41 | rating | List | 评分值趋势数据 | 见 PairNumberDto 趋势数字数据结构 |
| 42 | sellers | List | 卖家数趋势数据 | 见 PairNumberDto 趋势数字数据结构 |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/keepa/{marketplace}/{asin}' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US&asin=B08GHW4TBS'
```

## 10. 关键词选品

### 基本信息
- **MCP Code**: `keyword_research`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/keyword-research`

### 请求参数

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

### 响应参数

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
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/keyword-research/trends`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | keyword | String | ✓ |  |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | time | String | 时间 |  |
| 2 | keywrod | String | 关键词 |  |
| 3 | keywrodCn | String | 关键词-中文 |  |
| 4 | keywrodJp | String | 关键词-日文 |  |
| 5 | search | Integer | 搜索量 |  |
| 6 | purchase | BigDecimal | 购买量 |  |
| 7 | purchaseRate | BigDecimal | 购买率 |  |
| 8 | yearlyGrowth | BigDecimal | 同比增长率 |  |
| 9 | chainGrowth | BigDecimal | 环比增长率 |  |
| 10 | threeMonthGrowth | BigDecimal | 三个月增长率 |  |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword-research/trends' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "keyword": "test"}'
```

---

## 13. 流量词统计

### 基本信息
- **MCP Code**: `traffic_keyword_stat`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/traffic/keyword-stat`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asin | String | ✓ | B07Z82895W |
| 3 | month | String |  | 查询月份，202605 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | asin | String | asin | B07Z82895W |
| 3 | keywords | Integer | 全部流量词条数 | 2685 |
| 4 | ranks | Integer | 自然流量词条数 | 1848 |
| 5 | ads | Integer | 广告流量词条数 | 1414 |
| 6 | calcTime | Long | 最近计算时间 |  |
| 7 | badgeCount | Object | 流量词类型统计 |  |
| 8 | └ns | Integer | 自然搜索词数量 | 1070 |
| 9 | └ac | Integer | AC推荐词数量 | 0 |
| 10 | └er | Integer | ER推荐词数量 | 42 |
| 11 | └fs | Integer | 4星推荐词数量 | 0 |
| 12 | └hr | Integer | HR广告词数量 | 117 |
| 13 | └sb | Integer | 品牌广告词数量 | 334 |
| 14 | └sv | Integer | 视频广告词数量 | 208 |
| 15 | └ad | Integer | SP广告词数量 | 764 |
| 16 | └ns | Integer | 自然搜索词数量 | 1070 |
| 17 | └ac | Integer | AC推荐词数量 | 0 |
| 18 | └er | Integer | ER推荐词数量 | 42 |
| 19 | └fs | Integer | 4星推荐词数量 | 0 |
| 20 | └hr | Integer | HR广告词数量 | 117 |
| 21 | └sb | Integer | 品牌广告词数量 | 334 |
| 22 | └sv | Integer | 视频广告词数量 | 208 |
| 23 | └ad | Integer | SP广告词数量 | 764 |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/traffic/keyword/stat/{marketplace}/{asin}' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US&asin=B08GHW4TBS'
```

---

## 15. 关联流量统计

### 基本信息
- **MCP Code**: `traffic_listing_stat`
- **Method**: GET
- **URL**: `https://api.sellersprite.com/v1/traffic/listing/stat/{marketplace}/{asin}`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asinList | List |  | asin列表，["B07Z82895W"] |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | asin | String | asin | B07Z82895W |
| 3 | relations | Integer | 全部流量 | 1848 |
| 4 | freeRelations | Integer | 免费流量 | 1414 |
| 5 | paidRelations | Integer | 付费流量 | 286 |
| 6 | calcTime | Long | 最近计算时间 |  |
| 7 | items | List | 统计概要 |  |
| 8 | └relation | String | 关联类型，见表2.2,忽略大小写 | vav |
| 9 | └count | Integer | 数量 | 3 |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/traffic/listing/stat/{marketplace}/{asin}' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US'
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
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asinList | List | ✓ | asin列表，["B07Z82895W"] |
| 3 | relations | List | ✓ | 关联类型，见表2.2，["vav"] |
| 4 | variations | Boolean |  | 是否查询变体，false |
| 5 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 6 | size | Integer |  | 每页条数，默认：50 |
| 7 | order | Object |  | 排序 |
| 8 | └field | String |  | 排序字段，见表2.2 |
| 9 | └desc | boolean |  | true为降序 false为升序，默认降序 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asin | String | asin | B078J8VPVW |
| 2 | brand | String | 品牌 | Pampers |
| 3 | brandUrl | String | 品牌 URL | https://www.amazon.com/s?k=HP |
| 4 | imageUrl | String | 图片 URL | https://images-na.ssl-images-amazon.com/images/I/51axlzme6aL .AC_US200.jpg |
| 5 | title | String | 商品标题 | Diapers Size 2, 186 Count - Pampers Swaddlers Disposable Baby Diapers, ONE MONTH SUPPLY |
| 6 | parent | String | 父体 | B081RGNL17 |
| 7 | nodeId | Long | 节点 id | 3741281 |
| 8 | nodeIdPath | String | 节点 id 路径字符串 | 2619525011:3741271:3741281 |
| 9 | nodeLabelPath | String | 类目 | Baby Products:Diapering:Disposable Diapers |
| 10 | bsrId | String | BSRid | office-products |
| 11 | bsr | Integer | BSR 排名 | 1 |
| 12 | units | Integer | 月销量 | 26289 |
| 13 | unitsCr | Float | 月销量增长率 | -46.3 |
| 14 | revenue | Float | 月销售额 | 1693537.4 |
| 15 | price | Float | 价格 | 64.42 |
| 16 | profit | Float | 利润率 | 63.92 |
| 17 | fba | Float | fba 运费 | 13.58 |
| 18 | ratings | Integer | 评分数 | 32004 |
| 19 | ratingsRate | Float | 留评率 | 40.57 |
| 20 | rating | Float | 评分 | 4.8 |
| 21 | ratingsCv | Integer | 月度增长数 | 10666 |
| 22 | ratingDelta | Integer | 留评数：近 30 天新增评论数 | 0 |
| 23 | availableDate | Long | 上架时间，时间戳格式 | 1454083200000 |
| 24 | fulfillment | String | 配送方式 | AMZ or FBA or FBM |
| 25 | variations | Integer | 变体数 | 7 |
| 26 | sellers | Integer | 卖家数 | 7 |
| 27 | sellerId | String | BuyBox 卖家 id | A1Y8BVAASXO4R7 |
| 28 | sellerName | String | BuyBox 卖家 | Amazon |
| 29 | sellerNation | String | BuyBox 卖家国籍 | 见表 1.5 |
| 30 | badge | Badge | 标识 | 包括了下面 5 个标识 |
| 31 | └bestSeller | String | Best Seller 标识 | Y 或者 N |
| 32 | └amazonChoice | String | amazon choice 标识 | Y 或者 N |
| 33 | └newRelease | String | release 标识 | Y 或者 N |
| 34 | └ebc | String | A+页面 | Y 或者 N |
| 35 | └video | String | 视频介绍 | Y 或者 N |
| 36 | weight | String | 重量 | 8.88 pounds |
| 37 | dimension | String | 尺寸 | 13.3 x 15.8 x 10.6 inches |
| 38 | dimensionType | String | 尺寸类型 | ST,0V |
| 39 | sku | String | sku | ["Color: Beige","Size: 47 inches"] |
| 40 | └amazonChoice | String | amazon choice 标识 | Y 或者 N |

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
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | q | String | ✓ | asin 或者 关键词，B07Z82895W |
| 3 | month | String | ✓ | 筛选日期,yyyyMM格式，202203 |
| 4 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 5 | size | Integer |  | 每页条数，默认：50最大： 100 |
| 6 | order | Object |  | 排序 |
| 7 | └field | String |  | 排序字段，见表2.4 |
| 8 | └desc | boolean |  | true为降序 false为升序，默认降序 |

### 响应参数

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

### 响应参数

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
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | date | String |  | 为空时，查最近30天，202506 |
| 3 | departments | List |  | 类目列表，["automotive","baby-products"] |
| 4 | excludeKeywords | String |  | 排除关键词，portable |
| 5 | includeKeywords | String |  | 包含关键词 |
| 6 | exactFlag | Boolean |  | 是否精确匹配 |
| 7 | minRankGrowthRate | Double |  | 最小排名增长率 |
| 8 | maxRankGrowthRate | Double |  | 最大排名增长率 |
| 9 | minSearchRank | Integer |  | 最小排名 |
| 10 | maxSearchRank | Integer |  | 最大排名 |
| 11 | minSearches | Integer |  | 最小搜索量 |
| 12 | maxSearches | Integer |  | 最大搜索量 |
| 13 | minMonopolyClickRate | Double |  | 最小点击集中度 |
| 14 | maxMonopolyClickRate | Double |  | 最大点击集中度 |
| 15 | minConversionRate | Double |  | 最小转化占比 |
| 16 | maxConversionRate | Double |  | 最大转化占比 |
| 17 | minWordCount | Integer |  | 最小单词数 |
| 18 | maxWordCount | Integer |  | 最大单词数 |
| 19 | minSPR | Integer |  | 最小SPR |
| 20 | maxSPR | Integer |  | 最大SPR |
| 21 | minTitleDensity | Integer |  | 最小标题密度 |
| 22 | maxTitleDensity | Integer |  | 最大标题密度 |
| 23 | minClicks | Integer |  | 最小点击量，1 |
| 24 | maxClicks | Integer |  | 最大点击量，10000 |
| 25 | minImpressions | Integer |  | 最小展示量，10000 |
| 26 | maxImpressions | Integer |  | 最大展示量，20000 |
| 27 | searchModel | Integer |  | 搜索模式：1：热门市场2：异动市场3：持续增长市场4：快速飙升市场5：潜力市场6：长尾市场，1 |
| 28 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 29 | size | Integer |  | 每页条数，最大15，默认：15 |
| 30 | order | Object |  | 排序 |
| 31 | └field | String |  | 排序字段，见表2.4 |
| 32 | └desc | boolean |  | true为降序 false为升序，默认降序 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | date | String | 查询日期 | 202306 |
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
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asins | List | ✓ | asin列表，最大20，B07Z82895W |
| 3 | reverseType | String | ✓ | 反查模式 W-周 M-月，W |
| 4 | date | String |  | 查询日期，按周查，格式为yyyMMdd该周最后一天，按月查询yyyyMM，周：20241109月：202411 |
| 5 | conversionType | List |  | 转化类型：E：转化优质词，S：转化平稳词，L：转化流失词，I：无效曝光词，E |
| 6 | variation | List |  | 是否查询变体asin：Y:否 N:是，Y |
| 7 | page | Integer |  | 当前页，默认1 |
| 8 | size | Integer |  | 每页显示多少条，固定50 |
| 9 | order | Object |  | 排序 |
| 10 | └field | String |  | 排序字段，见表2.6 |
| 11 | └desc | Boolean |  | 是否倒序，false |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场，见表 1.2 | US |
| 2 | keyword | String | 关键词 | phone stand for recording |
| 3 | keywordCn | String | 关键词中文翻译 | 用于录音的电话支架 |
| 4 | keywordJp | String | 关键词英文翻译 | 録音用電話スタンド |
| 5 | asin | String | 所属asin | B0D1FZW65X |
| 6 | searches | Integer | 搜索量 | 21582 |
| 7 | monopolyClickRate | Float | 点击垄断率 | 0.3 |
| 8 | cvsShareRate | Float | 转化共享率 | 0.3084 |
| 9 | searchRank | Integer | 搜索排名 | 17910 |
| 10 | searchRankGv | Integer | 月变化量 | 5343 |
| 11 | searchRankGr | Double | 月变化率 | 0.3 |
| 12 | top3ClickingRate | Float | 前三点击 | 0.0813 |
| 13 | top3ConversionRate | Float | 前三转化 | 0.2011 |
| 14 | conversionType | String | 转化类型：E：转化优质词，S：转化平稳词，L：转化流失词，I：无效曝光词 | E |

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
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/review`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | ASIN |
| 3 | starList | List |  | 评论星级，1: 一星, 2: 二星, 3: 三星, 4: 四星, 5: 五星 |
| 4 | typeList | List |  | 评论类型，1：图片评论, 2：视频评论, 3：VP评论, 4：vine评论 |
| 5 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 6 | size | Integer |  | 每页条数，最大10，默认：5 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | author | String | 用户 |  |
| 2 | title | String | 标题 |  |
| 3 | content | String | 评论内容 |  |
| 4 | date | Long | 日期（时间戳） | 1772380800000 |
| 5 | star | Integer | 星级 |  |
| 6 | authorLabels | List | 评论人标签 |  |
| 7 | skus | List | sku信息 |  |
| 8 | images | List | 图片链接 |  |
| 9 | videos | List | 视频链接 |  |
| 10 | likes | Integer | 点赞数 |  |
| 11 | image | Boolean | 是否图片评论 |  |
| 12 | video | Boolean | 是否视频评论 |  |
| 13 | verified | Boolean | 是否实际购买评论 |  |
| 14 | vine | Boolean | 是否特邀评论 |  |
| 15 | free | Boolean | 是否免费评论 |  |
| 16 | experience | Boolean | 是否抢先体验评论 |  |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/review' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

---

## 29. 选市场列表

### 基本信息
- **MCP Code**: `market_research`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/research`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topNum | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，default: 3 |
| 5 | nodeIdPath | String |  | 类目，172282:281407 |
| 6 | departmentKeyword | String |  | 类目关键字，Electronics:Accessories & Supplies |
| 7 | minAvgUnits | Integer |  | 最低月均销量，100 |
| 8 | maxAvgUnits | Integer |  | 最高均月销量，10000 |
| 9 | minAvgRevenue | Float |  | 最低月均销售额，100 |
| 10 | maxAvgRevenue | Float |  | 最高月均销售额，900 |
| 11 | minAvgRatings | Integer |  | 最低平均评分数，100 |
| 12 | maxAvgRatings | Integer |  | 最高平均评分数，500 |
| 13 | minAvgRating | Float |  | 最低平均评分值，2.5 |
| 14 | maxAvgRating | Float |  | 最高平均评分值，3 |
| 15 | minAvgBsr | Integer |  | 最低平均BSR排名，50 |
| 16 | maxAvgBsr | Integer |  | 最高平均BSR排名，100 |
| 17 | minAvgPrice | Float |  | 最低平均价格，30 |
| 18 | maxAvgPrice | Float |  | 最高平均价格，50 |
| 19 | minWeight | Float |  | 最低重量，30 |
| 20 | maxWeight | Float |  | 最高重量，60 |
| 21 | minVolume | Float |  | 最低体积，20 |
| 22 | maxVolume | Float |  | 最高体积，50 |
| 23 | minAvgProfit | Float |  | 最低平均毛利率，20 |
| 24 | maxAvgProfit | Float |  | 最高平均毛利率，70 |
| 25 | minTopAvgUnits | Integer |  | 最低头部月均销量，200 |
| 26 | maxTopAvgUnits | Integer |  | 最高头部均月销量，300 |
| 27 | minTopAvgRevenue | Float |  | 最低头部月均销售额，2000 |
| 28 | maxTopAvgRevenue | Float |  | 最高头部月均销售额，3000 |
| 29 | minTopAvgBsr | Integer |  | 最低头部平均BSR，68 |
| 30 | maxTopAvgBsr | Integer |  | 最高头部平均BSR，998 |
| 31 | minGoodsCount | Integer |  | 最低商品数量，40 |
| 32 | maxGoodsCount | Integer |  | 最高商品数量，90 |
| 33 | minBrands | Integer |  | 最小品牌数量，10 |
| 34 | maxBrands | Integer |  | 最大品牌数量，20 |
| 35 | minSellers | Integer |  | 最小卖家数量，6 |
| 36 | maxSellers | Integer |  | 最大卖家数量，10 |
| 37 | minAvgSellers | Float |  | 最小平均卖家数量，4.4 |
| 38 | maxAvgSellers | Float |  | 最大平均卖家数量，10.4 |
| 39 | minGoodsCrn | Float |  | 最小商品集中度，45 |
| 40 | maxGoodsCrn | Float |  | 最大商品集中度，55 |
| 41 | minBrandCrn | Float |  | 最小品牌集中度，45 |
| 42 | maxBrandCrn | Float |  | 最大品牌集中度，55 |
| 43 | maxSellerCrn | Float |  | 最小卖家集中度，45 |
| 44 | minSellerCrn | Float |  | 最大卖家集中度，55 |
| 45 | minEbcProportion | Float |  | 最小A+数量占比，34 |
| 46 | maxEbcProportion | Float |  | 最大A+数量占比，54 |
| 47 | minFbaProportion | Float |  | 最小FBA占比，34 |
| 48 | maxFbaProportion | Float |  | 最大FBA占比，54 |
| 49 | minFbmProportion | Float |  | 最小FBM占比，34 |
| 50 | maxFbmProportion | Float |  | 最大FBM占比，54 |
| 51 | minAmazonSelfProportion | Float |  | 最小Amazon自营占比，34 |
| 52 | maxAmazonSelfProportion | Float |  | 最大Amazon自营占比，56 |
| 53 | sellerLocation | String |  | 卖家所属地，见表1.3，US,GB |
| 54 | minNewProportion | Float |  | 最小新品数量占比，34 |
| 55 | maxNewProportion | Float |  | 最大新品数量占比，56 |
| 56 | minNewCount | Integer |  | 最小新品数量，4 |
| 57 | maxNewCount | Integer |  | 最大新品数量，20 |
| 58 | minNewAvgRatings | Integer |  | 最小新品平均评分数，23 |
| 59 | maxNewAvgRatings | Integer |  | 最大新品平均评分数，554 |
| 60 | minNewAvgPrice | Float |  | 最小新品平均价格，34 |
| 61 | maxNewAvgPrice | Float |  | 最大新品平均价格，45 |
| 62 | minNewAvgRating | Float |  | 最小新品平均星级，4 |
| 63 | maxNewAvgRating | Float |  | 最大新品平均星级，4.5 |
| 64 | minNewAvgUnits | Float |  | 最低新品月均销量，400 |
| 65 | maxNewAvgUnits | Float |  | 最高新品月均销量，800 |
| 66 | minNewAvgRevenue | Float |  | 最低新品月均销售额，900 |
| 67 | maxNewAvgRevenue | Float |  | 最高新品月均销售额，2000 |
| 68 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 69 | size | Integer |  | 每页条数，默认：50，最大：200 |
| 70 | order | Object |  | 排序 |
| 71 | └field | String |  | 排序字段，见表1.6 |
| 72 | └desc | boolean |  | true为降序 false为升序，默认降序 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场标志 | US |
| 2 | currency | String | 该市场的货币类型 | USD |
| 3 | nodeId | String | 节点ID | 3732981 |
| 4 | nodeLabelName | String | 节点名称 | Mattresses |
| 5 | nodeIdPath | String | 节点ID路径 | 1055398:1063306:1063308:3732961:3732981 |
| 6 | nodeLabelPath | String | 节点名称路径 | Home & Kitchen:Furniture:Bedroom Furniture:Mattresses & Box Springs:Mattresses |
| 7 | nodeLabelLocale | String | 节点名称翻译 | 床垫 |
| 8 | nodeLabelPathLocale | String | 节点名称路径翻译 | 家居用品 厨房:家具:家具卧室:床垫:床垫 |
| 9 | totalProducts | Integer | 商品总数 | 1000 |
| 10 | ranking | Integer | 排名 | 1 |
| 11 | topProducts | Integer | 样本数量 | 100 |
| 12 | brands | Integer | 品牌数量 | 34 |
| 13 | sellers | Integer | 卖家数量 | 60 |
| 14 | totalUnits | Integer | 月总销量 | 539009 |
| 15 | totalRevenue | Float | 月总销售额 | 1.7995061038E8 |
| 16 | avgUnits | Integer | 月均销量 | 5390 |
| 17 | avgRevenue | Float | 月均销售额 | 1799506 |
| 18 | avgPrice | Float | 平均价格 | 296.11 |
| 19 | avgRatings | Integer | 平均评分数 | 14591 |
| 20 | avgRating | Float | 平均评分值 | 4.5 |
| 21 | avgBsr | Integer | 平均BSR | 198077 |
| 22 | baseAvgVolume | Float | 平均体积(cm³) | 529430.46 |
| 23 | avgVolume | Float | 平均体积(in³) | 32307.87 |
| 24 | baseAvgWeight | Float | 平均重量(g) | 35301.19 |
| 25 | avgWeight | Float | 平均重量(pound) | 77.8259 |
| 26 | avgProfit | Float | 平均利润率 | 68.76 |
| 27 | avgSellers | Float | 平均卖家数 | 3.3 |
| 28 | ebcProportion | Float | A+商品占比,百分比 | 80 |
| 29 | amazonSelfProportion | Float | Amazon自营占比,百分比 | 55 |
| 30 | fbaProportion | Float | FBA占比,百分比 | 22 |
| 31 | fbmProportion | Float | FBM占比,百分比 | 14 |
| 32 | sellerNation | String | 最多卖家归属地 code，见表1.3 | US |
| 33 | sellerNationLabel | String | 最多卖家归属地 label | 美国 |
| 34 | sellerProportion | Float | 最多卖家归属地 占比 | 59.3 |
| 35 | top10Images | List | 前10商品的图片 |  |
| 36 | └asin | String | asin | B01IU6RJYA |
| 37 | └image | String | asin图片链接 | https://images-na.ssl-images-amazon.com/images/I/51+5VVLcXSL._AC_US200_.jpg |
| 38 | returnRatio | Float | 退货率 | 3.51 |
| 39 | avgReturnRatio | Float | 退货率类目平均值 | 5.54 |
| 40 | searchToPurchaseRatio | Float | 搜索购买比,千分比 | 0.94926 |

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
- **URL**: `https://api.sellersprite.com/v1/market/statistics`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场标志 | US |
| 2 | currency | String | 该市场的货币类型 | USD |
| 3 | nodeIdPath | String | 节点ID路径 | 1064954:1069242:1069784:1069820:1069838:1069828 |
| 4 | nodeLabelPath | String | 节点名称路径 | Office Products:Office & School Supplies:Writing & Correction Supplies:Pens & Refills:Rollerball Pens:Gel Ink Rollerball Pens |
| 5 | nodeLabelLocale | String | 节点名称翻译 | 办公产品:办公室:写作:钢笔:滚珠笔:中性笔 |
| 6 | countryCode | String | 国家二简码 | US |
| 7 | totalProducts | Integer | 商品总数 | 5127 |
| 8 | products | Integer | 样品商品数 | 100 |
| 9 | brands | Integer | 品牌数 | 4 |
| 10 | sellers | Integer | 卖家数 | 58 |
| 11 | avgBsr | Integer | 平均BSR | 41970 |
| 12 | baseAvgVolume | Float | 平均体积(cm³) | 819942.68 |
| 13 | avgVolume | Float | 平均体积(in³) | 50035.97 |
| 14 | baseAvgWeight | Float | 平均重量(g) | 2460.95 |
| 15 | avgWeight | Float | 平均重量(pound) | 5.4255 |
| 16 | avgProfit | Float | 平均利润率 | 66.03 |
| 17 | avgUnits | Integer | 月均销量 | 26255 |
| 18 | avgRevenue | Float | 月均销售额 | 344369 |
| 19 | avgPrice | Float | 平均价格 | 13.91 |
| 20 | avgRatingsCv | Integer | 月评论平均增长数 | 0 |
| 21 | avgRatings | Integer | 平均评分数 | 19071 |
| 22 | avgRating | Float | 平均星级 | 4.7 |
| 23 | avgSellers | Float | 平均卖家数 | 5.2 |
| 24 | hlProducts | Integer | 头部Listing前N名商品样本数 | 5 |
| 25 | hlAvgBsr | Integer | 头部Listing前N名商品平均BSR | 13126 |
| 26 | hlAvgUnits | Integer | 头部Listing前N名商品月均销量 | 1123 |
| 27 | hlAvgRevenue | Float | 头部Listing前N名商品月均销售额 | 12342.85 |
| 28 | hlAvgPrice | Float | 头部Listing前N名商品平均价格 | 11.77 |
| 29 | hlAvgRatingsCv | Integer | 头部Listing前N名商品月评论平均增长数 | 0 |
| 30 | hlAvgRatings | Integer | 头部Listing前N名商品平均评论数 | 2794 |
| 31 | hlAvgRating | Float | 头部Listing前N名商品平均星级 | 4.7 |
| 32 | newProducts | Integer | 新品数量 | 67 |
| 33 | newProductProportion | Float | 新品数量占比 | 67 |
| 34 | newAvgPrice | Float | 新品平均价格 | 14.14 |
| 35 | newAvgRatings | Integer | 新品平均评分数 | 24295 |
| 36 | minNewRatings | Integer | 最低新品评分数 | 24 |
| 37 | maxNewRatings | Integer | 最高新品评分数 | 6432 |
| 38 | newAvgRating | Float | 新品平均星级 | 4.7 |
| 39 | newAvgUnits | Integer | 新品月均销量 | 26425 |
| 40 | newAvgRevenue | Float | 新品月均销售额 | 350209.91 |
| 41 | firstShelfDate | String | 商品首次上架日期 | 2014-10-30 |
| 42 | lastShelfDate | String | 商品最新上架日期 | 2021-04-28 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/statistics' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 31. 选市场-商品集中度

### 基本信息
- **MCP Code**: `market_product_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/goods`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | asins | List |  | 过滤asin，["B00P19MFYE"] |
| 4 | topN | Integer |  | 头部Listing数量，10 |
| 5 | newProduct | Integer |  | 新品定义，6 |
| 6 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | title | String | 标题 | Pilot G2, Dr. Grip Gel/Ltd, ExecuGel G6, Q7 Rollerball Gel Ink Pen Refills, 0.7mm, Fine Point, Black Ink, 3 Packs of 2 |
| 2 | asin | String | asin | B00P19MFYE |
| 3 | asinUrl | String | asin链接 | https://www.amazon.com/dp/B00P19MFYE |
| 4 | imageUrl | String | 图片链接 | https://images-na.ssl-images-amazon.com/images/I/51hxvoxGnjL._AC_US200_.jpg |
| 5 | ranking | Integer | 排名 | 1 |
| 6 | brand | String | 品牌 | PILOT |
| 7 | sellerName | String | 卖家名称 | JA Wholesale LLC |
| 8 | sellerType | String | 卖家类型 | FBA |
| 9 | price | Float | 价格 | 6.19 |
| 10 | shelfDate | String | 上架时间 | 2014-10-30 |
| 11 | ratings | Integer | 评分数 | 5695 |
| 12 | reviews | Integer | 评论数 | 133 |
| 13 | rating | Float | 评论值 | 4.8 |
| 14 | newFlag | Integer | 是否新品 1新品，0非新品 | 0 |
| 15 | totalUnits | Integer | 总销量 | 2515 |
| 16 | totalRevenue | Float | 总销额 | 18837.35 |
| 17 | totalUnitsRatio | Float | 总销量占比 | 0.4478 |
| 18 | totalRevenueRatio | Float | 总销额占比 | 0.3052 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/goods' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 32. 选市场-品牌集中度

### 基本信息
- **MCP Code**: `market_brand_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/brand`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | brand | String | 品牌名称 | PILOT |
| 2 | ranking | Integer | 排名 | 1 |
| 3 | asins | List | 包含的商品ASIN集合 | ["B00P19MFYE"] |
| 4 | products | Integer | 商品数量，包含新品 | 4 |
| 5 | newProducts | Integer | 新品数量 | 1 |
| 6 | newUnits | Integer | 新品销量 | 45 |
| 7 | newRevenue | Float | 新品销售额 | 2342 |
| 8 | newUnitsRatio | Float | 新品销量占比 | 4.3 |
| 9 | newRevenueRatio | Float | 新品销售额占比 | 4 |
| 10 | avgPrice | Float | 平均价格 | 6.19 |
| 11 | ratings | Integer | 评分数 | 5695 |
| 12 | rating | Float | 评分值 | 4.8 |
| 13 | reviews | Integer | 评论数 | 234 |
| 14 | totalUnits | Integer | 总销量 | 32342 |
| 15 | totalRevenue | Float | 总销额 | 18837.35 |
| 16 | totalUnitsRatio | Float | 总销量占比 | 0.4478 |
| 17 | totalRevenueRatio | Float | 总销额占比 | 0.3052 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/brand' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 33. 选市场-卖家集中度

### 基本信息
- **MCP Code**: `market_seller_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | name | String | 卖家名称 | JA Wholesale LLC |
| 2 | ranking | Integer | 排名 | 1 |
| 3 | asinSet | List | 包含的商品ASIN集合 | ["B00P19MFYE"] |
| 4 | products | Integer | 商品数量，包含新品 | 4 |
| 5 | newProducts | Integer | 新品数量 | 1 |
| 6 | newUnits | Integer | 新品销量 | 45 |
| 7 | newRevenue | Float | 新品销售额 | 2342 |
| 8 | newUnitsRatio | Float | 新品销量占比 | 4.3 |
| 9 | newRevenueRatio | Float | 新品销售额占比 | 4 |
| 10 | avgPrice | Float | 平均价格 | 6.19 |
| 11 | ratings | Integer | 评分数 | 5695 |
| 12 | rating | Float | 评分值 | 4.8 |
| 13 | reviews | Integer | 评论数 | 234 |
| 14 | totalUnits | Integer | 总销量 | 32342 |
| 15 | totalRevenue | Float | 总销额 | 18837.35 |
| 16 | totalUnitsRatio | Float | 总销量占比 | 0.4478 |
| 17 | totalRevenueRatio | Float | 总销额占比 | 0.3052 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/seller' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 34. 选市场-卖家类型分布

### 基本信息
- **MCP Code**: `market_seller_type_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller/type`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | Amazon自营 |
| 2 | asinNum | Integer | ASIN数量 | 4 |
| 3 | asinRatio | Float | ASIN数量占比 | 0.03 |
| 4 | units | Integer | 月销量 | 79875 |
| 5 | unitsRatio | Float | 月销量占比 | 0.0345 |
| 6 | ratings | Integer | 评分数 | 6607 |
| 7 | rating | Float | 评分值 | 4.7 |
| 8 | productNum | Integer | 商品总数 | 3 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/seller/type' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 35. 选市场-卖家所属地分布

### 基本信息
- **MCP Code**: `market_seller_country_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/seller/location`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 美国 |
| 2 | country | String | 国家 | 美国 |
| 3 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 4 | products | Integer | 产品数 | 3 |
| 5 | revenue | Float | 销售额 | 47492.83 |
| 6 | units | Integer | 销量 | 4107 |
| 7 | unitsRatio | Float | 销量占比 | 0.7313 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/seller/location' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 36. 选市场-商品需求趋势

### 基本信息
- **MCP Code**: `market_product_demand_trend`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/performance`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场 id，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，最早查询时间为2021年7月份，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asinCount | String | asin数量 | 22187 |
| 2 | returnRatio | String | 退货率，百分比 | 1.38 |
| 3 | searchToPurchaseRatio | List | 搜索购买比，千分比 | 3.17875 |
| 4 | avgReturnRatio | Integer | 类目平均退货率，百分比 | 2.72 |
| 5 | avgSearchToPurchaseRatio | Float | 类目平均搜索购买比，千分比 | 2.6 |
| 6 | items | List | 月浏览趋势 |  |
| 7 | └date | String | 时间，yyyy-MM-dd格式 | 2022-09-10 |
| 8 | └glanceViews | Integer | 浏览量 | 2 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/performance' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

## 37. 选市场-上架时间分布

### 基本信息
- **MCP Code**: `market_listing_date_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/shelf/time`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 3年以上 |
| 2 | shelfTime | String | 上架时间 | 3年以上 |
| 3 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 4 | products | Integer | 产品数 | B07Z82895W |
| 5 | revenue | Float | 销售额 | 40846.76 |
| 6 | units | Integer | 销量 | 4684 |
| 7 | unitsRatio | Float | 销量占比 | 0.834 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/shelf/time' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 38. 选市场-上架趋势分布

### 基本信息
- **MCP Code**: `market_listing_trend_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/shelf/trend`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String |  | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String |  | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 2014 |
| 2 | year | String | 年份，yyyy格式 | 2014 |
| 3 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 4 | products | Integer | 产品数 | 1 |
| 5 | revenue | Float | 销售额 | 2515 |
| 6 | units | Integer | 销量 | 18837.35 |
| 7 | unitsRatio | Float | 销量占比 | 0.4478 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/shelf/trend' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
```

---

## 39. 选市场-评分数分布

### 基本信息
- **MCP Code**: `market_ratings_count_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ratings`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 500以上 |
| 2 | asins | List | 包含的asin列表 | 5 |
| 3 | products | Integer | 产品数 | ["B00P19MFYE"] |
| 4 | revenue | Float | 销售额 | 61714.24 |
| 5 | units | Integer | 销量 | 5616 |
| 6 | unitsRatio | Float | 销量占比 | 0.9743 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/ratings' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 40. 选市场-评分值分布

### 基本信息
- **MCP Code**: `market_rating_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/rating`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 4.5以上 |
| 2 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 3 | products | Integer | 产品数 | 5 |
| 4 | revenue | Float | 销售额 | 59934.22 |
| 5 | units | Integer | 销量 | 5418 |
| 6 | unitsRatio | Float | 销量占比 | 0.9647 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/rating' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 41. 选市场-价格分布

### 基本信息
- **MCP Code**: `market_price_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/price`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 5-10 |
| 2 | asins | List | 包含的asin列表 | ["B00P19MFYE"] |
| 3 | products | Integer | 产品数 | 3 |
| 4 | revenue | Float | 销售额 | 33058.76 |
| 5 | units | Integer | 销量 | 4024 |
| 6 | unitsRatio | Float | 销量占比 | 0.7165 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/price' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
```

---

## 42. 选市场-A+视频分布

### 基本信息
- **MCP Code**: `market_ebc_distribution`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/ebc`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | label | String | 类型说明 | 有A+有视频 |
| 2 | products | Integer | 产品数 | 1 |
| 3 | productsRatio | Float | 类目名称产品占比 | 20 |
| 4 | units | Integer | 销量 | 1311 |
| 5 | unitsRatio | Float | 销量占比 | 23.34 |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/market/ebc' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "nodeIdPath": "2619525011"}'
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

### 响应参数

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
- **URL**: `https://api.sellersprite.com/v1/aba/research/trends`

### 请求参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | keyword | String | ✓ | 关键词 |
| 3 | timeGranularity | String |  | 时间粒度，W：周，M：月 |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | date | Date | 日期 |  |
| 2 | rank | String | ABA排名 |  |
| 3 | searches | String | 搜索量 |  |
| 4 | label | Integer | 日期标签 |  |

### 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/aba/research/trends' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace": "US", "keyword": "test", "timeGranularity":"M"}'
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
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | keyword | String |  | 关键字，iphone stand |
| 3 | googleProp | String |  | 类别，web:google网页搜索shoppingCart:google购物搜索 |
| 4 | monthly | boolean |  | 按照月份，false（默认值） |

### 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场，见表 1.2 | US |
| 2 | keyword | String | 关键字 | phone stand |
| 3 | link | String | google trend链接 |  |
| 4 | items | List | 明细 |  |
| 5 | └time | Long | 时间戳 | 1555804800000 |
| 6 | └value | Integer | 值 | 2 |

### 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/google/trends' \
  -H 'secret-key: Your Secret' \
  -G -d 'marketplace=US'
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
