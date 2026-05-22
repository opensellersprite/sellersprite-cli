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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | historyDate | String |  | 历史日期，yyyyMM格式，最近30天不传或传空字符串，202201 |
| 3 | keyword | String | ✓ | 关键词 |
| 4 | keywordList | List |  | 批量查询关键词，["phone stand"] |
| 5 | minSearch | Integer |  | 最小搜索量，543 |
| 6 | maxSearch | Integer |  | 最大搜索量，23453 |
| 7 | minPurchases | Integer |  | 最小购买量，6 |
| 8 | maxPurchases | Integer |  | 最大购买量，34 |
| 9 | minPurchasesRate | Float |  | 最小购买率，3 |
| 10 | maxPurchasesRate | Float |  | 最大购买率，43 |
| 11 | minSPR | Integer |  | 最小SPR，2 |
| 12 | maxSPR | Integer |  | 最大SPR，16 |
| 13 | minTitleDensity | Integer |  | 最小标题密度，2 |
| 14 | maxTitleDensity | Integer |  | 最大标题密度，23 |
| 15 | minRelevancy | Float |  | 最小相关度，23，最小0 |
| 16 | maxRelevancy | Float |  | 最大相关度，90，最大100 |
| 17 | minSearchRank | Integer |  | 最小搜索排名，33 |
| 18 | maxSearchRank | Integer |  | 最大搜索排名，3223 |
| 19 | minProducts | Integer |  | 最小商品数，54 |
| 20 | maxProducts | Integer |  | 最大商品数，324 |
| 21 | minSupplyDemandRatio | Float |  | 最小供需比，11.2 |
| 22 | maxSupplyDemandRatio | Float |  | 最大供需比，45.2 |
| 23 | minAdProducts | Integer |  | 最小广告竞品数，123 |
| 24 | maxAdProducts | Integer |  | 最大广告竞品数，345 |
| 25 | minWordCount | Integer |  | 最小单词个数，2 |
| 26 | maxWordCount | Integer |  | 最大单词个数，4 |
| 27 | minMonopolyClickRate | Float |  | 最小点击集中度，23.4 |
| 28 | maxMonopolyClickRate | Float |  | 最大点击集中度，53.1 |
| 29 | minBid | Float |  | 最小ppc竞价，10.2 |
| 30 | maxBid | Float |  | 最大ppc竞价，23.1 |
| 31 | minPrice | Float |  | 最小均价，43.3 |
| 32 | maxPrice | Float |  | 最大均价，234.2 |
| 33 | minRatings | Integer |  | 最小评分数，100 |
| 34 | maxRatings | Integer |  | 最大评分数，399 |
| 35 | minRating | Float |  | 最小评分值，3 |
| 36 | maxRating | Float |  | 最大评分值，4.9 |
| 37 | amazonChoice | Boolean |  | 亚马逊推荐词，true |
| 38 | filterRootWord | Integer |  | 过滤词根 0包含所有 1只包含词根，0 |
| 39 | matchType | Integer |  | 2: 广泛匹配, 3: 词组匹配，2 |
| 40 | includeKeywords | List |  | 包含的词，["phone stand"] |
| 41 | excludeKeywords | List |  | 排除的词，["phone stand"] |
| 42 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 43 | size | Integer |  | 每页条数，默认：50，最大：100 |
| 44 | order | Object |  | 排序 |
| 45 | └field | String |  | 排序字段，加入筛序条件之后，不能以相关度排序，见表2.4 |
| 46 | └desc | boolean |  | true为降序 false为升序，默认降序 |

## 基本信息

- **MCP Code**: `keyword_miner`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword/miner`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场，见表 1.2 | US |
| 2 | keyword | String | 关键词 | phone stand for recording |
| 3 | keywordCn | String | 关键词中文翻译 | 用于录音的电话支架 |
| 4 | keywordJp | String | 关键词英文翻译 | 録音用電話スタンド |
| 5 | departments | List | 类目 |  |
| 6 | └code | String | 类目代码 | electronics |
| 7 | └label | String | 类目名称 | Electronics |
| 8 | month | String | 搜索月份 | 2022.01 |
| 9 | supplement | String | 是否属于补充关键词（无当前月搜索量） | N |
| 10 | searches | Integer | 搜索量 | 21582 |
| 11 | purchases | Integer | 月购买量 | 1996 |
| 12 | purchaseRate | Float | 月购买率 | 0.0925 |
| 13 | monopolyClickRate | Float | 点击垄断率 | 0.3 |
| 14 | products | Integer | 商品数 | 1645 |
| 15 | adProducts | Integer | 广告竞品数 | 34 |
| 16 | supplyDemandRatio | Float | 供需比 | 13.12 |
| 17 | avgPrice | Float | 平均价格 | 36.14 |
| 18 | avgRatings | Integer | 平均评分数 | 12223 |
| 19 | avgRating | Float | 平均评分值 | 4.5 |
| 20 | bidMin | Float | 最小PPC价格 | 1.34 |
| 21 | bidMax | Float | 最大PPC价格 | 3.21 |
| 22 | bid | Float | PPC价格 | 1.6 |
| 23 | cvsShareRate | Float | 转化共享率 | 0.3084 |
| 24 | wordCount | Integer | 单词个数 | 4 |
| 25 | titleDensity | Integer | 标题密度 | 42.9 |
| 26 | spr | Integer | SPR | 6 |
| 27 | relevancy | Double | 相关度 | 28.6 |
| 28 | amazonChoice | Boolean | 亚马逊推荐词 true是的 false不是 | false |
| 29 | searchRank | Integer | 搜索排名 | 17910 |
| 30 | └code | String | 类目代码 | electronics |
| 31 | └label | String | 类目名称 | Electronics |
| 32 | clicks | Integer | 点击量 | 10 |
| 33 | impressions | Long | 展示量 | 20 |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword/miner' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keyword":"wireless earbuds","page":1,"size":1}'
```

