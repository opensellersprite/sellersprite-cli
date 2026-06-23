# trademark_list

## 描述

查询商标列表数据，支持文本、图片、品牌名、状态、申请人、尼斯分类等多维度筛选。

## MCP 调用名称

`mcp__sellersprite__trademark_list`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | office | List |  | 数据范围，见上一个接口，["US"] |
| 2 | text | String | ✓ | 查询文本，CHINESE |
| 3 | imageBase64 | String |  | base64字符串 |
| 4 | imageFile | File |  | 上传的文件，C:\fakepath\人像.jpeg |
| 5 | brandName | List |  | 品牌名，字段参数见统计接口，["ADVENTURE CLUB"] |
| 6 | status | List |  | 状态，字段参数见统计接口，["Registered"] |
| 7 | applicant | List |  | 申请人，字段参数见统计接口，["ANKER INC"] |
| 8 | niceClass | List |  | 尼斯分类，字段参数见统计接口，[5] |
| 9 | applicationYear | List |  | 申请年份，字段参数见统计接口，["1985"] |
| 10 | expiryYear | List |  | 过期年份，字段参数见统计接口，["2026"] |
| 11 | order.field | String |  | 排序字段，默认相关度，applicationDate申请日期 |
| 12 | order.desc | Boolean |  | true降序，false升序，默认true |
| 13 | page | Integer |  | 页码，1 |
| 14 | size | Integer |  | 每页条数，最大100，20 |

## 基本信息

- **MCP Code**: `trademark_list`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/global/brand/list`
- **说明**: 查询商标列表数据

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | id | String | id，US502022097612203 | |
| 2 | applicant | List | 申请人，ANKER INC | |
| 3 | applicantCountryCode | Integer | 申请人国家，US | |
| 4 | applicants | List | 申请人详情，格式同office | |
| 5 | └kind | String | 类型，Legal Entity | |
| 6 | └identifier | String | 标识，33744042 | |
| 7 | └countryCode | String | 国家编码，US | |
| 8 | └contact | JSONObject | 联系方式 | |
| 9 | └fullAddress | List | 完整地址 | |
| 10 | └└text | String | 描述 | |
| 11 | └└languageCode | String | 语言，en | |
| 12 | └└imageUrl | String | 图片URL，https://o.sellersprite.com/w/brands/ustm/US502022097612203/ee45f.jpg | |
| 13 | └fullName | List | 完整名称 | |
| 14 | └└text | String | 描述，ANKER INC | |
| 15 | └└languageCode | String | 语言，en | |
| 16 | applicationDate | String | 申请日期，2022-09-29 | |
| 17 | applicationLanguageCode | String | 申请语言，en | |
| 18 | applicationNumber | String | 申请编号，97612203 | |
| 19 | registrationNumber | String | 注册号，4590785 | |
| 20 | applicationRefNumber | List | 申请参考号 | |
| 21 | brandName | List | 品牌名，[ "1ST AID"] | |
| 22 | collection | String | 数据集，ustm | |
| 23 | designatedCountries | List | 指定国家，["US"] | |
| 24 | designation | List | 指定国家，["US"] | |
| 25 | filingPlace | String | 申请地点 | |
| 26 | kind | List | 商标类别，["Individual"] | |
| 27 | logos | List | logo | |
| 28 | └logo | String | logo | |
| 29 | └logoUrl | String | logo url | |
| 30 | markFeature | String | 商标种类，Combined | |
| 31 | niceClass | List | 尼斯分类，[5] | |
| 32 | office | String | 知识产权局，US | |
| 33 | status | String | 状态，Pending | |
| 34 | statusDate | String | 状态更新日期，2023-05-02 | |
| 35 | type | String | 类型，TRADEMARK | |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/global/brand/list' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{}'
```
