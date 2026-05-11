# API 附录

> 来源：https://open.sellersprite.com/appendix

---

## 市场信息（表1.2）

| 代码 | 市场 |
|------|------|
| US | 美国站（USD） |
| JP | 日本站（JPY） |
| UK | 英国站（GBP） |
| DE | 德国站（EUR） |
| FR | 法国站（EUR） |
| IT | 意大利站（EUR） |
| ES | 西班牙站（EUR） |
| CA | 加拿大站（C$） |
| IN | 印度站（INR） |

---

## 查询日期（表1.1）

| 值 | 说明 |
|----|------|
| nearly | 最近30天 |
| yyyyMM | 查询具体月份，如 202507，最多支持前24个月 |

---

## 上架日期（表1.3）

| 值 | 说明 |
|----|------|
| null | 无限制 |
| 1 | 近30天 |
| 3 | 近3个月 |
| 6 | 近半年 |
| 12 | 近1年 |
| 24 | 近2年 |

---

## 商品尺寸分类（美国）

| 代码 | 说明 |
|------|------|
| ST/SS | 小号标准尺寸 |
| LS | 大号标准尺寸 |
| SO | 小号大件 |
| MO | 中号大件 |
| LO/LB | 大号大件 |
| SP | 特殊大件 |
| ELO | 超大尺寸 0-50 磅 |
| EL5O | 50-70 磅 |
| EL7O | 70-150 磅 |
| EL15O | 150 磅以上 |

---

## 卖家所属地（表1.5）

| 代码 | 国家/地区 |
|------|-----------|
| CN | 中国 |
| HK | 中国香港特区 |
| US | 美国 |
| JP | 日本 |
| DE | 德国 |
| FR | 法国 |

---

## 选产品排序字段（表1.6）

| 字段 | 说明 |
|------|------|
| total_units | 月销量 |
| total_amount | 月销售额 |
| bsr_rank | BSR排名 |
| price | 价格 |
| rating | 评分 |
| reviews | 评分数 |
| profit | 毛利率 |
| reviews_rate | 留评率 |
| available_date | 上架时间 |
| questions | Q&A |
| total_units_growth | 月销量增长率 |
| reviews_increasement | 月新增评分数 |
| bsr_rank_cv | 近7天BSR增长数 |

---

## 市场周期（表1.7）

| 代码 | 说明 |
|------|------|
| N | 一般性市场 |
| S1-S3 | 季节性市场（1-3月旺季） |
| S4-S6 | 季节性市场（4-6月） |
| S7-S9 | 季节性市场（7-9月） |
| S10-S12 | 季节性市场（10-12月） |
| I | 持续增长市场 |
| D | 持续衰退市场 |

---

## 关键词选品排序字段（表1.8）

| 字段 | 说明 |
|------|------|
| searches | 月搜索量 |
| keywordsIsHide | 月购买量 |
| searches_growth | 增长率 |
| yearly_growth_rate | 同比增长率 |
| growth_rate_trend_min | 近3个月增长率 |
| monopoly_click_rate | 点击集中度 |
| goods_value | 货流值 |

---

## 流量分析相关

### 曝光位置（表1.10）

| 代码 | 说明 |
|------|------|
| naturalSearching | 自然搜索词 |
| amazonChoice | AC推荐词 |
| editorialRecommendations | ER推荐词 |
| sponsorBrand | 品牌推荐词 |
| sponsorVideo | 视频推荐词 |
| ads | SP广告词 |

### 流量占比类型（表2.0）

| 代码 | 说明 |
|------|------|
| primary | 主要流量词 |
| precise | 精准流量词 |
| preciseLongTail | 转化流失词 |

### 转化类型（表2.1）

| 代码 | 说明 |
|------|------|
| excellent | 转化优质词 |
| stable | 转化平稳词 |
| lost | 转化流失词 |
| invalid | 无效曝光词 |

---

## 关联流量关联类型（表2.2）

| 代码 | 说明 |
|------|------|
| mib | 捆绑销售 |
| fbt | 组合购买 |
| csi | 相似产品 |
| cob | 品牌推荐 |
| bab | 买了又买 |
| vav | 看了又看 |
| avp | 看了还看 |

---

## 流量词列表排序字段（表2.3）

| 字段 | 说明 |
|------|------|
| rankPosition | 自然排名 |
| adPosition | 广告排名 |
| createdTime | 创建时间 |
| searchesRank | 搜索量周排名 |
| purchases | 月购买量 |
| purchaseRate | 购买率 |
| products | 商品数 |
| supplyDemandRatio | 供需比 |
| bid | PPC竞价 |
| trafficPercentage | 流量占比 |

---

## ABA 选品排序字段（表2.4）

| 字段 | 说明 |
|------|------|
| searchfrequencyrank | 现排名 |
| cprExact | SPR |
| titleDensityExact | 标题密度 |
| searches | 搜索量周排名 |

---

## 商品重量单位（表2.7）

| 代码 | 说明 |
|------|------|
| g | 克 |
| kg | 千克 |
| oz | 盎司 |
| lb | 磅 |
