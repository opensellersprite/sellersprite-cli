# keyword_miner

## 描述

Amazon 高级关键词流量与竞争分析工具（卖家决策级）。

本工具用于从真实 Amazon 卖家视角，系统性评估某个关键词
或一组关键词是否具备以下价值：
- 是否存在真实且稳定的搜索与购买需求
- 是否存在可进入空间，而非被头部卖家或广告完全垄断
- 是否适合作为自然流量词、广告投放词或新品切入词

工具综合分析以下核心维度：
1. 需求强度：搜索量、购买量、购买率
2. 竞争强度：商品数、广告竞品数、标题密度、搜索排名
3. 垄断程度：点击集中度（monopolyClickRate）、SPR
4. 成本结构：PPC 竞价区间、平均售价
5. 相关性质量：关键词与市场的相关度、词长、类目匹配
6. 商业信号：是否为 Amazon Choice 关键词

适合在以下场景中调用：
- 批量挖掘高潜力流量关键词
- 筛选“高搜索但未被垄断”的可切入关键词
- 判断某关键词更适合做自然排名还是广告投放
- 为新品或Listing优化选择核心关键词与长尾词
- 对比多个关键词，选出竞争压力更小、ROI 更高的目标词

返回结果应以“是否值得做”为核心进行解读：
- 搜索量高 + 购买率高：代表真实需求强
- 商品数高但点击集中度低：代表市场分散，存在机会
- SPR 较低：代表进入成本相对友好
- PPC 竞价低于均价承受范围：代表广告可控
- 标题密度低 + 相关度高：代表 SEO 切入空间大

当需要基于数据判断关键词可行性、竞争难度或投放价值时，
AI 应优先调用该工具获取客观量化依据，而非凭经验猜测。

## MCP 调用名称

`mcp__sellersprite__keyword_miner`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `amazonChoice` | boolean |  | 亚马逊推荐词 |
| `excludeKeywords` | array |  | 排除的词 |
| `filterRootWord` | integer |  | 过滤词根 可选值(必须严格使用下列数字值之一): 0: 包含所有 1: 只包含词根  禁止使用未列出的值。  |
| `historyDate` | string |  | 查询月份, 格式: yyyyMM |
| `includeKeywords` | array |  | 包含的词 |
| `keyword` | string | 是 | 关键词 |
| `keywordList` | array |  | 批量查询关键词 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `matchType` | integer |  | 匹配方式 可选值(必须严格使用下列数字值之一): 2: 广泛匹配 3: 词组匹配  禁止使用未列出的值。  |
| `maxAdProducts` | integer |  | 最大广告竞品数 |
| `maxBid` | number |  | 最大ppc竞价 |
| `maxMonopolyClickRate` | number |  | 最大点击集中度 |
| `maxPrice` | number |  | 最大均价 |
| `maxProducts` | integer |  | 最大商品数 |
| `maxPurchases` | integer |  | 最大购买量 |
| `maxPurchasesRate` | number |  | 最大购买率 |
| `maxRating` | number |  | 最大评分值 |
| `maxRatings` | integer |  | 最大评分数 |
| `maxRelevancy` | number |  | 最大相关度 |
| `maxSPR` | integer |  | 最大SPR |
| `maxSearch` | integer |  | 最大搜索量 |
| `maxSearchRank` | integer |  | 最大搜索排名 |
| `maxSupplyDemandRatio` | number |  | 最大供需比 |
| `maxTitleDensity` | integer |  | 最大标题密度 |
| `maxWordCount` | integer |  | 最大单词个数 |
| `minAdProducts` | integer |  | 最小广告竞品数 |
| `minBid` | number |  | 最小ppc竞价 |
| `minMonopolyClickRate` | number |  | 最小点击集中度 |
| `minPrice` | number |  | 最小均价 |
| `minProducts` | integer |  | 最小商品数 |
| `minPurchases` | integer |  | 最小购买量 |
| `minPurchasesRate` | number |  | 最小购买率 |
| `minRating` | number |  | 最小评分值 |
| `minRatings` | integer |  | 最小评分数 |
| `minRelevancy` | number |  | 最小相关度 |
| `minSPR` | integer |  | 最小SPR |
| `minSearch` | integer |  | 最小搜索量 |
| `minSearchRank` | integer |  | 最小搜索排名 |
| `minSupplyDemandRatio` | number |  | 最小供需比 |
| `minTitleDensity` | integer |  | 最小标题密度 |
| `minWordCount` | integer |  | 最小单词个数 |
| `order` | object |  | 排序 |
| `page` | integer |  | 页码 |
| `size` | integer |  | 每页条数 |

## 基本信息

- **MCP Code**: `keyword_miner`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword/miner`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| keyword/keywordCn/keywordJp | String | 关键词及其翻译 |
| departments[].{code,label} | - | 类目 |
| month | String | 搜索月份 |
| supplement | String | 是否补充关键词 |
| searches/purchases/purchaseRate | - | 搜索/购买相关 |
| monopolyClickRate | Float | 点击垄断率 |
| products/adProducts | Integer | 商品数/广告竞品数 |
| supplyDemandRatio | Float | 供需比 |
| avgPrice/avgRatings/avgRating | - | 平均价格/评分数/评分值 |
| bidMin/bidMax/bid | Float | PPC价格 |
| cvsShareRate | Float | 转化共享率 |
| wordCount | Integer | 单词个数 |
| titleDensity | Integer | 标题密度 |
| spr | Integer | SPR |
| relevancy | Double | 相关度 |
| amazonChoice | Boolean | 亚马逊推荐词 |
| searchRank | Integer | 搜索排名 |
| clicks/impressions | - | 点击量/展示量 |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword/miner' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keyword":"wireless earbuds","page":1,"size":1}'
```

