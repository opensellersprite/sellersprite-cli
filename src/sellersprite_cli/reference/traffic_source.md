# traffic_source

## 描述

Amazon 流量关键词结构分析工具（ASIN / 关键词维度）。

用于分析某个 ASIN 或关键词在指定月份内：
- 实际带来流量的关键词总量
- 不同来源（自然搜索 / 官方推荐 / 广告）的流量词分布
- 广告词、品牌词、推荐词在整体流量中的占比
- ASIN 当前的基础商品信息与类目背景

该工具的核心价值在于：
【理解一个 ASIN 或关键词"流量是从哪里来的"】【而不是只有搜索量】

典型可回答的问题包括：
- 这个 ASIN 主要吃的是自然流量，还是广告流量？
- 有多少流量词是 Amazon 官方体系推荐出来的？
- 广告词在整体流量中占比高不高？
- 这个 ASIN 是否已经形成稳定的自然搜索词池？
- 竞品是否严重依赖 SP / 视频广告获客？

适用场景：
- 竞品流量结构分析
- 判断 ASIN 是否"靠广告堆起来"
- 广告投放与自然 SEO 策略制定
- 流量词挖掘与优先级判断

## MCP 调用名称

`mcp__sellersprite__traffic_source`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `marketplace` | string | 是 | Amazon 站点代码：US, JP, UK, DE, FR, IT, ES, CA, IN |
| `month` | string | 是 | 查询月份，格式 yyyyMM |
| `q` | string | 是 | ASIN 或关键词 |
| `page` | integer |  | 当前页，默认1 |
| `size` | integer |  | 每页条数，默认50，最大100 |
| `order` | object |  | 排序（见[表2.4 流量来源排序字段](./api_appendix.md#流量来源排序字段表24)） |

## 基本信息

- **MCP Code**: `traffic_source`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/traffic/source`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keywords | Integer | 全部流量词数量 |
| searchKeywords | Integer | 自然搜索词 |
| acKeywords | Integer | AC推荐词 |
| editorialKeywords | Integer | ER推荐词 |
| fourStarsKeywords | Integer | 4星推荐词 |
| hrKeywords | Integer | HR推荐词 |
| adKeywords | Integer | SP广告词 |
| videoKeywords | Integer | 视频广告词 |
| brandKeywords | Integer | 品牌广告词 |
| badgeLabels | List | 流量来源概览 |
| badgeDetails | Map | 流量来源明细 |
| asinInfo | Object | ASIN 相关信息 |

## ASIN 信息字段

| 字段 | 类型 | 说明 |
|------|------|------|
| asin | String | ASIN |
| asinUrl | String | ASIN 链接 |
| currency | String | 货币 |
| price | Float | 价格 |
| rating | Float | 评分 |
| reviews | Integer | 评分数 |
| title | String | 标题 |
| sku | String | SKU |
| variations | Integer | 变体数 |
| nodeId | String | 节点ID |
| nodeIdPath | String | 节点路径 |
| nodeLabelPath | String | 节点名称 |
| bsrRank | Integer | BSR排名 |

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "month": "202604",
    "q": "B07Z82895W",
    "page": 1,
    "size": 50
  }
}
```

## CLI 使用示例

```bash
# 基本用法
sellersprite traffic source 202604 --q B07Z82895W

# 使用 --asin 参数
sellersprite traffic source 202604 --asin B07Z82895W

# 带排序
sellersprite traffic source 202604 --asin B07Z82895W --order-field keywords --order-desc
```