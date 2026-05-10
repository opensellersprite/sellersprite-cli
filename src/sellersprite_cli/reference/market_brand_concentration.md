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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `newProduct` | integer |  | 新品定义阈值（单位：月），用于指定将上架在该时间范围内的商品视为新品。可根据行业特性调整，如服装类通常为 1，母婴等长生命周期行业可设为 6 |
| `nodeIdPath` | string | 是 | 产品所属的类目节点 ID, 例如： 2619525011:3741271， 通常通过查询【产品类目信息】获取，或由用户直接指定类目路径 |
| `topN` | integer |  | 头部Listing数量, 做竞争分析时，一般是取头部产品和整体样本做对比，来判断市场竞争度/集中度, 卖家精灵默认是取头部前10商品 |

## 基本信息

- **MCP Code**: `market_brand_concentration`
- **Method**: POST
- **URL**: `https://api.sellersprite.com/v1/market/brand-concentration`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| nodeIdPath | String | 类目路径 |
| totalBrands | Integer | 总品牌数 |
| top1BrandUnits | Float | TOP1 品牌销量占比 |
| top3BrandsUnits | Float | TOP3 品牌销量占比 |
| top10BrandsUnits | Float | TOP10 品牌销量占比 |
| hhi | Float | 赫芬达尔指数 |
| concentrationLevel | String | 集中度等级 |

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

