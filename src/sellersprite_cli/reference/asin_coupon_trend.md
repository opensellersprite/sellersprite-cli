# asin_coupon_trend

## 描述

查询指定 ASIN 在 Amazon 指定市场下的优惠价格信息。
返回 ASIN 原价、优惠类型（金额 / 百分比）、优惠金额，
以及计算后的最终成交价格。

## MCP 调用名称

`mcp__sellersprite__asin_coupon_trend`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | B08GHW4TBS |

## 基本信息

- **MCP Code**: `asin_coupon_trend`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/coupon-trend`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | marketplace |  |
| 2 | asin | String | asin |  |
| 3 | date | String | 日期 |  |
| 4 | type | String | 优惠类型 | M: 减免金额, P: 百分比折扣 |
| 5 | asinPrice | Float | ASIN价格 |  |
| 6 | couponPrice | Float | 优惠金额 |  |
| 7 | finalPrice | Float | 实际价格 |  |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

