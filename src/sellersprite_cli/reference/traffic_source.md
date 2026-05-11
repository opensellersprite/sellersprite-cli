# traffic_source

## 描述

Amazon 流量关键词结构分析工具（ASIN / 关键词维度）。

用于分析某个 ASIN 或关键词在指定月份内：
- 实际带来流量的关键词总量
- 不同来源（自然搜索 / 官方推荐 / 广告）的流量词分布
- 广告词、品牌词、推荐词在整体流量中的占比
- ASIN 当前的基础商品信息与类目背景

该工具的核心价值在于：
【理解一个 ASIN 或关键词“流量是从哪里来的”】【而不是只有搜索量】

典型可回答的问题包括：
- 这个 ASIN 主要吃的是自然流量，还是广告流量？
- 有多少流量词是 Amazon 官方体系推荐出来的？
- 广告词在整体流量中占比高不高？
- 这个 ASIN 是否已经形成稳定的自然搜索词池？
- 竞品是否严重依赖 SP / 视频广告获客？

适用场景：
- 竞品流量结构分析
- 判断 ASIN 是否“靠广告堆起来”
- 广告投放与自然 SEO 策略制定
- 流量词挖掘与优先级判断

## MCP 调用名称

`mcp__sellersprite__traffic_source`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string |  | 查询月份, 格式: yyyyMM |
| `order` | object |  | 排序（见[表2.3 流量词列表排序字段](./api_appendix.md#流量词列表排序字段表23)） |
| `page` | integer |  | 页码 |
| `q` | string | 是 | asin 或者 关键词 |
| `size` | integer |  | 每页条数 |

## 基本信息

- **MCP Code**: `traffic_source`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/source`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| trafficSources[].type | String | 流量来源类型 |
| trafficSources[].percentage | Float | 占比 |
| trafficSources[].count | Integer | 流量数 |
| trafficSources[].keywords | List | 关键词列表 |

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "month": "202604",
    "order": {
      "field": "searches",
      "desc": true
    },
    "page": 1,
    "q": "B0XXXXXXXXX",
    "size": 20
  }
}
```

