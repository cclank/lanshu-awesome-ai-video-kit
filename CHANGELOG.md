# Changelog

按 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 规范。

## [Unreleased]

### Fixed · 2026-10-07 模型规格勘误（用户指正）
- **Seedance 2.5**：`max_duration` 15s → **30s**（官方规格 4–30s，可延长）
- **MiniMax H3**：`max_duration` 4s → **15s**（官方规格 4–15s）
- **新增 Wan 3.0（通义万相）**：2026-08-24 正式发布，30s 单次生成，文档/多模态输入；prompt 收集中（0 条）
- 模型总数 22 → 23

### Added · 2026-10-06 晚间增补（10-03 ~ 10-06 新内容扫描）
- **+7 条提示词**（484 条分散 prompt）：Veo 3（ve-028..031）、Sora 2（so-024..026）
- 来源：sifuyik Substack 病毒视频 prompt 系列 #751–#758（reputable-3rd-party）；来源为模型无关 prompt，模型归属为编辑指派，日期为相对时间推算
- Reka Rho-1（10-05）仅 research preview，无公开访问，未入库

### Added · 2026-10-06 prompt 集中收录（近 3 个月，重点 9-06 ~ 10-06）
- **+44 条提示词**（477 条分散 prompt；另修复 9 条历史分类断裂引用 `dialogue`→`dialogue-driven`、`character-animation`→`portrait`）
- **+6 新模型**：Kling 4.0（k4-001..012）、MiniMax H3（mx-001..010）、Seedance 2.5（se-001..004）、Wan 2.6（w2-001）、Runway Aleph 2.0（ra-001..002）、Luma Ray 3.2（lu-001..002）
- **存量模型补充**：Veo 3（ve-021..027）、Sora 2（so-021..023）、Gemini Omni（gm-011..012）、Higgsfield Soul（hg-009）
- **+1 新分类**：`technique-snippet`（技巧片段与提示词语法）
- 10 条附官方/作者演示视频链接（见各条 notes）
- 各模型 README 新增"🆕 2026-10 新增"区；6 个新模型各建独立索引页


## [0.8.0] — 2026-05-25 · 4 大开源模型完整收录 + 英文化 + awesome 投稿

### Added · 4 大开源 / 开源友好模型(11 → 15)

| 模型 | 厂商 | 协议 | 看家本领 |
|---|---|---|---|
| **LTX-Video 0.9.7** | Lightricks | Apache 2.0 | 实时生成 — 5s 视频在 5s 内生成,30FPS 1216×704 |
| **Mochi 1** | Genmo | Apache 2.0 | 10B 最大开源 AsymmDiT + 强 prompt 遵循 |
| **CogVideoX 5B / 1.5** | 智谱 · 清华 | Apache 2.0 | 226 token 长 prompt + 768×1360 + T2V/I2V 双权重 |
| **Higgsfield Soul / DoP** | Higgsfield AI | 部分开源 | Soul ID 角色一致性 + DoP 模板 + AI Director 60-90s |

- **JSON 扩展**: prompts/data/all-prompts.json
  - +4 个 model 元数据(`ltx-video` / `mochi-1` / `cogvideox-5b` / `higgsfield-soul`)
  - +32 条精选提示词:`lt-001..008`(LTX 单段 prose / screenplay 对话 / 实时迭代)、`mo-001..008`(Mochi 物理细节)、`cg-001..008`(CogVideoX 长 prompt T2V/I2V)、`hg-001..008`(Higgsfield Soul ID / DoP 模板 / AI Director 60-90s 短片)
  - 269 → **301 prompts**;11 → **15 models**;schema_version: 1.4 → 1.5
- **新方法论**: [`methodology/14-四大开源模型速查.md`](methodology/14-四大开源模型速查.md)
  - 4 个开源模型公式对照 + 本地部署指南(GitHub / HuggingFace / ComfyUI / Modal)
  - 物理 vs 情感、短指令 vs 长描述、Soul ID 占位符等独家用法
  - **15 模型完整选型决策树**(本地部署 / 商业 API / 角色一致 / 60s+ 短片 4 大分支)
  - 4 大开源横向对比矩阵(时长/分辨率/提示词风格/FPS/参数量/I2V/中文/许可)
- **Web 工具升级**(`tools/prompt-browser/index.html`):
  - 加 4 个模型色 token(LTX 黄绿 / Mochi 玫红 / CogVideoX 蓝 / Higgsfield 紫品)
  - model-dot / meta-pill / MODEL_META / modelOpts 全部扩到 15
- **主页升级**(`index.html`):
  - Hero stats: 269/11/6/13 → **301/15/7/14**
  - MODELS 数组扩到 15 条,加 4 大开源 model-card(带本地部署 CTA)
  - description / nav 同步到 15 模型
- **监控扩展**(`scripts/model_endpoints.yaml`):
  - 加 4 大开源模型端点(GitHub releases.atom / HuggingFace model card / 官网 prompt guide)
  - 监控覆盖:11 模型 23 端点 → **15 模型 32 端点**
- **资源清单升级**(`RESOURCES.md`):
  - 加 4 大开源专属 section,每个含官方 GitHub / HuggingFace / 部署指南 / 社区讨论

### Added · 国际化与发布准备
- **英文 README**(`README.en.md`): 与中文 README 同结构的国际化版本,15 模型完整介绍 + awesome 标签
- **awesome 投稿稿**(`awesome.md`): 符合 sindresorhus/awesome 格式的目录,可直接 PR 到上游 awesome-claude-code / awesome-ai-video-generation
- 主 README 顶部加 🌍 **English README** 跳转

### Why
- **完整性闭环**: 商业模型固然强,但开源才是真正的底座(本地部署 + LoRA + 二次开发)。少了开源这块,"awesome 全集"名不副实
- **真正的全球受众**: 中文已成型,英文版打开全球开发者市场,准备投递 awesome-lists 上游
- **决策树升级**: 15 模型版决策树覆盖"本地 vs 商业 / 实时 vs 高分 / Soul ID vs Avatar / 60s 短片"等真实场景

### 全项目状态
- 文件:**50+** | Prompt 资产:**411**(301 分散 + 110 跨模型)
- 模型:**15**(11 商业 + 4 开源) | Skill:**7** | 方法论:**14** | Web 工具:3
- 端点监控:**32** | Issue 模板:4 | PR 模板:1

---

## [0.7.0] — 2026-05-25 · 社区驱动 + 自动监控

### Added · 社区贡献基础设施
- **Cross-Model 视频展示槽位**(`tools/cross-model/index.html`):
  - 已实测 → 绿色发光按钮 "▶ 实测视频" + 星级评分 + 测试人/日期
  - 未实测 → 灰色虚线 "🎬 待实测 · 欢迎贡献" 链接到 CONTRIBUTING
- **4 个 Issue Template**(`.github/ISSUE_TEMPLATE/`):
  1. 🎬 贡献实测视频(场景 + 模型 + URL + 评分 + 描述,表单式)
  2. 🚀 发现新模型 / 新版本(已收录新版/版本号过时/新模型应收录)
  3. 💡 贡献新提示词(模型 + 标题 + prompt + 标签 + 推荐参数)
  4. ⚙️ config.yml(禁用 blank issue + 引导 Discussions)
- **PR Template**(`.github/pull_request_template.md`):8 类贡献清单 + 自查清单 + 关联 issue

### Added · 11 模型版本自动监控
- **[`scripts/monitor_models.py`](scripts/monitor_models.py)** — Python 版本监控核心
  - 抓取 11 模型 × 23 个官方端点
  - 噪音清洗(timestamps / nonces / sessions)
  - SHA-256 hash 对比 baseline
  - 自动提取页面中的版本号关键词作为提示
  - 4 种运行模式:default / `--ci` / `--rebaseline` / `--issue-body`
- **[`scripts/model_endpoints.yaml`](scripts/model_endpoints.yaml)** — 11 模型 23 端点配置
- **[`scripts/known_hashes.json`](scripts/known_hashes.json)** — hash baseline(由 CI 自动维护)
- **[`.github/workflows/model-version-monitor.yml`](.github/workflows/model-version-monitor.yml)** — GitHub Action
  - 每周一 北京时间 09:00 自动跑(cron `0 1 * * 1`)
  - 检测变化 → `gh issue create` 自动开 issue 通知维护者
  - 自动 commit 更新的 baseline(`[skip ci]`)
  - 手动触发支持 `rebaseline` 模式
- **[`scripts/README.md`](scripts/README.md)** — 完整使用文档 + 工作原理 + 监控覆盖表

### Why
- 让社区参与不再是"口号":3 个 issue 模板 + 1 个 PR 模板把贡献门槛降到表单级
- 让仓库永远跟得上模型迭代:每周自动巡检,发现变化 5 分钟内 issue 上墙
- "全网最权威"不靠运气靠机制

### 全项目状态
- 文件:**45+** | Prompt 资产:**379** | 模型:11 | Skill:7 | 方法论:13
- **自动化等级**:从"被动等用户提 PR" → "**主动监控 + 主动催办**"

---

## [0.6.0] — 2026-05-25 · Round 4 · 矩阵 v2 + Translator Skill

### Added
- **跨模型矩阵 v2 扩展**:从 5 场景 → **10 场景**,从 55 条 → **110 条**对照 prompt
  - 新增 5 个核心场景:
    1. 恐怖悬疑:走廊深处的红气球(horror / suspense)
    2. 自然延时:山顶日出(nature / timelapse,无人物)
    3. 抽象艺术:液态金属变形循环(experimental / abstract,可循环)
    4. 武侠决斗:竹林雨夜剑客(wuxia / 中式美学)
    5. 萌宠爆款:戴墨镜冲浪金毛(viral / pet,垂直 9:16)
- **新 Skill**:[`skills/prompt-translator/SKILL.md`](skills/prompt-translator/SKILL.md) — 跨模型提示词转换器
  - **关键差异**:基于 110 条对照基准做查表式 in-context learning,**不是凭 AI 直觉重写**
  - 5 步工作流:接收输入 → 提取语义 → 查最相似场景 → 对照模式转换 → 输出含映射表与注意事项
  - 含 3 个实战示例(Sora→Kling / Wan→Hailuo / Kling 中文→Pika 英文)
  - **诚实标注局限性**:这是"公式对照转换",不是"基于实测视频效果的优化"
- **JSON Schema 扩展**:加 `effect_video_url` / `tested_at` / `tested_by` / `subjective_rating` 字段(等待社区填充)
- **CONTRIBUTING.md 加章节**:Cross-Model Matrix 实测视频贡献流程 + 评分标准 + Top Contributor 激励

### Why
回应"prompt-translator 需要数据支撑否则就是废"的挑战,**先把数据建到 110 条**,Skill 才有底气。

### 路线图
- v3(下一步):社区贡献实测视频链接,真正可视化对照
- v4(中期):基于实测评分驱动 ELO 排行,自动推荐"最佳模型 × 场景"组合

### 全项目状态
- 总文件:**42+** | Prompt 资产:**379**(269 分散 + 110 对照)
- 模型:11 | Skill:**7**(加 prompt-translator)| 方法论:13 | Web 工具:3
- 跨模型对照:**10 场景 × 11 模型 = 110 条**(从 55 → 110 翻倍)

---

## [0.5.0] — 2026-05-25 · Cross-Model Matrix（跨模型对照矩阵）

### Added
- **核心新数据集**：[`prompts/data/cross-model-matrix.json`](prompts/data/cross-model-matrix.json) — 5 个核心场景 × 11 个主流模型 = **55 条精心撰写的对照 prompt**。每条严格遵循对应模型的官方公式与最佳实践。
- **5 个核心场景**：
  1. 奢华香水旋转广告（商业 / 产品）
  2. 金色时刻情侣重逢（叙事 / 双人对话）
  3. 滑板 Kickflip 慢动作（动作 / 物理仿真）
  4. 图生视频:咖啡馆肖像（image-to-video）
  5. 办公室会议三人讨论（多角色 / 多人对话）
- **新 Web 专页**：[`tools/cross-model/index.html`](tools/cross-model/index.html) — Liquid Glass 风格的横向对比专页（场景 tab 切换 + 11 模型 grid + 一键复制 + URL hash 同步）
- **新 markdown 索引**：[`prompts/cross-model/README.md`](prompts/cross-model/README.md) — 详细方法对照表 + 路线图
- **主页新入口**：替换原"11 模型官方平台"为 **"Cross-Model Matrix ★ NEW"** 卡片

### Why
这是回应用户挑战"prompt-translator skill 没有数据支撑就是废"后的正面建设 — 与其做基于直觉的转换 skill，**先把基准数据建好**。

### Notes
- 这份对照矩阵也是未来 `prompt-translator` skill 的基准数据
- 路线图 v2 计划再加 5 个场景（恐怖悬疑 / 自然延时 / 抽象艺术 / 武侠 / 萌宠）
- v3 计划每条 prompt 附实测视频对比

---

## [0.4.1] — 2026-05-25 · 版本号校准（追平 2026/5 最新）

### Changed
- **Runway Gen-4** → **Runway Gen-4.5**（已发布，ELO 综合质量排名第一）
- **Wan 2.5** → **Wan 2.7**（Wan 2.6 开源稳定 / 2.7 最新，更长 prompt 窗口 + 更锐控制）
- **即梦 3.0** → **即梦 AI（Seedance 2.0 引擎）**（即梦是字节剪映 C 端产品，底层即 Seedance 2.0）
- **HappyHorse 1.0** 加 ⭐ "2026/5 Elo 排名第一（1357）" 徽章
- **Hailuo 02** 加 notice：MiniMax 同期有 Hailuo 2.3 性价比版本

### Important
- ⚠️ **Sora 2 即将停止**：OpenAI 2026/3 月宣布 Sora web/app 于 **2026-04-26** 停止。生产建议迁移到 Veo 3.1 / Kling 3.0 / Runway Gen-4.5 / Seedance 2.0
- 主页、Web 工具、JSON、README 中 Sora 相关条目均加 ⚠️ EOL 标记

### Fixed
- 旧版本号在所有展示位（主页/Web/README/索引/CHANGELOG）均同步到最新

### Notes
- JSON 中 model `id` 不变（保持 prompt 数据引用兼容），只更新 `name` 显示字段
- schema_version: 1.3 → 1.4

---

## [0.4.0] — 2026-05-25 · 全网最权威 · 11 模型完整收录

### Added
- **新增 6 大主流模型**（每个 12 条精选提示词，共 +72 条）：
  - **Runway Gen-4 / Aleph**（视频编辑独家：add/remove/change/re-light/re-style）
  - **Pika 2.5**（Pikaffects 15+ 创意特效 + Pikaframes 关键帧延长）
  - **Hailuo 02**（物理仿真业界第一：水/火/烟/布料/重力 准确度）
  - **Hunyuan Video 1.5**（开源最强 + 跨维度生成 + LoRA 训练）
  - **Wan 2.5**（数字人 lip-sync 业界最准 + Entity+Scene+Motion+Sound 公式）
  - **即梦 3.0**（中文最强 + 剪映原生集成 + 中式美学）
- **新方法论**：`methodology/13-六大模型公式速查.md`（6 模型公式 + 11 模型选型决策树 + 能力星级矩阵）
- **新 Skill**：`skills/model-selector/`（11 模型"购物顾问"：根据需求推荐最佳模型 + 3 个实战示例）
- **新 6 个分类**：video-edit / pikaffects / physics-sim / open-source / lip-sync / chinese-native
- **Web 工具升级**：
  - 11 模型彩虹筛选（每个模型独特颜色发光圆点）
  - Hero stats 升级到 11 / 269 / 6 / 13
  - 模型 chip 排序按发布优先级
- **RESOURCES.md 升级**：每个新模型加 3-5 个官方/权威链接（包括官方 GitHub / HuggingFace / Prompt Handbook）

### Changed
- 总提示词数：197 → **269**（+72）
- 模型数：5 → **11**
- 分类数：23 → **29**
- Skill 数：5 → **6**
- 方法论篇数：12 → **13**
- README 主标题：「Doubao Seedance + HappyHorse + Kling 三大模型」→ 「**11 大主流 AI 视频生成模型**」
- 项目定位：从「跨厂商工具集」升级为 **awesome-style 资源汇编 + 工程化工具集**

### Sources
- [Runway Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide) 官方
- [Runway Aleph Prompting Guide](https://help.runwayml.com/hc/en-us/articles/43277392678803-Aleph-Prompting-Guide) 官方
- [Pika 2.5 Promptomania 模板](https://promptomania.com/models/pika/pika-2-5)
- [Pika Labs 完整教程](https://pikalabsai.org/pika-labs-prompting-guide/)
- [MiniMax 官方 API 文档](https://platform.minimax.io/docs/guides/video-generation)
- [Hailuo 02 物理细节解析](https://getimg.ai/blog/minimax-hailuo-02-the-1080p-ai-video-model-that-gets-physics-right)
- [Tencent HunyuanVideo GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo) 官方
- [HunyuanVideo-1.5 Prompt Handbook](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md) 官方
- [Alibaba Cloud Wan 提示词指南](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt) 官方
- [即梦 AI 官网](https://jimeng.jianying.com/) 官方

---

## [0.3.0] — 2026-05-24 · awesome 化 + Sora/Veo

### Added
- **新模型**：Sora 2（OpenAI）和 Veo 3.1（Google DeepMind），各 20 条精选提示词
- **新方法论**：
  - `methodology/10-跨模型对比.md` — 五大模型对比 + 选型决策树 + 同需求 5 模型写法对照
  - `methodology/11-sora-公式.md` — Sora 两套官方写法（Shot List / 参数化）
  - `methodology/12-veo-公式.md` — Veo 8 元素 + 原生音频 4 层写法
- **Web 工具 v2**：
  - Hero section（197 / 5 / 5 / 9 统计 + 渐变标题 + 快捷键提示）
  - URL 状态同步（`#model=...&tags=...` 可分享筛选）
  - 键盘导航（`j`/`k` 上下、`Enter` 详情、`c` 复制、`Esc` 关闭）
  - 卡片详情 Drawer（完整 prompt + 相似条目推荐）
  - 新模型徽章色（Sora 绿、Veo 黄）
- **新分类**：`horror`、`documentary`、`dialogue-driven`
- **新文档**：
  - `RESOURCES.md` — 资源清单（官方文档、教程、API、社区、姊妹工具）
  - `CONTRIBUTING.md` — 贡献指南（提示词 / 模型 / 方法论 / Skill / Web 工具）
  - `CHANGELOG.md` — 本文件
- **README 改造**：标准 awesome 格式（banner + 徽章 + TOC + 五模型对比）

### Changed
- 总提示词数：121 → **197**（+76）
- 模型数：3 → **5**
- 分类数：15 → **23**
- 方法论篇数：9 → **12**

---

## [0.2.0] — 2026-05-24 · UI 重设计 + Kling

### Added
- **新模型**：Kling 3.0（快手），36 条提示词
- **新 skill**：`kling-prompter`（三套写法自适应）
- **新方法论**：`methodology/09-kling-公式.md`
- **新分类**：`viral-transform`、`music-video`、`experimental`、`gaming-ip`、`image-to-video`
- **UI 重设计**（Arc / Raycast 风格）：
  - Mesh gradient 背景 + glass blur
  - 模型彩色发光小圆点
  - Inter + JetBrains Mono 字体
  - 卡片 hover 上浮微动效
  - 复制按钮 SVG icon + 成功反馈动画
  - Prompt 不限高完整显示
  - 主题切换图标变形

### Changed
- 项目改名：`lanshu-awesome-seedance-tools` → **`lanshu-awesome-ai-video-kit`**
- 总提示词数：121 → **157**
- 移除所有装饰性 emoji，全改 lucide-icon 风格 SVG

---

## [0.1.0] — 2026-05-24 · 初始发布

### Added
- **prompts/**：121 条实测提示词（Seedance 64 + HappyHorse 57）
  - 单一数据源 JSON + 双索引 markdown
- **methodology/**：8 篇 SOP（基础公式 / 进阶公式 / 分镜时序 / 情绪外化 / 运镜词典 / 约束词 / 特殊字符 / 避坑 12 问）
- **skills/**：4 个 Claude Code Skill
  - `seedance-prompter`（自然语言 → 8 要素）
  - `seedance-storyboard`（剧情 → 多镜头）
  - `seedance-debugger`（12 类问题诊断 + 修复）
  - `happyhorse-prompter`（30-55 词紧凑 + 音频）
- **tools/prompt-browser/**：单页 HTML 提示词浏览器
  - 暗/亮主题切换
  - 模型 / 分类 / 标签 / 关键词四维筛选
  - 响应式布局
- **基础文件**：`README.md`、`LICENSE`（MIT）、`.gitignore`
