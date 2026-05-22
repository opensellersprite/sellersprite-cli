# product_research

## 描述

高级商品筛选工具，用于在 Amazon 指定市场中，
根据关键词、品牌、卖家、类目、价格区间、销量、销售额、
BSR 排名及增长、评分、评论数、利润率、配送方式等多维条件，
精准筛选符合特定商业条件的商品列表。

适用于以下场景：
- 爆品 / 潜力品筛选
- 蓝海机会挖掘
- 条件化选品（价格、利润、销量、竞争度）
- 按规则扫描整个类目或关键词市场

## MCP 调用名称

`mcp__sellersprite__product_research`

## 参数

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

## 基本信息

- **MCP Code**: `product_research`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/product/research`

## 响应参数

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

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/product/research' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","minPrice":100,"maxPrice":101,"variation":"N","page":1,"size":1}'
```

