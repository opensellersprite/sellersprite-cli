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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `availableMonth` | integer |  | 上架月份 |
| `maxAmzUnit` | integer |  | 最大子体月销量 |
| `minAmzUnit` | integer |  | 最小子体月销量 |
| `badgeAC` | string |  | 是否有热销标识 Amazon's Choice |
| `badgeBS` | string |  | 是否有热销标识 Best Seller |
| `badgeNR` | string |  | 是否有新品标识 New Release |
| `dimensionType` | string |  | 尺寸类型集合,逗号分隔，默认不限制 |
| `excludeBrands` | string |  | 排除品牌 |
| `excludeKeywords` | string |  | 排除的关键字 |
| `excludeSellers` | string |  | 排除卖家 |
| `filterSub` | string |  | 是否筛选子类目，Y：是 |
| `fulfillment` | string |  | 配送方式，多条件查询用逗号隔开 |
| `includeBrands` | string |  | 包含品牌 |
| `includeSellers` | string |  | 包含卖家 |
| `keyword` | string |  | 关键字 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `matchType` | integer |  | "匹配方式, 默认: 2 可选值(必须严格使用下列数字值之一): 1: 词组匹配 2: 模糊匹配 3: 精准匹配  禁止使用未列出的值。  |
| `maxBsr` | integer |  | 大类 BSR 最低排名 |
| `maxBsrCr` | number |  | BSR 最高增长率 |
| `maxBsrCv` | integer |  | BSR 最高增长数 |
| `maxFba` | number |  | FBA 最高运费 |
| `maxLqs` | number |  | 最高 Listing 页面质量分 |
| `maxPrice` | number |  | 最高价格 |
| `maxProfit` | number |  | 最大毛利率 |
| `maxRating` | number |  | 最高评分值 |
| `maxRatings` | integer |  | 最高评分数 |
| `maxRatingsCv` | integer |  | 最高月新增评分数 |
| `maxRevenue` | number |  | 最高月销售额 |
| `maxRevenueCr` | number |  | 月销售额最高增长率 |
| `maxSellers` | integer |  | 最大卖家数量 |
| `maxSubBsrRank` | integer |  | 最大子类排名 |
| `maxUnits` | integer |  | 最高月销量 |
| `maxUnitsCr` | number |  | 月销量最高增长率 |
| `maxVariations` | integer |  | 最高变体数 |
| `maxWeights` | number |  | 最大重量 |
| `minBsr` | integer |  | 大类 BSR 最高排名 |
| `minBsrCr` | number |  | BSR 最低增长率 |
| `minBsrCv` | integer |  | BSR 最低增长数 |
| `minFba` | number |  | FBA 最低运费 |
| `minLqs` | number |  | 最低 Listing 页面质量分 |
| `minPrice` | number |  | 最低价格 |
| `minProfit` | number |  | 最小毛利率 |
| `minRating` | number |  | 最低评分值 |
| `minRatings` | integer |  | 最低评分数 |
| `minRatingsCv` | integer |  | 最低月新增评分数 |
| `minRevenue` | number |  | 最低月销售额 |
| `minRevenueCr` | number |  | 月销售额最低增长率 |
| `minSellers` | integer |  | 最小卖家数量 |
| `minSubBsrRank` | integer |  | 最小子类排名 |
| `minUnits` | integer |  | 最低月销量 |
| `minUnitsCr` | number |  | 月销量最低增长率 |
| `minVariations` | integer |  | 最低变体数 |
| `minWeights` | number |  | 最小重量 |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `nodeIdPath` | string |  | 类目编号 |
| `nodeIdPathEqual` | boolean |  | true为类目精确查询 false为查询当前及子类目 |
| `nodeIdPaths` | array |  | 类目节点字符串列表 |
| `order` | object |  | 排序 |
| `page` | integer |  | 页码 |
| `sellerNation` | string |  | 卖家所属地, 默认不限制, 多个用逗号隔开 可选值(仅填写字段名): - CN: 中国 - HK: 中国香港 - US: 美国 - JP: 日本 - GB: 英国 - DE: 德国 - FR: 法国 - IT: 意大利 - ES: 西班牙 - CA: 加拿大 - IN: 印度 - TR: 土耳其 - TW: 中国台湾 - MX: 墨西哥 - AU: 澳大利亚 - AE: 阿联酋 - BR: 巴西 禁止使用未列出的值。  |
| `size` | integer |  | 每页条数 |
| `variation` | string |  | 是否查询变体ASIN，如果没有明确指定则要设置成: Y 可选值(仅填写字段名): - Y: exclude - N: include  |
| `weightUnit` | string |  | 重量单位，默认：g 可选值(仅填写字段名): - g: 克 - kg: 千克 - ounces: 盎司 - pounds: 磅 禁止使用未列出的值。  |

## 基本信息

- **MCP Code**: `product_research`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/product/research`

## 响应参数

返回字段与 `competitor_lookup` 一致（见上）。

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/product/research' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","month":"202507","minPrice":100,"maxPrice":101,"variation":"N","page":1,"size":1}'
```

