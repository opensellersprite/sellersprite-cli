# SellerSprite CLI

<p align="center">
  <b>卖家精灵开放平台 MCP 官方 CLI</b><br>
  <sub>交互式终端工具 + Python MCP 客户端 + 27 个 AI Skills，通过 MCP 调用全部 43 个 Amazon 数据工具</sub><br>
  <span style="color: #27ae60;"><b>CLI 完全免费</b></span> · <code>pip install</code> 即可使用
</p>

---

## 🔥 MCP 服务限时特惠

前往 [卖家精灵开放平台](https://open.sellersprite.com/pricing/mcp) 购买密钥，一价解锁 43 个 Amazon 数据工具：

| 周期 | 套餐 | 特惠价 | 原价 | 速率 | 月额度 | 用户数 |
|------|------|--------|------|------|--------|--------|
| **月付** | Basic | **¥99** | ¥199 | 40 次/分钟 | 1,000 次 | 1 个密钥 |
| 月付 | Pro | **¥299** | ¥599 | 40 次/分钟 | 4,000 次 | 1 个密钥 |
| 月付 | Max | **¥599** | ¥1,199 | 40 次/分钟 | 10,000 次 | 1 个密钥 |
| **季付** | Basic | **¥297** | ¥597 | 40 次/分钟 | 1,000 次 | 1 个密钥 |
| 季付 | Pro | **¥499** | ¥999 | 40 次/分钟 | 4,000 次 | 1 个密钥 |
| 季付 | Max | **¥990** | ¥1,990 | 40 次/分钟 | 10,000 次 | 1 个密钥 |
| **年付** | Basic | **¥990** | ¥1,990 | 40 次/分钟 | 4,000 次 | 1 个密钥 |
| 年付 | Pro | **¥1,990** | ¥3,999 | 60 次/分钟 | 10,000 次 | 1 个密钥 |
| 年付 | Max | **¥2,990** | ¥5,990 | 80 次/分钟 | 15,000 次 | 1 个密钥 |

> 🎁 **618 限时活动**（2026.06.06 - 2026.06.20）：购买年套餐，额外获赠相同规格的 1 个月 Agent 服务。
>
> 💡 购买密钥后，通过本 CLI 即可调用全部接口，无需再按 API 单独付费。Token 消耗直降 90%+。

## 📚 接口文档

完整 MCP 接口文档见：[https://open.sellersprite.com/api](https://open.sellersprite.com/api)

## 🚀 在 Claude Code 一键安装 27 个 Skills

通过 [ClawHub](https://clawhub.ai/opensellersprite/sellersprite-skills) 一行命令导入到 Claude Code（需先安装 Node.js）：

```bash
# 全局安装（推荐 · 所有项目可用）
npx clawhub@latest install opensellersprite/sellersprite-skills

# 项目级安装（团队共享 · 提交到 .claude/skills/ 后队友自动同步）
npx clawhub@latest install opensellersprite/sellersprite-skills --project
```

安装后**重启 Claude Code**，即可使用：

```
/product-research wireless earbuds    # 智能选品
/market-analysis earbuds US           # 市场全景
/competitor-analysis B0XXX            # 竞品拆解
# ...另外 7 个 /命令 + 17 个对话触发的战术选品卡
```

> 完整技能清单见 [skills/README.md](src/sellersprite_cli/skills/README.md)。Skills 由 Claude Code 直接执行，调用本 CLI 的 MCP 工具拿数据 —— 需要先 `pip install sellersprite-cli` 并配置密钥（见下文）。

## 安装

> **要求：** Python ≥ 3.10

```bash
pip install sellersprite-cli
```

### 国内镜像加速

临时使用清华镜像：

```bash
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple sellersprite-cli
```

设为默认（升级 pip 后配置）：

```bash
python -m pip install --upgrade pip
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

## 配置密钥

```bash
sellersprite config --key 你的API密钥
```

或交互式输入（密钥不会回显）：

```bash
sellersprite config
```

密钥在 [卖家精灵开放平台](https://open.sellersprite.com) 获取。

配置会保存到全局 `.env` 文件，所有项目共享：

- **Linux / macOS**: `~/.config/sellersprite/.env`
- **Windows**: `%APPDATA%\sellersprite\.env`

### 项目级密钥覆盖

如需为当前项目单独配置密钥（不影响全局），加 `--project`：

```bash
sellersprite config --key 项目密钥 --project
```

这会保存到当前目录的 `.env` 文件。读取优先级：**项目 `.env` > 全局 `.env`**。

也可以直接编辑 `.env` 文件：

```
SELLERSPRITE_KEY=你的API密钥
```

## CLI 使用

### 交互式 TUI

```bash
sellersprite               # 无参数启动交互式菜单
```

### 域命令（43 个工具）

```bash
# ASIN 分析
sellersprite asin detail B0D6LQ5VZM
sellersprite asin predict B0D6LQ5VZM
sellersprite asin coupon B0D6LQ5VZM
sellersprite asin keepa B0D6LQ5VZM --daily-latest true --start-timestamp 1722470400000 --end-timestamp 1754006400000
sellersprite asin sales-trend B0D6LQ5VZM

# 商品与竞品
sellersprite product search --keyword "wireless earbuds" --min-price 10 --max-price 30
sellersprite product competitor --asins B0XXX1,B0XXX2
sellersprite product node --keyword earbuds

# 关键词
sellersprite keyword mine --keyword earbuds --size 20
sellersprite keyword research --keywords earbuds
sellersprite keyword order --reverse-type M --date 202501 --asins B0XXX1,B0XXX2
sellersprite keyword bsr 10000 172282
sellersprite keyword trends earbuds

# 流量
sellersprite traffic keyword B0XXX1
sellersprite traffic keyword-stat B0XXX1 --month 202501
sellersprite traffic source --month 202501 --asin B0XXX1
sellersprite traffic source --month 202501 --asin B0XXX1 --size 50
sellersprite traffic listing --asin-list B0XXX1 --relations also_bought
sellersprite traffic extend --asin-list B0XXX1

# 市场分析
sellersprite market research --keyword earbuds
sellersprite market stats --node-id-path "172282:24046923011"
sellersprite market price --node-id-path "172282:24046923011"
sellersprite market brand --node-id-path "172282:24046923011"
sellersprite market demand --node-id-path "172282:24046923011"
# ... 共 14 个市场分析命令

# ABA / 趋势
sellersprite trend aba-weekly --keyword-list earbuds,buds
sellersprite trend aba-monthly --keyword-list earbuds
sellersprite trend aba-monthly --keyword-list earbuds
sellersprite trend aba-trend earbuds
sellersprite trend google --keyword earbuds
sellersprite trend review B0D6LQ5VZM --star-list 4,5

# 商标查询
sellersprite trademark countries

# --office 支持单个或多个（逗号分隔），trademark_detail 除外
sellersprite trademark list ANKER --office US
sellersprite trademark list ANKER --office US,EU

# --brand-name 同样支持逗号分隔
sellersprite trademark list ANKER --office US --brand-name ANKER
sellersprite trademark list ANKER --office US --brand-name ANKER,EUFY

# 图片搜索
sellersprite trademark list ANKER --office US --image-file ./logo.png

sellersprite trademark stats --office US ANKER
sellersprite trademark stats --office US,EU ANKER
sellersprite trademark detail BRAND_ID --office US
```

### 参数注意事项

1. **参数命名层级**
   - CLI 选项使用 **kebab-case**：`--start-timestamp`
   - Python 方法参数使用 **snake_case**：`start_timestamp`
   - 接口入参使用 **camelCase**：`startTimestamp`
   - 转换由 CLI / `mcp_client.py` 自动处理，正常使用时无需关心。

2. **`extra key=value` 传参必须用 snake_case**

   `extra` 参数会经过 `_req()` 自动转 camelCase，但只对带下划线的 key 生效。

   如果某个字段是 List 类型（如 `status`、`nice_class`、`brand_name`），在 `extra` 中用逗号分隔即可：

   ```bash
   # ✅ 正确：单个值
   sellersprite product search --keyword earbuds extra="min_price=10 max_price=30"

   # ✅ 正确：List 类型用逗号分隔
   sellersprite trademark list ANKER --office US extra="status=Registered,Pending nice_class=9,11"

   # ❌ 错误，kebab-case 不会转换
   sellersprite product search --keyword earbuds extra="min-price=10"
   ```

3. **`--daily-latest` 接受 true/false 字符串**

   ```bash
   sellersprite asin keepa B0D6LQ5VZM --daily-latest true
   sellersprite asin keepa B0D6LQ5VZM --daily-latest false
   ```

4. **时间戳单位是毫秒**

   `asin keepa` 的 `--start-timestamp` / `--end-timestamp` 为毫秒时间戳：

   ```bash
   sellersprite asin keepa B0D6LQ5VZM \
     --start-timestamp 1722470400000 \
     --end-timestamp 1754006400000
   ```

5. **月份格式为 `yyyyMM`**

   涉及月份的参数（如 `--month`）统一使用 `yyyyMM`，例如 `202501`、`202604`。

6. **分页参数使用 `--page` 和 `--size`**

   以下命令支持分页，默认每页条数因接口而异，最大一般不超过 100：

   ```bash
   # 商品筛选
   sellersprite product search --keyword earbuds --size 50 --page 1

   # 流量词列表
   sellersprite traffic keyword B0XXX1 --size 100 --page 1

   # 流量来源
   sellersprite traffic source --month 202501 --asin B0XXX1 --size 50 --page 1

   # 评论查询
   sellersprite trend review B0D6LQ5VZM --star-list 4,5 --size 10 --page 1

   # ABA 数据
   sellersprite trend aba-weekly --keyword-list earbuds,buds --size 40 --page 1
   sellersprite trend aba-monthly --keyword-list earbuds --size 15 --page 1
   ```

7. **列表型选项支持逗号分隔**

   接受多个值的选项（如 `trademark list` 的 `--office`、`--brand-name`，以及 `--asin-list`、`--keyword-list`）均可用逗号分隔一次性传入。

   注意：`trademark detail` 的 `--office` 为单字符串，不要传逗号分隔：

   ```bash
   sellersprite trademark list ANKER --office US,EU
   sellersprite trademark list ANKER --office US --brand-name ANKER,EUFY
   sellersprite traffic listing --asin-list B0XXX1,B0XXX2 --relations also_bought,also_viewed

   # detail 的 office 是单字符串
   sellersprite trademark detail BRAND_ID --office US
   ```

### 其他命令

```bash
sellersprite list                              # 列出所有 43 个工具
sellersprite skill list                        # 列出 27 个 Skills
sellersprite skill show --name product-research # 查看某个 Skill 内容

# 查看接口参数文档
sellersprite docs trademark_list               # 查看商标列表接口的参数表
sellersprite docs product_research             # 查看选产品接口的参数表

# 生成 AI 客户端配置
sellersprite init claude-code --skills         # Claude Code
sellersprite init cursor --skills              # Cursor
sellersprite init --all --skills               # 全部客户端
sellersprite init --dry-run                    # 预览模式
```

### 查看接口文档

```bash
sellersprite docs <工具名>
```

例如：

```bash
sellersprite docs asin_sales_trend
sellersprite docs trademark_list
sellersprite docs traffic_keyword
```

`docs` 命令会从 `src/sellersprite_cli/reference/` 或 `docs/mcp-api-source.md` 中读取接口文档，以表格形式展示请求参数。对于支持 `extra key=value` 传参的命令，可通过 `docs` 查看可用的字段名和类型。

### 全局参数

| 参数 | 说明 |
|------|------|
| `--key, -k` | API 密钥 |
| `--marketplace, -m` | 站点代码（默认 US） |

支持站点：`US`、`JP`、`UK`、`DE`、`FR`、`IT`、`ES`、`CA`、`IN`

## Python MCP 客户端

```python
from sellersprite_cli import SellerSprite

ss = SellerSprite()

# 搜索类目
nodes = ss.product_node(keyword="wireless earbuds")

# ASIN 详情
detail = ss.asin_detail(asin="B0D6LQ5VZM")

# 商品筛选
result = ss.product_research(keyword="earbuds", priceMin=10, priceMax=30)

# 切换站点
ss_jp = SellerSprite(marketplace="JP")
```

## AI Skills（27 个）

### 综合分析（10 个）

| 命令 | 说明 |
|------|------|
| 智能选品助手 | 按多维条件筛选潜力商品 |
| 市场全景分析 | 11 个维度的全方位市场评估 |
| 竞品深度拆解 | 8 大维度全面拆解竞品 |
| 关键词选品研究 | 基于关键词的市场需求分析 |
| Listing 优化诊断 | 发现关键词覆盖缺口 |
| 流量结构分析 | 拆解自然/广告/推荐流量 |
| 蓝海机会挖掘 | 通过 ABA 趋势发现机会 |
| 买家评论洞察 | 提炼痛点和改进方向 |
| 定价策略分析 | 价格带分布与最优定价 |
| 广告投放优化 | PPC 策略、竞价和否词 |

### 战术选品（17 个）

新品爆发、关键词趋势、产品缺陷、类目结构、流量防伪、机会捕捉

通过 `sellersprite skill list` 查看完整列表。

## 支持客户端

`claude-code`、`cursor`、`cline`、`claude-desktop`、`vscode`、`windsurf`、`trae`、`codex`、`antigravity`、`openclaw`

## 许可证

[MIT License](LICENSE)
