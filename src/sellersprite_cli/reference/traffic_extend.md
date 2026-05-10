# traffic_extend

## 描述

用于在指定 Amazon 站点中，根据 ASIN、时间范围及多维筛选条件，
批量搜索并分析高价值关键词的工具。

该工具适用于：
- 关键词拓展与筛选
- 广告投放关键词决策（PPC）
- 市场需求与竞争强度评估
- 选品或Listing优化前的关键词调研

返回结果包含：搜索量、购买量、转化率、PPC竞价、供需比、
广告竞争度、点击集中度、关联ASIN等核心商业指标，
可直接用于“是否值得投放 / 是否值得进入”的判断。

## MCP 调用名称

`mcp__sellersprite__traffic_extend`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `amazonChoice` | boolean |  | 亚马逊推荐词 |
| `asinList` | array | 是 | asins, 最多只支持20个，如果超过20个, 需要拆分多次请求 |
| `excludeKeywords` | array |  | 排除的词 |
| `historyDate` | string |  | 查询月份, 格式: yyyyMM |
| `includeKeywords` | array |  | 包含的词 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `matchType` | integer |  | 匹配方式 可选值(必须严格使用下列数字值之一): 1: 模糊匹配 2: 宽泛匹配 3: 精准匹配  禁止使用未列出的值。  |
| `maxAdProducts` | integer |  | 最大广告竞品数 |
| `maxAvgPrice` | number |  | 最大均价 |
| `maxBid` | number |  | 最大ppc竞价 |
| `maxCompetitors` | integer |  | 最大asin数 |
| `maxConversionRate` | number |  | 最大转化率 |
| `maxMonopolyClickRate` | number |  | 最大点击集中度 |
| `maxProducts` | integer |  | 最大商品数 |
| `maxPurchaseRate` | number |  | 最大购买率 |
| `maxPurchases` | integer |  | 最大购买量 |
| `maxSPR` | integer |  | 最大SPR |
| `maxSearchRank` | integer |  | 最大搜索排名 |
| `maxSearches` | integer |  | 最大月搜索量 |
| `maxSupplyDemandRatio` | number |  | 最大供需比 |
| `maxTitleDensity` | integer |  | 最大标题密度 |
| `maxTrafficPercentage` | number |  | 最大流量占比 |
| `maxWordCount` | integer |  | 最大单词个数 |
| `minAdProducts` | integer |  | 最小广告竞品数 |
| `minAvgPrice` | number |  | 最小均价 |
| `minBid` | number |  | 最小ppc竞价 |
| `minCompetitors` | integer |  | 最小asin数 |
| `minConversionRate` | number |  | 最小转化率 |
| `minMonopolyClickRate` | number |  | 最小点击集中度 |
| `minProducts` | integer |  | 最小商品数 |
| `minPurchaseRate` | number |  | 最小购买率 |
| `minPurchases` | integer |  | 最小购买量 |
| `minSPR` | integer |  | 最小SPR |
| `minSearchRank` | integer |  | 最小搜索排名 |
| `minSearches` | integer |  | 最小月搜索量 |
| `minSupplyDemandRatio` | number |  | 最小供需比 |
| `minTitleDensity` | integer |  | 最小标题密度 |
| `minTrafficPercentage` | number |  | 最小流量占比 |
| `minWordCount` | integer |  | 最小单词个数 |
| `order` | object |  | 排序 |
| `page` | integer |  | 页码 |
| `queryType` | integer | 是 | 查询方式, 默认: 2 可选值(必须严格使用下列数字值之一):  0: 所有变体  1: 畅销变体  2: 当前变体   禁止使用未列出的值。  |
| `size` | integer |  | 每页条数 |

## 基本信息

- **MCP Code**: `traffic_extend`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/traffic/extend`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 拓展关键词 |
| keywordCn | String | 中文翻译 |
| searches | Integer | 搜索量 |
| products | Integer | 商品数 |
| purchaseRate | Float | 购买率 |
| avgPrice | Float | 平均价格 |
| sourceAsins | List | 来源 ASIN |

## 请求示例

```json
{
  "request": {
    "amazonChoice": false,
    "asinList": [
      "B0XXX1",
      "B0XXX2"
    ],
    "excludeKeywords": [
      "keyword1"
    ],
    "historyDate": "202604",
    "includeKeywords": [
      "keyword1"
    ],
    "marketplace": "US",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "queryType": 2,
    "size": 20
  }
}
```

