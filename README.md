# Content Automation Pipeline CN

> 一套面向中文创作者的内容自动化流水线：选题 → 成稿 → 改写 → 排期 → 复盘。

适合：独立开发者、个体创业者、内容团队。

---

## MVP 功能

- ✅ 选题池模板（持续产出）
- ✅ 一稿多改（多平台风格）
- ✅ 发布排期清单
- ✅ 周复盘模板（看数据迭代）

---

## 快速开始

1. 按 `docs/SETUP-CHECKLIST.md` 配置
2. 用 `examples/content-calendar.example.md` 建你的一周内容表
3. 每天按 `docs/OPS-RUNBOOK.md` 执行

---

## 代码能力（已内置）

### 启动 API（本地）

```powershell
python -m pip install -r requirements.txt
python -m uvicorn src.api:app --reload --port 8013
```

### 开发者快速开始

```powershell
# 1) 跑测试
powershell -ExecutionPolicy Bypass -File .\scripts\tasks.ps1 -Task test

# 2) 跑 CLI 演示
powershell -ExecutionPolicy Bypass -File .\scripts\tasks.ps1 -Task run-cli

# 3) 跑 API
powershell -ExecutionPolicy Bypass -File .\scripts\tasks.ps1 -Task run-api
```

- 健康检查：`GET http://127.0.0.1:8013/health`
- Swagger：`http://127.0.0.1:8013/docs`


- `src/content_pipeline.py`
  - `generate`：按主题生成主文案
  - `repurpose`：一稿改写为不同平台版本
  - `plan-week`：生成周排期文件
- `scripts/run-demo.ps1`：一键演示命令

示例：

```powershell
python .\src\content_pipeline.py generate --topic "老板助手自动化"
python .\src\content_pipeline.py repurpose --input .\examples\post.example.txt --platform x
```

---

## 项目结构

```txt
content-automation-pipeline-cn/
├─ README.md
├─ docs/
│  ├─ SETUP-CHECKLIST.md
│  ├─ OPS-RUNBOOK.md
│  └─ SALES-PAGE-COPY.md
├─ examples/
│  ├─ content-calendar.example.md
│  └─ repurpose-workflow.example.md
└─ scripts/
   └─ quickstart-notes.md
```

---

## 定价建议

- 模板版：¥149
- Pro 版：¥399
- 代部署：¥2999

---

## 快速部署（Docker）

```bash
docker build -t content-pipeline-cn .
docker run --rm -p 8013:8013 content-pipeline-cn
```

更多 API 调用示例见：`docs/API-EXAMPLES.md`

成交资料：
- `docs/QUOTE-TEMPLATE.md`
- `docs/CONTRACT-LITE.md`
- `docs/DELIVERY-REPORT.md`

自动成交推进：
- `docs/LEAD-TRACKER.md`
- `docs/FOLLOW-UP-MESSAGES.md`
- `docs/NO-REPLY-NUDGE.md`

转化增强：
- `docs/FAQ.md`
- `docs/COOP-FLOW.md`
- `docs/CASE-STUDY-TEMPLATE.md`
- `docs/TESTIMONIAL-TEMPLATE.md`
- `docs/PRICING-PAGE-COPY.md`
- `docs/EN-OVERVIEW.md`

---

## 关联仓库（推荐一起看）

- OpenClaw Biz Assistant Starter  
  https://github.com/caishenyechina/openclaw-biz-assistant-starter
- China Market Watchdog  
  https://github.com/caishenyechina/china-market-watchdog

---

## 联系方式

- Email：4553377@qq.com
- QQ：4553377

---

## License

MIT
