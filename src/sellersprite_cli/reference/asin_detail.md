# asin_detail

## 描述

查询 Amazon 单个商品（ASIN）的完整详情信息。
返回商品的基础信息、类目结构、价格与促销、
评分与评论、卖家与配送方式、变体信息、
Listing 页面质量得分以及 Best Seller、Amazon's Choice 等运营标识。

适用于以下场景：
- 单 ASIN 商品深度分析
- 竞品拆解与对比
- 商品进入可行性评估
- 商品详情页质量与风险判断

## MCP 调用名称

`mcp__sellersprite__asin_detail`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |

## 基本信息

- **MCP Code**: `asin_detail`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}`

## 响应参数

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

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

