# review

## 描述

查询指定 Amazon ASIN 的商品评论列表，返回评论标题、评论内容、评分、评论人、评论时间等信息，用于获取商品的用户反馈和评价数据。

适用于以下场景：
- 分析竞品评论情感倾向（好评/中评/差评占比）
- 挖掘用户痛点和需求（从评论内容中提取）
- 筛选特定类型的评论（带图/带视频/带VP/带VINE）
- 监控评论变化趋势

## MCP 调用名称

`mcp__sellersprite__review`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | asin | String | ✓ | ASIN |
| 3 | starList | List |  | 评论星级，1: 一星, 2: 二星, 3: 三星, 4: 四星, 5: 五星 |
| 4 | typeList | List |  | 评论类型，1：图片评论, 2：视频评论, 3：VP评论, 4：vine评论 |
| 5 | page | Integer |  | 页码，从 1 开始，默认：1 |
| 6 | size | Integer |  | 每页条数，最大10，默认：5 |

## 基本信息

- **MCP Code**: `review`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/review/{marketplace}/{asin}`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | author | String | 用户 |  |
| 2 | title | String | 标题 |  |
| 3 | content | String | 评论内容 |  |
| 4 | date | Long | 日期（时间戳） | 1772380800000 |
| 5 | star | Integer | 星级 |  |
| 6 | authorLabels | List | 评论人标签 |  |
| 7 | skus | List | sku信息 |  |
| 8 | images | List | 图片链接 |  |
| 9 | videos | List | 视频链接 |  |
| 10 | likes | Integer | 点赞数 |  |
| 11 | image | Boolean | 是否图片评论 |  |
| 12 | video | Boolean | 是否视频评论 |  |
| 13 | verified | Boolean | 是否实际购买评论 |  |
| 14 | vine | Boolean | 是否特邀评论 |  |
| 15 | free | Boolean | 是否免费评论 |  |
| 16 | experience | Boolean | 是否抢先体验评论 |  |

## 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/review/US/B07Z82895W?starList=4,5&typeList=1&page=1&size=10' \
  -H 'secret-key: Your Secret'
```

