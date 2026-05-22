# market_research

## 描述

Amazon 类目市场分析工具，用于从“类目维度”评估市场规模、
竞争强度、盈利空间以及新品进入可行性。

该工具回答的核心问题包括：
- 这个类目整体有多大？是否有足够销量与销售额？
- 类目是否被头部商品或头部品牌高度垄断？
- 平均价格、利润率是否具备盈利空间？
- FBA / FBM / Amazon 自营结构是否健康？
- 新品在该类目中是否仍有成长机会？

适用于以下场景：
- 选品前的类目筛选与市场可行性判断
- 新品是否适合进入该类目
- 类目竞争激烈程度评估
- 对比多个类目，寻找更优的切入市场

## MCP 调用名称

`mcp__sellersprite__market_research`

## 参数

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

## 基本信息

- **MCP Code**: `market_research`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/market/research`

## 响应参数

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

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "month": "202604",
    "newProduct": 6,
    "nodeIdPath": "2619525011:3741271",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "size": 20,
    "topNum": 10
  }
}
```

