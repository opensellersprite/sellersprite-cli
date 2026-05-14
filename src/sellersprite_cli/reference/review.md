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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `asin` | string | 是 | ASIN |
| `starList` | array | | 评论星级（1-5星） |
| `typeList` | array | | 评论类型：1=图片 2=视频 3=VP 4=VINE |
| `page` | integer | | 当前页，默认1 |
| `size` | integer | | 每页条数，默认5，最大10 |

## 基本信息

- **MCP Code**: `review`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/review/{marketplace}/{asin}`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| author | String | 评论用户 |
| title | String | 评论标题 |
| content | String | 评论内容 |
| date | Long | 日期时间戳 |
| star | Integer | 星级 |
| authorLabels | List | 评论人标签 |
| skus | List | SKU信息 |
| images | List | 图片链接 |
| videos | List | 视频链接 |
| likes | Integer | 点赞数 |
| image | Boolean | 是否图片评论 |
| video | Boolean | 是否视频评论 |
| verified | Boolean | 是否VP购买评论 |
| vine | Boolean | 是否VINE评论 |
| free | Boolean | 是否免费评论 |
| experience | Boolean | 是否抢先体验评论 |

## 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/review/US/B07Z82895W?starList=4,5&typeList=1&page=1&size=10' \
  -H 'secret-key: Your Secret'
```

## CLI 使用示例

```bash
# 基本用法
sellersprite trend review B07Z82895W

# 筛选4-5星评论
sellersprite trend review B07Z82895W --star-list 4,5

# 筛选有图片的评论
sellersprite trend review B07Z82895W --type-list 1

# 筛选VP评论
sellersprite trend review B07Z82895W --type-list 3

# 筛选VINE评论
sellersprite trend review B07Z82895W --type-list 4
```
