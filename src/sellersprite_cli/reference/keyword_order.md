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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `asins` | array | 是 | ASIN列表，最大20个 |
| `conversionType` | array |  | 转化类型：E=优质词 S=平稳词 L=流失词 I=无效曝光词 |
| `date` | string |  | 查询日期。周格式 yyyyMMdd(当周周六)，月格式 yyyyMM |
| `marketplace` | string | 是 | Amazon 站点代码：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `order` | object |  | 排序（见[表2.6 出单词排序字段](./api_appendix.md#出单词排序字段表26)） |
| `page` | integer |  | 当前页，默认1 |
| `reverseType` | string | 是 | 反查模式：W=周，M=月 |
| `size` | integer |  | 每页条数，默认50 |
| `variation` | array |  | 是否查询变体：Y=否，N=是 |

## 基本信息

- **MCP Code**: `keyword_order`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-order`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| keyword | String | 关键词 |
| keywordCn | String | 中文翻译 |
| keywordJp | String | 日文翻译 |
| asin | String | 所属ASIN |
| searches | Integer | 搜索量 |
| monopolyClickRate | Float | 点击垄断率 |
| cvsShareRate | Float | 转化共享率 |
| searchRank | Integer | 搜索排名 |
| searchRankGv | Integer | 搜索量变化 |
| searchRankGr | Double | 搜索量变化率 |
| top3ClickingRate | Float | 前三点击占比 |
| top3ConversionRate | Float | 前三转化占比 |
| conversionType | String | 转化类型：E=优质 S=平稳 L=流失 I=无效 |
| pages | Integer | 总页数 |
| page | Integer | 当前页 |
| size | Integer | 每页条数 |
| total | Integer | 总条数 |
| took | Integer | 耗时(毫秒) |
| order | Object | 当前排序信息 |

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

## CLI 使用示例

```bash
# 月度反查
sellersprite keyword order 202604 --asins B07Z82895W --reverse-type M

# 周度反查
sellersprite keyword order 20260426 --asins B07Z82895W --reverse-type W

# 带筛选条件
sellersprite keyword order 202604 --asins B07Z82895W --conversion-type E,S --variation Y

# 自定义排序
sellersprite keyword order 202604 --asins B07Z82895W --order-field searchRank --order-desc
```