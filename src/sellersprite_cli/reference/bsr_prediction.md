# bsr_prediction

## 描述

根据 Amazon 指定市场下的一级类目节点和大类 BSR 排名，
预测该 BSR 在当前类目中的日销量和近 30 天销量，
并返回对应 BSR 区间的销量预测明细，
用于评估类目热度和市场容量。

## MCP 调用名称

`mcp__sellersprite__bsr_prediction`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | bsr | Integer | ✓ | 大类排名，1024 |
| 3 | categoryId | String | ✓ | 一级类目节点，查产品类目返回，11260432011 |

## 基本信息

- **MCP Code**: `bsr_prediction`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/bsr`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | marketplace | String | 市场 | US |
| 2 | bsr | Integer | 1 | B07Z82895W |
| 3 | categoryLabel | String | 类目名称 | 2685 |
| 4 | estDailySales | Integer | 预测日销量 | 99 |
| 5 | estMonthSales | Integer | 预测30天销量 | 2965 |
| 6 | itemList | List | 明细 |  |
| 7 | └bsr | Integer | bsr | 1 |
| 8 | └estDailySales | Integer | 预测日销量 | 99 |
| 9 | └estMonthSales | Integer | 预测30天销量 | 2965 |

## 请求示例

```json
{
  "marketplace": "US",
  "bsr": 10000,
  "categoryId": "172282"
}
```

