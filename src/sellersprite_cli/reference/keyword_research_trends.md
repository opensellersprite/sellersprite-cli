# keyword_research_trends

## 描述

基于 Amazon 站内搜索行为数据，
分析指定关键词随时间的搜索热度变化趋势。

该工具用于判断：
- 某个关键词的搜索热度是上升、下降还是平稳
- 是否存在季节性波动或周期性规律
- 与历史同期相比，当前需求处于什么水平

适合在以下场景调用：
- 验证关键词的长期需求稳定性
- 判断是否为季节性关键词
- 对比不同关键词的增长趋势
- 分析市场需求的长期变化方向

## MCP 调用名称

`mcp__sellersprite__keyword_research_trends`

## 参数

| # | 参数 | 类型 | 必填 | 说明 |
|---|------|------|------|------|
| 1 | marketplace | String | ✓ | 市场，见表 1.2 |
| 2 | keyword | String | ✓ |  |

## 基本信息

- **MCP Code**: `keyword_research_trends`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-research/trends`

## 响应参数

| # | 字段 | 类型 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | time | String | 时间 |  |
| 2 | keywrod | String | 关键词 |  |
| 3 | keywrodCn | String | 关键词-中文 |  |
| 4 | keywrodJp | String | 关键词-日文 |  |
| 5 | search | Integer | 搜索量 |  |
| 6 | purchase | BigDecimal | 购买量 |  |
| 7 | purchaseRate | BigDecimal | 购买率 |  |
| 8 | yearlyGrowth | BigDecimal | 同比增长率 |  |
| 9 | chainGrowth | BigDecimal | 环比增长率 |  |
| 10 | threeMonthGrowth | BigDecimal | 三个月增长率 |  |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword-research/trends' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keyword":"test"}'
```

