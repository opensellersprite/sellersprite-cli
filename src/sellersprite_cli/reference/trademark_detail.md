# trademark_detail

## 描述

查询商标的详细信息。

## MCP 调用名称

`mcp__sellersprite__trademark_detail`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | office | String | ✓ | 数据范围，见上一个接口，US |
| 2 | brandId | String | ✓ | id,见列表接口，US502022097612203 |

## 基本信息

- **MCP Code**: `trademark_detail`
- **Method**: `GET`
- **URL**: `https://api.sellersprite.com/v1/global/brand/detail`
- **说明**: 查询商标的详细信息

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | id | String | id，US502022097612203 | |
| 2 | applicant | List | 申请人，ANKER INC | |
| 3 | applicantCountryCode | Integer | 申请人国家，US | |
| 4 | applicants | List | 申请人详情，格式同office,结构见下表 | |
| 5 | applicationDate | String | 申请日期，2022-09-29 | |
| 6 | applicationLanguageCode | String | 申请语言，en | |
| 7 | applicationNumber | String | 申请编号，97612203 | |
| 8 | registrationNumber | String | 注册号，4590785 | |
| 9 | applicationRefNumber | List | 申请参考号 | |
| 10 | brandName | List | 品牌名，[ "1ST AID"] | |
| 11 | collection | String | 数据集，ustm | |
| 12 | designatedCountries | List | 指定国家，["US"] | |
| 13 | designation | List | 指定国家，["US"] | |
| 14 | filingPlace | String | 申请地点 | |
| 15 | kind | List | 商标类别，["Individual"] | |
| 16 | logos | List | logo | |
| 17 | └logo | String | logo | |
| 18 | └logoUrl | String | logo url | |
| 19 | markFeature | String | 商标种类，Combined | |
| 20 | niceClass | List | 尼斯分类，[5] | |
| 21 | office | String | 知识产权局，US | |
| 22 | status | String | 状态，Pending | |
| 23 | statusDate | String | 状态更新日期，2023-05-02 | |
| 24 | type | String | 类型，TRADEMARK | |
| 25 | appeals | List | 上诉信息 | |
| 26 | └date | String | 日期 | |
| 27 | └kind | String | 分类 | |
| 28 | correspondence | AddressDto | 通信地址 | |
| 29 | events | List | 事件 | |
| 30 | └date | String | 日期 | |
| 31 | └officeKind | String | 产权局分类 | |
| 32 | └gbdKind | String | 品牌分析 | |
| 33 | └doc | String | 文档 | |
| 34 | └country | String | 国家 | |
| 35 | expiryDate | String | 过期时间 | |
| 36 | extra | String | 扩展信息 | |
| 37 | gbdStatus | String | 品牌状态 | |
| 38 | goodsServicesClassification | Object | 商品分类信息 | |
| 39 | └kind | String | 类型 | |
| 40 | └version | String | 版本 | |
| 41 | └classification | String | 详情 | |
| 42 | └└code | String | code码 | |
| 43 | └└terms | Map | 说明 | |
| 44 | goodsServicesUnclassified | Map | 商品未分类信息 | |
| 45 | markDescriptionDetails | List | 商标描述细节 | |
| 46 | └text | String | 描述，ANKER INC | |
| 47 | └languageCode | String | 语言，en | |
| 48 | markDisclaimerDetails | List | 商标免责声明 | |
| 49 | └text | String | 描述，ANKER INC | |
| 50 | └languageCode | String | 语言，en | |
| 51 | markImageDetails | JSONArray | 商标图形分类 | |
| 52 | nationalGoodsServicesClassification | Object | 国际商品分类信息 | |
| 53 | └kind | String | 类型 | |
| 54 | └version | String | 版本 | |
| 55 | └classification | String | 详情 | |
| 56 | └└code | String | code码 | |
| 57 | └└terms | Map | 说明 | |
| 58 | officeStatus | String | 办公状态 | |
| 59 | priorities | List | 优先事项 | |
| 60 | └severity | String | 级别 | |
| 61 | └code | String | code码 | |
| 62 | └field | String | 字段 | |
| 63 | └type | String | 类型 | |
| 64 | └message | String | 说明 | |
| 65 | publicationDate | String | 发表日期 | |
| 66 | publications | List | 发表详情 | |
| 67 | └date | String | 日期 | |
| 68 | └identifier | String | 标志 | |
| 69 | └section | String | 内容 | |
| 70 | qc | List | 审核意见 | |
| 71 | └severity | String | 级别 | |
| 72 | └code | String | code码 | |
| 73 | └field | String | 字段 | |
| 74 | └type | String | 类型 | |
| 75 | └message | String | 说明 | |
| 76 | reference | Object | 参考信息 | |
| 77 | └office | String | 机构code | |
| 78 | └application | Object | 申请信息 | |
| 79 | └└date | String | 日期 | |
| 80 | └└number | String | 编号 | |
| 81 | └registration | Object | 注册信息 | |
| 82 | └└date | String | 日期 | |
| 83 | └└number | String | 编号 | |
| 84 | refOffice | String | 参考办公室 | |
| 85 | registrationDate | String | 注册日期 | |
| 86 | registrationOfficeCode | String | 注册国家 | |
| 87 | registrationRefNumber | List | 注册参考号 | |
| 88 | representatives | List | 代表信息 | |
| 89 | secondLanguageCode | String | 第二语言 | |
| 90 | st13 | String | id | |
| 91 | terminationDate | String | 终止日期 | |
| 92 | wordMarkSpecification | Object | 文字商标说明 | |
| 93 | └markTransliteration | String | markTransliteration | |
| 94 | └markTranslation | Object | 商标翻译 | |
| 95 | └└text | String | 内容 | |
| 96 | └└languageCode | String | 语言类型 | |
| 97 | └markVerbalElement | Object | markVerbalElement | |
| 98 | └└text | String | 内容 | |
| 99 | └└languageCode | String | 语言类型 | |
| 100 | └markSignificantVerbalElement | Object | markSignificantVerbalElement | |
| 101 | └└text | String | 内容，SONICARE | |
| 102 | └└languageCode | String | 语言类型，en | |

## 请求示例

```bash
curl -X GET 'https://api.sellersprite.com/v1/global/brand/detail' \
  -H 'secret-key: Your Secret'
```
