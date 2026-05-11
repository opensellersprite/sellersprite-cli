# asin_detail_with_coupon_trend

## 描述

查询指定 ASIN 在 Amazon 指定市场下的完整商品详情信息，
包括基础属性、类目、评分、卖家、价格、配送方式等，
并同时返回该 ASIN 的优惠（Coupon）价格趋势数据，
用于分析真实成交价变化及促销策略。

## MCP 调用名称

`mcp__sellersprite__asin_detail_with_coupon_trend`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `asin` | string | 是 | Amazon 商品编号（ASIN） |

## 基本信息

- **MCP Code**: `asin_detail_with_coupon_trend`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/asin/{marketplace}/{asin}/with-coupon-trend`

## 响应参数

返回 `asin` 对象（结构同 [ASIN 详情](#3-asin-详情)） + `couponTrends` 数组（结构同 [ASIN优惠趋势](#56-asin优惠趋势)）。

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

