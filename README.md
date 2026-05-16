# SellerSprite CLI

<p align="center">
  <b>卖家精灵开放平台 MCP 官方 CLI</b><br>
  <sub>交互式终端工具 + Python MCP 客户端 + 27 个 AI Skills，通过 MCP 调用全部 38 个 Amazon 数据工具</sub><br>
  <span style="color: #27ae60;"><b>CLI 完全免费</b></span> · <code>pip install</code> 即可使用
</p>

---

## 🔥 MCP 服务限时特惠

前往 [卖家精灵开放平台](https://open.sellersprite.com/pricing/mcp) 购买密钥，一价解锁 38 个 Amazon 数据工具：

| 套餐 | 价格 | 速率 | 月额度 | 用户数 |
|------|------|------|--------|--------|
| **限时特惠 - 月** | **¥99**（原价 ¥199） | 40 次/分钟 | 1,000 次 | 1 个密钥 |
| 限时特惠 - 半年 | ¥594（原价 ¥1,194） | 40 次/分钟 | 1,000 次 | 1 个密钥 |
| Basic - 年付 | ¥990（原价 ¥1,990） | 40 次/分钟 | 6,000 次 | 1 个密钥 |
| Pro - 年付 | ¥1,990（原价 ¥3,990） | 80 次/分钟 | 15,000 次 | 3 个密钥 |

> 💡 购买密钥后，通过本 CLI 即可调用全部接口，无需再按 API 单独付费。Token 消耗直降 90%+。

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

```bash
pip install sellersprite-cli
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

以上命令会自动将密钥保存到当前目录的 `.env` 文件中， sellersprite 会自动读取。

你也可以手动设置环境变量：

```bash
# Linux / macOS
export SELLERSPRITE_KEY="你的API密钥"

# Windows CMD
set SELLERSPRITE_KEY=你的密钥

# Windows PowerShell
$env:SELLERSPRITE_KEY = "你的API密钥"
```

## CLI 使用

### 交互式 TUI

```bash
sellersprite               # 无参数启动交互式菜单
```

### 域命令（38 个工具）

```bash
# ASIN 分析
sellersprite asin detail B0D6LQ5VZM
sellersprite asin predict B0D6LQ5VZM
sellersprite asin coupon B0D6LQ5VZM
sellersprite asin keepa B0D6LQ5VZM

# 商品与竞品
sellersprite product search --keyword "wireless earbuds" --min-price 10 --max-price 30
sellersprite product competitor --asins B0XXX1,B0XXX2
sellersprite product node --keyword earbuds

# 关键词
sellersprite keyword mine --keyword earbuds --size 20
sellersprite keyword research --keyword earbuds
sellersprite keyword order --asins B0XXX1,B0XXX2
sellersprite keyword bsr 10000 172282
sellersprite keyword trends earbuds --month 2025-01

# 流量
sellersprite traffic keyword --asin-list B0XXX1,B0XXX2
sellersprite traffic keyword-stat B0XXX1 --month 2025-01
sellersprite traffic source --asin B0XXX1
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
sellersprite trend review B0D6LQ5VZM 172282
```

### 其他命令

```bash
sellersprite list                              # 列出所有 38 个工具
sellersprite skill list                        # 列出 27 个 Skills
sellersprite skill show --name product-research # 查看某个 Skill 内容

# 生成 AI 客户端配置
sellersprite init claude-code --skills         # Claude Code
sellersprite init cursor --skills              # Cursor
sellersprite init --all --skills               # 全部客户端
sellersprite init --dry-run                    # 预览模式
```

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
