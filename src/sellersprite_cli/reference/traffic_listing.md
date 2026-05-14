# traffic_listing

## 描述

查询指定 ASIN 在 Amazon 站内的关联商品列表，用于分析竞品结构与关联关系。

该工具基于 Amazon 站内关系模型，返回与目标 ASIN 存在
关联、竞品或同类关系的商品数据，包括销量、BSR、价格、
利润率、评分、卖家结构、变体信息等核心指标。

适用于以下场景：
- 查找目标 ASIN 的直接竞品与强关联商品
- 分析某个市场的头部商品结构与集中度
- 判断新品进入时将面对的主要对手
- 分析变体数量、卖家数量、品牌垄断程度

## MCP 调用名称

`mcp__sellersprite__traffic_listing`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `asinList` | array | 是 | asin列表 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `order` | object |  | 排序（见[表2.3 流量词列表排序字段](./api_appendix.md#流量词列表排序字段表23)） |
| `page` | integer |  | 页码 |
| `relations` | array | 是 | 关联类型 |
| `size` | integer |  | 每页条数 |
| `trafficSourceTypes` | array |  | 流量来源类型 |
| `variations` | boolean |  | 是否查询变体 |

## 基本信息

- **MCP Code**: `traffic_listing`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/listing/page`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| relations[].{asin,title,imageUrl,brand} | - | 关联 ASIN 信息 |
| relations[].trafficSourceType | String | 流量来源 |
| relations[].trafficCount | Integer | 流量数 |
| relations[].conversionCount | Integer | 转化数 |

## 请求示例

```json
{
  "request": {
    "asinList": [
      "B0XXX1",
      "B0XXX2"
    ],
    "marketplace": "US",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "relations": [
      "similar"
    ],
    "size": 20,
    "variations": false
  }
}
```

