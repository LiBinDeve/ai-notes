---
id: "consolidated-fastapi-backend"
name: "FastAPI 与后端接口开发速记"
description: "汇总 FastAPI 入门阶段的路由、参数来源、响应方式与前后端联调要点。"
source_notes:
  - "FastAPI-入门笔记_2026-04-21_11-54-34.md"
metadata:
  created_at: "2026-04-22T10:17:57+08:00"
  updated_at: "2026-04-22T10:17:57+08:00"
---

## 条目 1：FastAPI 入门主线（路由、参数与响应）
来源：`FastAPI-入门笔记_2026-04-21_11-54-34.md`

- 最小起步：`app = FastAPI()` 后通过 `@app.get()` / `@app.post()` 等装饰器挂载路由。
- 参数来源分三类：
  - 路径参数：如 `/projects/{pid}`。
  - 查询参数：URL 中 `?` 之后部分，如 `?page=1&keyword=test`。
  - 请求体：通常用 `BaseModel` 定义 JSON 结构并自动校验。
- 响应方式：
  - 正常返回用 `return`（`dict/list/Pydantic`）。
  - 文件/页面可用 `FileResponse`、`HTMLResponse`、`JSONResponse`。
  - 错误返回用 `raise HTTPException(status_code=..., detail=...)`。
- 路由设计建议：按资源命名（如 `/projects`、`/projects/{pid}`），避免将动作写进路径（如 `/getProjects`）。
- 前后端联调关键：前端 `fetch("/api/projects")` 的 URL、Method、Body 需与后端路由和模型定义一一对应。

