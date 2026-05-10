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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点 |
| `asin` | string | 是 |  |

## 基本信息

- **MCP Code**: `asin_detail`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}`

## 响应参数

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

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

