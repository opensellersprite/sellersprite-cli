# competitor_lookup

## 描述

查询 Amazon 商品列表数据，支持按市场、月份、品牌、卖家、ASIN、类目、关键词等条件筛选，
并返回商品的销量、销售额、BSR、价格、评分、卖家、类目、变体等核心运营指标。

适用于以下场景：
- 选品分析（找高销量 / 高增长商品）
- 类目或关键词下的商品调研
- 竞品监控（品牌 / 卖家 / ASIN 对比）
- 市场趋势与榜单分析

## MCP 调用名称

`mcp__sellersprite__competitor_lookup`

## 参数

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

## 基本信息

- **MCP Code**: `competitor_lookup`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/product/competitor-lookup`

## 响应参数

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

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/product/competitor-lookup' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","brand":"apple","variation":"N","page":1,"size":1}'
```

