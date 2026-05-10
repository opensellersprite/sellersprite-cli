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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `asins` | array |  | asins, 最多只支持40个，如果超过40个, 需要拆分多次请求 |
| `brand` | string |  | brand name |
| `keyword` | string |  | 关键字，基于商品标题进行匹配 |
| `keywordEqual` | boolean |  |  |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `matchType` | integer |  | 匹配方式, 默认: 2 可选值(必须严格使用下列数字值之一): 1: 词组匹配 2: 模糊匹配 3: 精准匹配  禁止使用未列出的值。  |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `nodeIdPath` | string |  | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `nodeIdPathEqual` | boolean |  | 类目节点查询方式 |
| `order` | object |  | 排序 |
| `page` | integer |  | 页码 |
| `sellerName` | string |  | seller name |
| `size` | integer |  | 每页条数 |
| `variation` | string |  | 是否查询变体ASIN，如果没有明确指定则要设置成: Y 可选值(仅填写字段名): - Y: exclude - N: include  |

## 基本信息

- **MCP Code**: `competitor_lookup`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/product/competitor-lookup`

## 响应参数

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

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/product/competitor-lookup' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","brand":"apple","variation":"N","page":1,"size":1}'
```

