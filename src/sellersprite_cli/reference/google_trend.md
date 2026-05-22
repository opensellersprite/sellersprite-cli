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
- 判断关键词是否为"短期热词"还是"长期需求"
- 对比不同平台（Google vs Amazon）的需求变化节奏

## MCP 调用名称

`mcp__sellersprite__google_trend`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | keyword | String |  | 关键字，iphone stand |
| 3 | googleProp | String |  | 类别，web:google网页搜索shoppingCart:google购物搜索 |
| 4 | monthly | boolean |  | 按照月份，false（默认值） |

## 基本信息

- **MCP Code**: `google_trend`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/google/trends`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场，见表 1.2 | US |
| 2 | keyword | String | 关键字 | phone stand |
| 3 | link | String | google trend链接 |  |
| 4 | items | List | 明细 |  |
| 5 | └time | Long | 时间戳 | 1555804800000 |
| 6 | └value | Integer | 值 | 2 |

## 请求示例

```json
{
  "code": "OK",
  "message": "成功",
  "data": {
    "marketplace": "US",
    "keyword": "iphone stand",
    "link": "https://trends.google.com/trends/explore?...",
    "items": [
      {"time": 1599350400000, "value": 33},
      {"time": 1599955200000, "value": 37}
    ]
  }
}
```

