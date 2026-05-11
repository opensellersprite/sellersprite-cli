# google_trend

## 描述

用于查询 Google Trends 中指定关键词在特定市场的搜索热度变化趋势。

该工具基于 Google 搜索行为（非 Amazon 站内），
反映真实用户在搜索引擎层面的需求变化，
可用于验证某个关键词或产品概念是否处于：
- 上升期
- 稳定期
- 衰退期
- 周期性波动

适合与 Amazon 关键词数据结合使用，用于：
- 新品立项前的需求趋势验证
- 判断关键词是否为“短期热词”还是“长期需求”
- 对比不同平台（Google vs Amazon）的需求变化节奏

## MCP 调用名称

`mcp__sellersprite__google_trend`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `endDate` | string |  | 结束日期，格式: yyyy-MM-dd |
| `googleProp` | string |  | 搜索来源类型（枚举值）: web, shoppingCart |
| `keyword` | string |  | 关键字 |
| `keywords` | array |  | 关键词列表 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `monthly` | boolean |  | 按照月份 |
| `startDate` | string |  | 开始日期，格式: yyyy-MM-dd |

## 基本信息

- **MCP Code**: `google_trend`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/google/trend`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 关键词 |
| timeline[].date | String | 日期 |
| timeline[].value | Integer | 搜索指数 |
| timeline[].category | Integer | 类别 |

## 请求示例

```json
{
  "request": {
    "googleProp": "web",
    "keyword": "wireless earbuds",
    "marketplace": "US",
    "monthly": false
  }
}
```

