# aba_research_trend

## 描述

基于 Amazon Brand Analytics (ABA) 数据，
分析指定关键词在指定时间范围内的搜索排名变化趋势。

该工具聚焦于：
- 关键词的搜索排名是上升还是下降
- 排名变化的幅度和速度
- 与竞品相比的排名相对位置变化

适合在以下场景调用：
- 监控核心关键词的排名波动
- 判断某个关键词的竞争激烈程度变化
- 分析竞品在特定关键词上的排名趋势
- 评估广告投放和 Listing 优化的效果

## MCP 调用名称

`mcp__sellersprite__aba_research_trend`

## 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `keyword` | string | 是 | 关键字 |
| `marketplace` | string | 是 | Amazon 站点代码（枚举值）：US, JP, UK, DE, FR, IT, ES, CA, IN |

## 基本信息

- **MCP Code**: `aba_research_trend`
- **Method**: `POST`
- **URL**: `https://api.sellersprite.com/v1/aba/research/trend`

## 响应参数

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | String | 关键词 |
| time | String | 时间 |
| searches | Integer | 搜索量 |
| clicks | Integer | 点击量 |
| ctr | Float | 点击率 |
| cvShareRate | Float | 转化共享率 |
| rank | Integer | 排名 |

## 请求示例

```bash
curl -X POST 'https://api.sellersprite.com/v1/aba/research/trend' \
  -H 'secret-key: Your Secret' \
  -H 'Content-Type: application/json' \
  -d '{"marketplace":"US","keyword":"wireless earbuds"}'
```

