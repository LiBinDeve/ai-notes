---
id: "raw-20260422095355-5499135e"
name: "今日学习记录：Claude Design 到 Tauri 桌面化"
description: "记录从 Claude Design 原型到 Tauri 桌面应用搭建、无边框窗口处理与安装包构建的完整学习流程。"
metadata:
  stored_at: "2026-04-22T09:53:55.487645+08:00"
---
# Claude Design → 原型 → Tauri 桌面化（完整流程）

以下安装tauri教程来源于https://github.com/tauri-apps/tauri开源项目。该项目Getting Started的prerequisites提示要安装c++和rust，然后执行安装命令npm create tauri-app@latest。

## 核心步骤

1. Claude Design 生成 项目控制中心 原型（里面有两个功能，一个是交互式的调节UI主体和组件参数；另一个是评论功能打开，选择组件，局部上下文的对这个组件进行修改。）
2. 测试 BAT 脚本与页面功能
3. 安装 Microsoft C++ Build Tools（选择第一个安装，选中之后点击安装，安装完关闭界面就可以了。安装tauri的前置条件。）
4. winget install --id Rustlang.Rustup（powershell直接执行命令安装。安装tauri的前置条件。）
5. 验证 rustc / cargo / node / npm
6. 创建目录并执行 npm create tauri-app@latest（安装构建tauri项目所需的依赖到项目文件夹）
7. 选择 React + JavaScript + npm
8. 关闭 Windows 智能应用控制（避免拦截 Rust DLL）
9. cd project-control-center
10. npm install
11. npm run tauri dev（启动开发模式）
12. 成功运行 Welcome to Tauri + React
13.项目内打开 Claude Code，输入项目原型文件夹路径，让 Claude Code 一比一还原项目。（主要生成这几个文件：index.html是宿主容器，浏览器只能打开html文件，不能打开react文件，所以必须有这个文件作为入口；src/main.jsx把 React 挂载到 html；src/App.jsx所有 React 组件；src/App.css所有 CSS；src-tauri/src/lib.rs是Rust 后端，对应原型的 main.py，tauri项目后端只能用rust;src-tauri/Cargo.toml是Rust 依赖;src-tauri/tauri.conf.json是Tauri 配置，窗口大小、标题等；src-tauri/capabilities/default.json：权限配置
14.无边框窗口（去掉系统标题栏）的改法：tauri.conf.json 窗口加 "decorations": false；capabilities/default.json 加权限：allow-minimize、allow-toggle-maximize、allow-close、allow-is-maximized、allow-start-dragging；App.jsx 的 header 标签加属性 data-tauri-drag-region（实现拖拽移动窗口）；App.jsx 加 WinControls 组件（自定义最小化/最大化/关闭按钮），从 @tauri-apps/api/window 引入 getCurrentWindow； App.css 给 .win-btn 加 -webkit-app-region: no-drag（防止按钮触发拖拽）
15. npm run tauri build 打包正式版安装包。输出位置：src-tauri/target/release/bundle/。nsis/BatPad_0.1.0_x64-setup.exe（推荐，普通用户用这个）。msi/BatPad_0.1.0_x64_en-US.msi（企业环境）。只需把 setup.exe 发给对方，对方无需安装任何环境（需要 Windows 10 1803 以上）。
    debug 版命令：npm run tauri build -- --debug（编译更快，用于开发测试）
