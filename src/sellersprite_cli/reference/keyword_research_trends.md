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

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `keyword` | string | 是 | 关键字 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |

## 基本信息

- **MCP Code**: `keyword_research_trends`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/keyword-research/trends`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| time | String | 时间（按月，从2017年01月起） |
| keywrod | String | 关键词（注意原始拼写有误） |
| keywrodCn/keywrodJp | String | 中文/日文翻译 |
| search | Integer | 搜索量 |
| purchase | BigDecimal | 购买量 |
| purchaseRate | BigDecimal | 购买率 |
| yearlyGrowth | BigDecimal | 同比增长率 |
| chainGrowth | BigDecimal | 环比增长率 |
| threeMonthGrowth | BigDecimal | 三个月增长率 |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/keyword-research/trends' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keyword":"test"}'
```

