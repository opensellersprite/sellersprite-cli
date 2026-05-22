# market_product_concentration

## 描述

用于分析指定 Amazon 市场类目节点下的商品集中度情况。

通过传入对应站点（国家编码）、类目节点路径及筛选条件，返回该类目中头部 Listing 的
排名、价格、品牌、卖家类型、上架时间、评分、评论数、销量、销售额
以及对应的销量占比与销额占比等核心指标。

头部商品的总销量T，占样本范围内商品总销量A的比例，即商品集中度=T/A
头部商品在整个市场中占比越大，说明头部商品垄断越明显，市场竞争度越大

可用于判断：
- 类目内销量与销售额是否高度集中
- 头部商品的市场主导程度
- 市场竞争强度与进入机会
- 新品在该类目下的潜在生存空间

## MCP 调用名称

`mcp__sellersprite__market_product_concentration`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | asins | List |  | 过滤asin，["B00P19MFYE"] |
| 4 | topN | Integer |  | 头部Listing数量，10 |
| 5 | newProduct | Integer |  | 新品定义，6 |
| 6 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_product_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/product-concentration`

## 响应参数

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

## 请求示例

```json
{
  "request": {
    "asins": [
      "B0XXX1",
      "B0XXX2"
    ],
    "marketplace": "US",
    "month": "202604",
    "newProduct": 6,
    "nodeIdPath": "2619525011:3741271",
    "topN": 10
  }
}
```

