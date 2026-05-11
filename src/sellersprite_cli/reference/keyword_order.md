# keyword_order

## 描述

基于 ASIN 的关键词反查工具，用于分析某个或多个 ASIN
在指定时间周期内，实际参与曝光与转化的关键词表现。

该工具从“结果倒推原因”，回答以下关键问题：
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
| `asins` | array | 是 | asin list |
| `conversionType` | string |  | 转化类型 可选值(仅填写字段名): - E: 转化优质词 - S: 转化平稳词 - L: 转化流失词 - I: 无效曝光词  |
| `date` | string | 是 | 回溯类型. 可选值: W/M. 当 reverseType = 'W' 时, date 必须为 yyyyMMdd 格式, 且表示当周的周六. 当 reverseType = 'M' 时, date 必须为 yyyyMM 格式. |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `matchType` | integer |  | 匹配方式 可选值(必须严格使用下列数字值之一): 1: 词组匹配 2: 模糊匹配 3: 精准匹配  禁止使用未列出的值。  |
| `order` | object |  | 排序（见[表1.8 关键词选品排序字段](./api_appendix.md#关键词选品排序字段表18)） |
| `page` | integer |  | 页码 |
| `reverseType` | string | 是 | 反查模式 可选值(仅填写字段名): - W: 周 - M: 月  |
| `size` | integer |  | 每页条数 |
| `variation` | string |  | 是否查询变体ASIN 可选值(仅填写字段名): - Y: exclude - N: include  |

## 基本信息

- **MCP Code**: `keyword_order`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword/order`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| keyword | String | 出单关键词 |
| keywordCn | String | 中文翻译 |
| searchRank | Integer | 搜索排名 |
| orderCount | Integer | 出单数 |
| orderRate | Float | 出单率 |
| page | Integer | 页码 |
| size | Integer | 每页条数 |
| total | Integer | 总条数 |

## 请求示例

```json
{
  "request": {
    "asins": [
      "B0XXX1",
      "B0XXX2"
    ],
    "conversionType": "E",
    "date": "20260425",
    "marketplace": "US",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "reverseType": "M",
    "size": 20,
    "variation": "Y"
  }
}
```

