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

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场,见表1.2，US |
| 2 | asin | String | ✓ | B07Z82895W |

## 基本信息

- **MCP Code**: `asin_prediction`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/sales/prediction/asin`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | asinDetail | Object | asin明细 |  |
| 2 | └asin | String | asin | B00CFM8DI2 |
| 3 | └title | String | 标题 | Boot Bananas Original Shoe Deodorizer |
| 4 | └brand | String | 平台 | Boot Bananas |
| 5 | └availableDate | Long | 上架时间 | 1397001600000 |
| 6 | └category | String | 类目名称 | Clothing, Shoes & Jewelry |
| 7 | └categoryId | String | 类目id | 7141123011 |
| 8 | └imageUrl | String | 图片URL | https://images-na.ssl-images-amazon.com/images/I/41AGxmiW-vL._AC_US600_.jpg |
| 9 | └ratings | Integer | 评分数 | 32004 |
| 10 | └rating | Float | 评分值 | 4.6 |
| 11 | dailyItemList | List | 日销量预测明细 |  |
| 12 | └date | String | 日期 | 45035 |
| 13 | └bsr | Integer | bsr | 48614 |
| 14 | └sales | Integer | 销量 | 14 |
| 15 | └amount | Float | 销售额 | 200 |
| 16 | └price | Float | 单价 | 20 |
| 17 | monthItemList | List | 月销量预测明细 |  |
| 18 | └date | String | 日期 | 45017 |
| 19 | └sales | Integer | 销量 | 14 |
| 20 | └amount | Float | 销售额 | 200 |
| 21 | └price | Float | 单价 | 20 |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B0XXXXXXXXX"
}
```

