# asin_detail_with_coupon_trend

## 描述

查询指定 ASIN 在 Amazon 指定市场下的完整商品详情信息，
包括基础属性、类目、评分、卖家、价格、配送方式等，
并同时返回该 ASIN 的优惠（Coupon）价格趋势数据，
用于分析真实成交价变化及促销策略。

## MCP 调用名称

`mcp__sellersprite__asin_detail_with_coupon_trend`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |

## 基本信息

- **MCP Code**: `asin_detail_with_coupon_trend`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/with-coupon-trend`

## 响应参数

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

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

