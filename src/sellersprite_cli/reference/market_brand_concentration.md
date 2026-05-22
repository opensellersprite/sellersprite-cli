# market_brand_concentration

## 描述

用于分析指定 Amazon 市场类目节点下的品牌集中度情况。

通过传入对应站点（国家编码）、类目节点路径及筛选条件，返回该类目中头部 Listing 的
对各品牌的商品数量、新品数量、新品销量与销售额、总体销量与销售额及其占比进行统计分析。

头部品牌的总销量Y，占样本范围内商品总销量A的比例，即品牌集中度=Y/A
头部品牌的销量占比越高，品牌的垄断程度越高，或用户对品牌的关注程度越高
例：头部品牌（销量前10品牌）总销量为7000，样本商品（销量前100位）总销量为10000，则品牌集中度为：7000/10000=70%；代表前10大品牌的销量占样本商品销量的70%

同级类目品牌集中度：是指该类目的同级类目的平均品牌集中度
比如类目：宠物用品 › 猫用品 › 玩具 › 薄荷玩具，其中薄荷玩具类目A1有2个同级类目（羽毛玩具A2、球形玩具A3，同属于宠物用品 › 猫用品 › 玩具类目）
则同级类目品牌集中度 = (A1品牌集中度+A2品牌集中度+A3品牌集中度)/3

可用于判断：
- 市场是否被少数头部品牌高度占据
- 新品牌在该类目中的生存与成长空间
- 各品牌在销量与销售额维度上的集中程度

## MCP 调用名称

`mcp__sellersprite__market_brand_concentration`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 站点编码，见表 1.2 |
| 2 | month | String |  | 筛选日期,默认最近30天，见表 1.1 |
| 3 | topN | Integer |  | 头部Listing数量，10 |
| 4 | newProduct | Integer |  | 新品定义，6 |
| 5 | nodeIdPath | String | ✓ | 节点 id 路径字符串，1064954:1069242:1069784:1069820:1069838:1069828 |

## 基本信息

- **MCP Code**: `market_brand_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/brand-concentration`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | brand | String | 品牌名称 | PILOT |
| 2 | ranking | Integer | 排名 | 1 |
| 3 | asins | List | 包含的商品ASIN集合 | ["B00P19MFYE"] |
| 4 | products | Integer | 商品数量，包含新品 | 4 |
| 5 | newProducts | Integer | 新品数量 | 1 |
| 6 | newUnits | Integer | 新品销量 | 45 |
| 7 | newRevenue | Float | 新品销售额 | 2342 |
| 8 | newUnitsRatio | Float | 新品销量占比 | 4.3 |
| 9 | newRevenueRatio | Float | 新品销售额占比 | 4 |
| 10 | avgPrice | Float | 平均价格 | 6.19 |
| 11 | ratings | Integer | 评分数 | 5695 |
| 12 | rating | Float | 评分值 | 4.8 |
| 13 | reviews | Integer | 评论数 | 234 |
| 14 | totalUnits | Integer | 总销量 | 32342 |
| 15 | totalRevenue | Float | 总销额 | 18837.35 |
| 16 | totalUnitsRatio | Float | 总销量占比 | 0.4478 |
| 17 | totalRevenueRatio | Float | 总销额占比 | 0.3052 |

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "month": "202604",
    "newProduct": 6,
    "nodeIdPath": "2619525011:3741271",
    "topN": 10
  }
}
```

