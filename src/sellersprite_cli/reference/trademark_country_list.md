# trademark_country_list

## 描述

查询支持商标查询的国家/地区列表。

## MCP 调用名称

`mcp__sellersprite__trademark_country_list`

## 参数



## 基本信息

- **MCP Code**: `trademark_country_list`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/global/brand/range`
- **说明**: 查询支持查询商标的国家数据

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | office | String | 简码，AD | |
| 2 | officeLabel | String | 中文名称，安道尔 | |

## 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/global/brand/range' \
  -H 'secret-key: Your Secret'
```
