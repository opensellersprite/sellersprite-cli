# review

## 描述

查询指定 Amazon ASIN 的商品评论列表，返回评论标题、评论内容、评分、评论人、评论时间等信息，用于获取商品的用户反馈和评价数据。

适用于以下场景：
- 分析竞品评论情感倾向（好评/中评/差评占比）
- 挖掘用户痛点和需求（从评论内容中提取）
- 筛选特定类型的评论（带图/带视频/带文字回复）
- 监控评论变化趋势

## MCP 调用名称

`mcp__sellersprite__review`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `asin` | string | 是 | ASIN |
| `categoryId` | string |  | 类目节点 |
| `star` | integer |  | 星级筛选 |
| `hasImage` | boolean |  | 仅含图片评论 |
| `hasVideo` | boolean |  | 仅含视频评论 |
| `hasComment` | boolean |  | 仅含文字评论 |
| `page` | integer |  | 页码，默认 1 |
| `size` | integer |  | 每页条数，默认 20，最大 50 |

## 基本信息

- **MCP Code**: `review`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/review/{marketplace}/{asin}`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| totalReviews | Integer | 总评论数 |
| positiveRate | Float | 好评率 |
| neutralRate | Float | 中评率 |
| negativeRate | Float | 差评率 |
| reviews[].id | String | 评论ID |
| reviews[].rating | Integer | 星级 |
| reviews[].title | String | 评论标题 |
| reviews[].content | String | 评论内容 |
| reviews[].author | String | 评论者 |
| reviews[].date | String | 评论日期 |
| reviews[].helpful | Integer | 有帮助数 |
| reviews[].verified | Boolean | 是否已验证购买 |
| reviews[].images | List | 评论图片 |
| reviews[].videos | List | 评论视频 |

## 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/review/US/B07Z82895W?size=1' \
  -H 'secret-key: Your Secret'
```

