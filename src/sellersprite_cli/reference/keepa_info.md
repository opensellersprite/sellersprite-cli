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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `asin` | string | 是 | Amazon 商品编号（ASIN） |
| `dailyLatest` | boolean |  | 是否仅获取每日最新数据 |
| `endTimestamp` | integer |  | 趋势结束时间戳 |
| `startTimestamp` | integer |  | 趋势起始时间戳 |

## 基本信息

- **MCP Code**: `keepa_info`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/keepa/{marketplace}/{asin}`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace/asin/dataAsin/parentAsin/variationAsins | - | 基本ASIN信息 |
| rootCategory/rootCategoryLabel | - | BSR大类信息 |
| salesRankReference/salesRankReferenceHistory | - | 排名节点变动历史 |
| nodeIdPath/nodeLabelPath | - | 上架类目全路径 |
| productStatus | String | STANDARD/DOWNLOADABLE/EBOOK等 |
| availabilityAmazon | String | 亚马逊跟卖状态 |
| title/brand/asinUrl/brandUrl | - | 标题品牌链接 |
| imageUrl/zoomImageUrl/imageUrls | - | 商品图片 |
| dimensions/weight/weightGram | - | 净尺寸/重量 |
| pkgDimensions/pkgDimensionsSize/pkgWeight/pkgWeightGram | - | 打包尺寸/重量 |
| fbaFees/fbaItems | - | FBA费用 |
| numberOfPages/numberOfItems | - | 页数/商品数 |
| price[].{timePoint,value} | - | 价格趋势 |
| dealPrice/buyBox/priceList | - | 各种价格趋势 |
| buyBoxSellerIdHistory | List | 黄金购物车卖家历史 |
| bsr[].{timePoint,value} | - | BSR排名趋势 (-1表示无效) |
| subSalesRank[].{nodeId,node,ranks} | - | 小类排名趋势 |
| reviews/rating/sellers | List | 评分数/值/卖家数趋势 |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

