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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `keyword` | string | | 关键字 |
| `googleProp` | string | | 类别：web=Google网页搜索，shoppingCart=Google购物搜索 |
| `monthly` | boolean | | 是否按月份，默认 false |

## 基本信息

- **MCP Code**: `google_trend`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/google/trends`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| keyword | String | 关键字 |
| link | String | Google趋势链接 |
| items | List | 趋势数据明细 |
| items[].time | Long | 时间戳（毫秒） |
| items[].value | Integer | 趋势指数值 |

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

## CLI 使用示例

```bash
# 基本用法
sellersprite trend google --keyword "iphone stand"

# 搜索类型：网页搜索
sellersprite trend google --keyword "iphone stand" --google-prop web

# 搜索类型：购物搜索
sellersprite trend google --keyword "iphone stand" --google-prop shoppingCart

# 按月份汇总
sellersprite trend google --keyword "iphone stand" --monthly
```
