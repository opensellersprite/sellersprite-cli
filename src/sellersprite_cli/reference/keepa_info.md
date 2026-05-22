# keepa_info

## 描述

获取指定 Amazon ASIN 的完整商品画像及多维度历史趋势数据(不含有销量数据)。

本工具用于对单个 ASIN 进行深度分析，同时返回商品的静态基础信息
与随时间变化的核心经营指标趋势数据，适用于选品评估、竞品分析、
定价与跟卖监控、Listing 健康度分析等专业卖家场景。

返回内容包括但不限于：
  - 商品基础信息：标题、品牌、图片、ASIN 链接、商品状态、是否可售
  - 类目与排名信息：大类 / 小类 BSR、类目节点路径及其历史变化
  - 价格相关趋势：售价、成交价、划线价、黄金购物车价格历史
  - 竞争环境指标：卖家数量变化、Buy Box 卖家 ID 历史
  - 用户反馈指标：评论数、评分值的历史趋势
  - 变体与父子体关系：父 ASIN、变体 ASIN 列表
  - 物流与成本信息：FBA 费用、商品尺寸、重量、包装信息

  所有趋势字段均以标准时间序列结构返回（如 timePoint: 时间戳, value: 为对应的值），
  可直接用于趋势分析、图表展示或 AI 自动解读。

  适用场景示例：
  - 分析某个 ASIN 的价格、BSR 和评论趋势是否健康
  - 判断商品销量潜力及生命周期阶段（增长 / 稳定 / 衰退）
  - 监控 Buy Box 价格与卖家竞争变化
  - 理解商品在类目体系中的定位及变体结构
  - 为 AI 生成选品建议、竞品对比结论或运营决策支持

  当用户问题涉及「某一个 ASIN 的详情、趋势、变化、历史表现或综合分析时，应优先使用本工具。

## MCP 调用名称

`mcp__sellersprite__keepa_info`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |
| 3 | startTimestamp | Long |  | Trend Data Start Timestamp |
| 4 | endTimestamp | Long |  | Trend Data End Timestamp |
| 5 | dailyLatest | Boolean |  | Only Get Daily Latest Data |

## 基本信息

- **MCP Code**: `keepa_info`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/keepa/{marketplace}/{asin}`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | 见表 1.2 |
| 2 | asin | String | asin | B07V34QQ3C |
| 3 | dataAsin | String | 实际返回Keepa数据的ASIN | B07V34QQ3C |
| 4 | parentAsin | String | 父体ASIN | B0CWW9N7QW |
| 5 | variationAsins | List | 变体ASIN列表 | ["B0CN2PBVNS","B0BT4PMNY4","B0C6FYKC3D","B0CSLMG2TF","B0CGGPC6G3","B0BXG8L46Y","B0CRSZGN9L","B07V34QQ3C"] |
| 6 | rootCategory | String | BSR大类节点ID | 172282 |
| 7 | rootCategoryLabel | String | 跟类目 | Electronics |
| 8 | salesRankReference | String | 排名节点ID | 541966 |
| 9 | salesRankReferenceHistory | List | 排名节点变动历史 | PairStrDto 趋势字符串数据结构 |
| 10 | nodeIdPath | String | 上架类目全路径 | 172282:541966:13896617011:565098:13896597011 |
| 11 | nodeLabelPath | String | 上架类目名称全路径 | Electronics:Computers & Accessories:Computers & Tablets:Desktops:Towers |
| 12 | productStatus | String | 商品状态 | STANDARD:everything accessibleDOWNLOADABLE:no marketplace/3rd party price dataEBOOK:no price data and sales rank accessibleINACCESSIBLE:no data accessibleINVALID:invalid or deprecated asinVARIATION_PARENT:product is a parent ASINUNKNOWN:null of status |
| 13 | availabilityAmazon | String | 亚马逊跟卖转态 | -1 |
| 14 | title | String | 标题 | iBUYPOWER Gaming PC Computer Desktop Element 9260 (Intel Core i7-9700F 3.0Ghz, NVIDIA GeForce GTX 1660 Ti 6GB, 16GB DDR4, 240GB SSD, 1TB HDD, Wi-Fi & Windows 10 Home) Black |
| 15 | brand | String | 品牌 | iBUYPOWER |
| 16 | asinUrl | String | ASIN链接 | https://www.amazon.com/dp/B07V34QQ3C |
| 17 | brandUrl | String | 品牌链接 | https://www.amazon.com/s?k=iBUYPOWER |
| 18 | salesRankUrl | String | 销售排名链接 | https://www.amazon.com/b/?node=541966 |
| 19 | imageUrl | String | 商品缩略图200*200 | https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US200_.jpg |
| 20 | zoomImageUrl | String | 商品大图600*600 | https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US600_.jpg |
| 21 | imageUrls | List | 商品图片列表 | ["https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US200_.jpg","https://images-na.ssl-images-amazon.com/images/I/61bpfnvHjqL._AC_US200_.jpg",......] |
| 22 | dimensions | String | 净尺寸 | 97 |
| 23 | weight | String | 净重量 | 1063280 |
| 24 | weightGram | Integer | 净重数值 单位统一为：克(g) | 1055398:1063252:1063280 |
| 25 | pkgDimensions | String | 打包尺寸 | 22 x 19.9 x 12.4 inches |
| 26 | pkgDimensionsSize | List | 打包尺寸 长/宽/高 单位统一为：厘米(cm) | [558,506,316] |
| 27 | pkgWeight | String | 打包重量 | 0.11 pounds |
| 28 | pkgWeightGram | Integer | 打包重量数值 单位统一为：克(g) | 13660 |
| 29 | fbaFees | Float | FBA总费用 | 26.11 |
| 30 | fbaItems | String | FBA费用项明细JSON串，包含：仓储费，仓储费税，运送打包费，运送打包费税 | "{\"pickAndPackFeeTax\":0,\"storageFee\":0,\"storageFeeTax\":0,\"pickAndPackFee\":26.11}" |
| 31 | numberOfPages | Integer | 在第几页 | -1 |
| 32 | numberOfItems | Integer | 在第几个 | 1 |
| 33 | price | List | 价格趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 34 | dealPrice | List | 成交价趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 35 | buyBox | List | 黄金购物车价格趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 36 | priceList | List | 划线价格 | 见 PairNumberDto 趋势数字数据结构 |
| 37 | buyBoxSellerIdHistory | List | 黄金购物车卖家Id历史趋势 | PairStrDto 趋势字符串数据结构 |
| 38 | bsr | List | 大类BSR排名历史趋势 | 见 PairNumberDto 趋势数字数据结构 |
| 39 | subSalesRank | List | 小类排名趋势数据 | 见 SubRankTrendDto 小类排名趋势 |
| 40 | reviews | List | 评分数趋势数据 | 见 PairNumberDto 趋势数字数据结构 |
| 41 | rating | List | 评分值趋势数据 | 见 PairNumberDto 趋势数字数据结构 |
| 42 | sellers | List | 卖家数趋势数据 | 见 PairNumberDto 趋势数字数据结构 |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

