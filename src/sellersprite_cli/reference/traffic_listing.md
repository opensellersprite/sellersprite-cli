# traffic_listing

## 描述

查询指定 ASIN 在 Amazon 站内的关联商品列表，用于分析竞品结构与关联关系。

该工具基于 Amazon 站内关系模型，返回与目标 ASIN 存在
关联、竞品或同类关系的商品数据，包括销量、BSR、价格、
利润率、评分、卖家结构、变体信息等核心指标。

适用于以下场景：
- 查找目标 ASIN 的直接竞品与强关联商品
- 分析某个市场的头部商品结构与集中度
- 判断新品进入时将面对的主要对手
- 分析变体数量、卖家数量、品牌垄断程度

## MCP 调用名称

`mcp__sellersprite__traffic_listing`

## 参数

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

## 基本信息

- **MCP Code**: `traffic_listing`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/listing/page`

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

## 请求示例

```json
{
  "request": {
    "asinList": [
      "B0XXX1",
      "B0XXX2"
    ],
    "marketplace": "US",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "relations": [
      "similar"
    ],
    "size": 20,
    "variations": false
  }
}
```

