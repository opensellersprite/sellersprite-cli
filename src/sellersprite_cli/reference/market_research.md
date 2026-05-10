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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `departmentKeyword` | string |  | 类目关键字 |
| `fulfillment` | string |  | 配送方式，AMZ/FBA/FBM |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `maxAmazonSelfProportion` | number |  | 最大Amazon自营占比 |
| `maxAvgBsr` | integer |  | 最高平均BSR排名 |
| `maxBrandConcentration` | number |  | 最大品牌集中度 |
| `maxNewProductRatio` | number |  | 最大新品占比 |
| `maxAvgPrice` | number |  | 最高平均价格 |
| `maxPrice` | number |  | 最高价格 |
| `maxRating` | number |  | 最高评分值 |
| `maxRatings` | integer |  | 最高评分数 |
| `maxRevenue` | number |  | 最高月均销售额 |
| `maxAvgProfit` | number |  | 最高平均毛利率 |
| `maxAvgRating` | number |  | 最高平均评分值 |
| `maxAvgRatings` | integer |  | 最高平均评分数 |
| `maxAvgRevenue` | number |  | 最高月均销售额 |
| `maxAvgSellers` | number |  | 最大平均卖家数量 |
| `maxAvgUnits` | integer |  | 最高均月销量 |
| `maxUnits` | integer |  | 最高月销量 |
| `maxBrandCrn` | number |  | 最大品牌集中度 |
| `maxBrands` | integer |  | 最大品牌数量 |
| `maxEbcProportion` | number |  | 最大A+数量占比 |
| `maxFbaProportion` | number |  | 最大FBA占比 |
| `maxFbmProportion` | number |  | 最大FBM占比 |
| `maxGoodsCount` | integer |  | 最高商品数量 |
| `maxGoodsCrn` | number |  | 最大商品集中度 |
| `maxNewAvgPrice` | number |  | 最大新品平均价格 |
| `maxNewAvgRating` | number |  | 最大新品平均星级 |
| `maxNewAvgRatings` | integer |  | 最大新品平均评分数 |
| `maxNewAvgRevenue` | number |  | 最高新品月均销售额 |
| `maxNewAvgUnits` | number |  | 最高新品月均销量 |
| `maxNewCount` | integer |  | 最大新品数量 |
| `maxNewProportion` | number |  | 最大新品数量占比 |
| `maxSellerCrn` | number |  | 最小卖家集中度 |
| `maxSellers` | integer |  | 最大卖家数量 |
| `maxTopAvgBsr` | integer |  | 最高头部平均BSR |
| `maxTopAvgRevenue` | number |  | 最高头部月均销售额 |
| `maxTopAvgUnits` | integer |  | 最高头部均月销量 |
| `maxVolume` | number |  | 最高体积 |
| `maxWeight` | number |  | 最高重量 |
| `minAmazonSelfProportion` | number |  | 最小Amazon自营占比 |
| `minAvgBsr` | integer |  | 最低平均BSR排名 |
| `minBrandConcentration` | number |  | 最小品牌集中度 |
| `minNewProductRatio` | number |  | 最小新品占比 |
| `minAvgPrice` | number |  | 最低平均价格 |
| `minPrice` | number |  | 最低价格 |
| `minRating` | number |  | 最低评分值 |
| `minRatings` | integer |  | 最低评分数 |
| `minRevenue` | number |  | 最低月均销售额 |
| `minAvgProfit` | number |  | 最低平均毛利率 |
| `minAvgRating` | number |  | 最低平均评分值 |
| `minAvgRatings` | integer |  | 最低平均评分数 |
| `minAvgRevenue` | number |  | 最低月均销售额 |
| `minAvgSellers` | number |  | 最小平均卖家数量 |
| `minAvgUnits` | integer |  | 最低月均销量 |
| `minUnits` | integer |  | 最低月销量 |
| `minBrandCrn` | number |  | 最小品牌集中度 |
| `minBrands` | integer |  | 最小品牌数量 |
| `minEbcProportion` | number |  | 最小A+数量占比 |
| `minFbaProportion` | number |  | 最小FBA占比 |
| `minFbmProportion` | number |  | 最小FBM占比 |
| `minGoodsCount` | integer |  | 最低商品数量 |
| `minGoodsCrn` | number |  | 最小商品集中度 |
| `minNewAvgPrice` | number |  | 最小新品平均价格 |
| `minNewAvgRating` | number |  | 最小新品平均星级 |
| `minNewAvgRatings` | integer |  | 最小新品平均评分数 |
| `minNewAvgRevenue` | number |  | 最低新品月均销售额 |
| `minNewAvgUnits` | number |  | 最低新品月均销量 |
| `minNewCount` | integer |  | 最小新品数量 |
| `minNewProportion` | number |  | 最小新品数量占比 |
| `minSellerCrn` | number |  | 最大卖家集中度 |
| `minSellers` | integer |  | 最小卖家数量 |
| `minTopAvgBsr` | integer |  | 最低头部平均BSR |
| `minTopAvgRevenue` | number |  | 最低头部月均销售额 |
| `minTopAvgUnits` | integer |  | 最低头部月均销量 |
| `minVolume` | number |  | 最低体积 |
| `minWeight` | number |  | 最低重量 |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string |  | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `nodeIdPathEqual` | boolean |  | true为类目精确查询 false为查询当前及子类目 |
| `order` | object |  | 排序 |
| `page` | integer |  | 页码 |
| `sellerLocation` | string |  | 卖家所属地，见表1.3 |
| `size` | integer |  | 每页条数 |
| `topNum` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_research`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/research`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|------|
| nodeIdPath | String | 类目路径 |
| nodeLabelPath | String | 类目标签 |
| totalProducts | Integer | 商品总数 |
| avgPrice | Float | 平均价格 |
| avgRating | Float | 平均评分 |
| avgRatings | Float | 平均评分数 |
| avgUnits | Integer | 平均销量 |
| avgRevenue | Float | 平均销售额 |
| newProductRatio | Float | 新品占比 |
| brandConcentration | Float | 品牌集中度 |
| topBrands | List | 头部品牌 |
| topSellers | List | 头部卖家 |

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

