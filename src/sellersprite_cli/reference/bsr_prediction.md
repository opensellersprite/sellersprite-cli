# bsr_prediction

## 描述

根据 Amazon 指定市场下的一级类目节点和大类 BSR 排名，
预测该 BSR 在当前类目中的日销量和近 30 天销量，
并返回对应 BSR 区间的销量预测明细，
用于评估类目热度和市场容量。

## MCP 调用名称

`mcp__sellersprite__bsr_prediction`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点 |
| `bsr` | integer | 是 |  |
| `categoryId` | string | 是 | 一级类目节点，查产品类目返回 |

## 基本信息

- **MCP Code**: `bsr_prediction`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/bsr`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| marketplace | String | 市场 |
| bsr | Integer | BSR 排名 |
| categoryLabel | String | 类目名称 |
| estDailySales | Integer | 预测日销量 |
| estMonthSales | Integer | 预测30天销量 |
| itemList[].{bsr,estDailySales,estMonthSales} | - | 类目内排名靠前的BSR销量明细 |

## 请求示例

```json
{
  "marketplace": "US",
  "bsr": 10000,
  "categoryId": "172282"
}
```

