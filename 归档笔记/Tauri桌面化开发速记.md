---
id: "consolidated-tauri-desktop-dev"
name: "Tauri 桌面化开发速记"
description: "汇总从 Claude Design 原型到 Tauri 桌面应用搭建、无边框窗口与打包发布流程。"
source_notes:
  - "Claude-Design-到-Tauri-桌面化_2026-04-22_09-53-55.md"
metadata:
  created_at: "2026-04-22T10:17:57+08:00"
  updated_at: "2026-04-22T10:17:57+08:00"
---

## 条目 1：Claude Design 原型迁移到 Tauri 的完整链路
来源：`Claude-Design-到-Tauri-桌面化_2026-04-22_09-53-55.md`

- 环境前置：
  - 安装 Microsoft C++ Build Tools。
  - 执行 `winget install --id Rustlang.Rustup`，并验证 `rustc`、`cargo`、`node`、`npm`。
- 项目初始化：
  - 执行 `npm create tauri-app@latest`。
  - 选择 `React + JavaScript + npm`。
  - 进入目录后执行 `npm install` 与 `npm run tauri dev`。
- 原型落地映射：
  - 前端入口与组件：`index.html`、`src/main.jsx`、`src/App.jsx`、`src/App.css`。
  - Tauri/Rust 侧：`src-tauri/src/lib.rs`、`src-tauri/Cargo.toml`、`src-tauri/tauri.conf.json`、`src-tauri/capabilities/default.json`。
- 无边框窗口实现：
  - `tauri.conf.json` 设置 `"decorations": false`。
  - `capabilities/default.json` 增加窗口控制与拖拽相关权限。
  - `App.jsx` 使用 `data-tauri-drag-region` 和自定义 WinControls（配合 `@tauri-apps/api/window`）。
  - `App.css` 给按钮设置 `-webkit-app-region: no-drag` 避免按钮触发拖拽。
- 打包发布：
  - 正式版：`npm run tauri build`。
  - 调试版：`npm run tauri build -- --debug`。
  - 产物目录：`src-tauri/target/release/bundle/`，常用分发文件为 `nsis/*-setup.exe`。

