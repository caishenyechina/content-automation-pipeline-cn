# API Examples

Base URL: `http://127.0.0.1:8013`

## Health
```bash
curl http://127.0.0.1:8013/health
```

## Generate
```bash
curl -X POST http://127.0.0.1:8013/generate \
  -H "Content-Type: application/json" \
  -d '{"topic":"老板助手自动化"}'
```

## Repurpose
```bash
curl -X POST http://127.0.0.1:8013/repurpose \
  -H "Content-Type: application/json" \
  -d '{"text":"今天聊聊自动化...","platform":"x"}'
```

## Plan Week
```bash
curl -X POST http://127.0.0.1:8013/plan-week \
  -H "Content-Type: application/json" \
  -d '{"topics":["自动化","复盘","增长"]}'
```
