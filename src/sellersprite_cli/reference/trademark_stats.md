# trademark_stats

## 描述

查询商标统计数据，获取按知识产权局、品牌名、状态、申请人、尼斯分类、申请年份、过期年份等维度的聚合结果。

## MCP 调用名称

`mcp__sellersprite__trademark_stats`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | office | List | ✓ | 数据范围，见上一个接口，["US"] |
| 2 | text | String | ✓ | 查询文本，CHINESE |
| 3 | imageBase64 | String |  | base64字符串 |
| 4 | imageFile | File |  | 上传的文件，C:\fakepath\人像.jpeg |

## 基本信息

- **MCP Code**: `trademark_stats`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/global/brand/stats`
- **说明**: 查询商标统计数据

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | office | List | 知识产权局，[{"key":"US","count":2}] | |
| 2 | └key | String | 值，US | |
| 3 | └count | Integer | 数量，2 | |
| 4 | brandName | List | 品牌名，格式同office | |
| 5 | └key | String | 值，ADVENTURE CLUB | |
| 6 | └count | Integer | 数量，4 | |
| 7 | status | List | 状态，格式同office | |
| 8 | └key | String | 值，Registered | |
| 9 | └count | Integer | 数量，12 | |
| 10 | applicant | List | 申请人，格式同office | |
| 11 | └key | String | 值，ANKER INC | |
| 12 | └count | Integer | 数量，4 | |
| 13 | niceClass | List | 尼斯分类，格式同office | |
| 14 | └key | String | 值，5 | |
| 15 | └count | Integer | 数量，2 | |
| 16 | └label | String | 分类名称，医药用品 | |
| 17 | applicationYear | List | 申请年份，格式同office | |
| 18 | └key | String | 值，1985 | |
| 19 | └count | Integer | 数量，5 | |
| 20 | expiryYear | List | 过期年份，格式同office | |
| 21 | └key | String | 值，2026 | |
| 22 | └count | Integer | 数量，2 | |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/global/brand/stats' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{}'
```
