---
id: "consolidated-runtime-network"
name: "Windows 启动与代理环境配置"
description: "汇总 Windows 启动脚本与项目代理隔绝配置的可执行做法。"
source_notes:
  - "Windows批处理启动脚本示例：launch.bat_2026-03-12_09-41-10.md"
  - "项目隔绝代理设置_2026-03-16_14-34-16.md"
  - "Hermes-Agent（Windows-11-+-WSL-+-Ubuntu-+-DashScope-Qwen）安装教程_2026-04-20_08-37-19.md"
  - "激活虚拟环境（venv）_2026-04-20_12-00-26.md"
metadata:
  created_at: "2026-03-19T09:39:17+08:00"
  updated_at: "2026-04-21T09:30:00+08:00"
---

## 条目 1：Windows 启动脚本模板
来源：`Windows批处理启动脚本示例：launch.bat_2026-03-12_09-41-10.md`

```batch
@echo off
cd /d %~dp0
call venv\Scripts\activate.bat
nanobot agent
pause
```

- 核心流程：切目录 -> 激活虚拟环境 -> 启动 agent -> 保持窗口。

## 条目 2：项目代理隔绝生效时机
来源：`项目隔绝代理设置_2026-03-16_14-34-16.md`

- `NO_PROXY` 需要在首次实例化客户端（如 `OpenAI(...)`、`httpx.Client(...)`）前设置。
- 最稳妥位置是主程序入口顶部、且在其它模块导入前。

```python
import os
os.environ["NO_PROXY"] = "api.deepseek.com,dashscope.aliyuncs.com"
os.environ["no_proxy"] = os.environ["NO_PROXY"]
```

## 条目 3：WSL + Ubuntu 安装 Hermes 与 DashScope/Qwen 配置
来源：`Hermes-Agent（Windows-11-+-WSL-+-Ubuntu-+-DashScope-Qwen）安装教程_2026-04-20_08-37-19.md`

- Windows 侧先执行 `wsl --install`，进入 Ubuntu 初始化后创建 Linux 账号。
- Linux 侧建议固定工作目录为 `~/projects/hermes`，并先将 Ubuntu 源切换到阿里云镜像后再 `sudo apt update`。
- 依赖安装顺序：`sudo apt install pipx -y` -> `pipx install uv` -> `pipx ensurepath` -> `source ~/.bashrc`。
- Hermes 安装与验证：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes version
hermes doctor
```

- 配置拆分原则：
  - `~/.hermes/.env` 存 `DASHSCOPE_API_KEY` 与 `DASHSCOPE_BASE_URL`
  - `~/.hermes/config.yaml` 存 `model.provider` 与 `model.default`

- 命令更正（版本修订）：
  - `cd \~` -> `cd ~`（`replaced`: 反斜杠写法会导致路径解析异常）
  - `source \~/.bashrc` -> `source ~/.bashrc`（`replaced`: 需使用标准 home 展开）

## 条目 4：PowerShell 下 venv 初始化与日常启动
来源：`激活虚拟环境（venv）_2026-04-20_12-00-26.md`

- 首次初始化建议命令：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- 项目依赖安装与运行：

```powershell
python -m pip install sqlalchemy streamlit
python -m pip install -e wechat-cli
streamlit run app.py
python analyzer.py
```

- 常用验证命令：

```powershell
wechat-cli history "联系人备注名" --format text
python -m pip list
```

- 命令更新说明：
  - `venv\Scripts\activate` 标记为 `deprecated`（该写法更偏向 `cmd.exe`，在 PowerShell 下推荐 `Activate.ps1`）。
  - `pip install ...` 标记为 `replaced`，建议统一为 `python -m pip install ...` 以避免多解释器环境下的 pip 指向偏差。
