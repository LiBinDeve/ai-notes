---
id: "consolidated-python-asyncio"
name: "Python 异步编程与并发控制速记"
description: "汇总 asyncio 中 await 传递、事件循环入口与 Semaphore 并发控制要点。"
source_notes:
  - "asyncio使用教程_2026-03-25_16-52-31.md"
metadata:
  created_at: "2026-03-30T10:01:09+08:00"
  updated_at: "2026-03-30T10:01:09+08:00"
---

## 条目 1：await 传递与协程边界
来源：`asyncio使用教程_2026-03-25_16-52-31.md`

- 调用协程函数必须使用 `await`。
- 只要函数体内出现 `await`，该函数需要定义为 `async def`。
- `await` 语义会沿调用链向上传递，直到顶层入口。

## 条目 2：同步阻塞函数接入异步流程
来源：`asyncio使用教程_2026-03-25_16-52-31.md`

- 若底层函数是同步阻塞函数，使用 `await asyncio.to_thread(func, ...)` 包装。
- 若底层本身已是异步函数，直接 `await` 即可。
- 顶层执行入口使用 `asyncio.run(main())` 启动事件循环。

## 条目 3：Semaphore 与 gather 的分工
来源：`asyncio使用教程_2026-03-25_16-52-31.md`

- `asyncio.gather(*tasks)` 负责并发调度与结果收集，不直接限流。
- `asyncio.Semaphore(n)` 控制同一时刻最多运行的任务数。
- 常见模式：在任务函数中使用 `async with sem:`，再执行真实 I/O 或 `to_thread` 调用。
