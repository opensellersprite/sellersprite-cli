# product_node

## 描述

查询 Amazon 产品类目信息的工具。
支持通过类目节点路径、类目名称、关键词或节点 ID 搜索类目，
并返回类目的层级路径、名称以及该类目下的商品数量。

适用于以下场景：
- 根据关键词查找对应的 Amazon 类目
- 获取类目的完整层级结构
- 选品前评估类目规模（商品数量）
- 为后续商品搜索或筛选提供类目参数

## MCP 调用名称

`mcp__sellersprite__product_node`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | nodeIdPath | String |  | 类目节点 id 字符串，2619525011:3741271:3741281 |
| 3 | keyword | String |  | 搜索关键字，nodeId或类目名称，Books 或者 4053 |
| 4 | month | String |  | 查询历史月份类目，格式yyyyMM，202502 |

## 基本信息

- **MCP Code**: `product_node`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/product/node`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | nodeIdPath | String | 类目 id 字符串，即 nodeIdPath | 2619525011:3741271 |
| 2 | nodeLabelPath | String | 类目名称 | Appliances:Dishwashers |
| 3 | products | Integer | 类目下产品数 | 42 |
| 4 | nodeLabelLocale | String | 类目节点名称中文 | 洗碗机 |
| 5 | nodeLabelPathLocale | String | 类目所属所有节点名称中文 | 大家电:洗碗机 |

## 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/product/node?marketplace=US&month=202507&nodeIdPath=2619525011:3741271' \
  -H 'secret-key: Your Secret'
```

