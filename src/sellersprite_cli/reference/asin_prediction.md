# asin_prediction

## 描述

查询指定 ASIN 在 Amazon 对应市场的商品基础信息及销量与销售额预测数据。
该接口返回 ASIN 近14个月的销量数据，并提供按日维度与月维度汇总的销量、销售额、价格及 BSR 等预测指标。

适用于以下场景：
- ASIN 销量趋势分析与判断
- 商品增长性与生命周期判断
- 竞品销售表现对比分析
- 选品评估

## MCP 调用名称

`mcp__sellersprite__asin_prediction`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `asin` | string | 是 | Amazon 商品编号（ASIN） |

## 基本信息

- **MCP Code**: `asin_prediction`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/asin`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asinDetail.{asin,title,brand,availableDate,category,categoryId,imageUrl,ratings,rating} | - | ASIN 明细 |
| dailyItemList[].{date,bsr,sales,amount,price} | - | 日销量预测 |
| monthItemList[].{date,sales,amount,price} | - | 月销量预测 |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

