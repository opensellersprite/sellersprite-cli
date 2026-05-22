# keyword_order

## 描述

基于 ASIN 的关键词反查工具，用于分析某个或多个 ASIN
在指定时间周期内，实际参与曝光与转化的关键词表现。

该工具从"结果倒推原因"，回答以下关键问题：
- 一个 ASIN 是通过哪些关键词获得曝光和转化的？
- 哪些关键词是真正带来转化的优质词？
- 哪些关键词正在流失转化，或只是无效曝光？
- 转化结构在最近一周 / 一个月是改善还是恶化？

适用于：
- 广告投放关键词优化（扩词 / 否词 / 降价）
- Listing 优化关键词取舍
- 竞品 ASIN 转化词拆解
- 判断某个 ASIN 的真实流量来源质量

## MCP 调用名称

`mcp__sellersprite__keyword_order`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asins | List | ✓ | asin列表，最大20，B07Z82895W |
| 3 | reverseType | String | ✓ | 反查模式 W-周 M-月，W |
| 4 | date | String |  | 查询日期，按周查，格式为yyyMMdd该周最后一天，按月查询yyyyMM，周：20241109月：202411 |
| 5 | conversionType | List |  | 转化类型：E：转化优质词，S：转化平稳词，L：转化流失词，I：无效曝光词，E |
| 6 | variation | List |  | 是否查询变体asin：Y:否 N:是，Y |
| 7 | page | Integer |  | 当前页，默认1 |
| 8 | size | Integer |  | 每页显示多少条，固定50 |
| 9 | order | Object |  | 排序 |
| 10 | └field | String |  | 排序字段，见表2.6 |
| 11 | └desc | Boolean |  | 是否倒序，false |

## 基本信息

- **MCP Code**: `keyword_order`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-order`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场，见表 1.2 | US |
| 2 | keyword | String | 关键词 | phone stand for recording |
| 3 | keywordCn | String | 关键词中文翻译 | 用于录音的电话支架 |
| 4 | keywordJp | String | 关键词英文翻译 | 録音用電話スタンド |
| 5 | asin | String | 所属asin | B0D1FZW65X |
| 6 | searches | Integer | 搜索量 | 21582 |
| 7 | monopolyClickRate | Float | 点击垄断率 | 0.3 |
| 8 | cvsShareRate | Float | 转化共享率 | 0.3084 |
| 9 | searchRank | Integer | 搜索排名 | 17910 |
| 10 | searchRankGv | Integer | 月变化量 | 5343 |
| 11 | searchRankGr | Double | 月变化率 | 0.3 |
| 12 | top3ClickingRate | Float | 前三点击 | 0.0813 |
| 13 | top3ConversionRate | Float | 前三转化 | 0.2011 |
| 14 | conversionType | String | 转化类型：E：转化优质词，S：转化平稳词，L：转化流失词，I：无效曝光词 | E |

## 请求示例

```json
{
  "request": {
    "asins": [
      "B07Z82895W"
    ],
    "conversionType": ["E", "S"],
    "date": "20260425",
    "marketplace": "US",
    "order": {
      "field": "searchRank",
      "desc": false
    },
    "page": 1,
    "reverseType": "M",
    "size": 50,
    "variation": ["Y"]
  }
}
```

