---
id: "raw-20260420083719-ebeddb08"
name: "Hermes Agent（Windows 11 + WSL + Ubuntu + DashScope / Qwen）安装教程"
description: "记录在 Windows 11 上通过 WSL + Ubuntu 安装 Hermes Agent，并配置 DashScope/Qwen 的步骤与命令清单。"
metadata:
  stored_at: "2026-04-20T08:37:19.094516+08:00"
---

## 一、安装 WSL

### 1\. 以管理员身份打开 PowerShell

开始菜单搜索：

```text
PowerShell
```

右键：

```text
以管理员身份运行
```

\---

### 2\. 执行安装命令

```powershell
wsl --install
```

这条命令会自动安装 WSL 和 Ubuntu。  
命令执行后直接进入了 Ubuntu 初始化，没有额外要求重启。

\---

## 二、初始化 Ubuntu

出现提示：

```text
Create a default Unix user account:
```

输入你的 Linux 用户名，例如：

```text
libin
```

然后按回车。

接着输入密码两次。  
注意：Linux 输入密码时不会显示字符或星号，这是正常现象。

\---

## 三、进入 Linux 主目录

安装完成后执行：

```bash
cd ~
```

这会进入你的 Linux Home 目录，例如：

```text
/home/libin
```

\---

## 四、创建项目目录

执行：

```bash
mkdir -p ~/projects/hermes
cd ~/projects/hermes
```

以后建议所有 Linux 项目都放在：

```text
/home/用户名/projects/
```

这样结构最清晰。

\---

## 五、把 Ubuntu 软件源改成阿里云镜像

国内环境下，先改镜像源更稳。

### 1\. 打开源配置文件

```bash
sudo nano /etc/apt/sources.list.d/ubuntu.sources
```

### 2\. 把两处 `URIs` 改成：

```yaml
URIs: https://mirrors.aliyun.com/ubuntu
```

### 3\. 保存退出

保存：

```text
Ctrl + O
```

确认：

```text
Enter
```

退出：

```text
Ctrl + X
```

### 4\. 更新软件源

```bash
sudo apt update
```

\---

## 六、安装 pipx

执行：

```bash
sudo apt install pipx -y
```

`pipx` 适合安装命令行 Python 工具，避免系统 Python 受到影响。

\---

## 七、安装 uv

执行：

```bash
pipx install uv
```

然后执行：

```bash
pipx ensurepath
source ~/.bashrc
```

验证：

```bash
uv --version
```

如果能显示版本号，说明 `uv` 已经可用。

\---

## 八、安装 Hermes

在项目目录里执行：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

\---

## 九、验证 Hermes 是否安装成功

执行：

```bash
hermes version
hermes doctor
```

如果都能正常输出，说明 Hermes 已经安装好。

\---

## 十、通过配置文件配置 DashScope / Qwen

不建议在交互界面里粘贴 key。  
直接改文件最稳。

\---

### 1\. 配置 API Key 和 Base URL：`\~/.hermes/.env`

打开：

```bash
nano ~/.hermes/.env
```

写入：

```env
DASHSCOPE\_API\_KEY=你的DashScope\_API\_Key
DASHSCOPE\_BASE\_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
HERMES\_MAX\_ITERATIONS=90
```

如果你只打算使用 DashScope，就不要保留其他无关 provider 的 key。

保存退出：

```text
Ctrl + O
Enter
Ctrl + X
```

\---

### 2\. 配置 provider 和 model：`\~/.hermes/config.yaml`

打开：

```bash
nano ~/.hermes/config.yaml
```

在 `model:` 段里设置为：

```yaml
model:
  provider: alibaba
  default: qwen3.6-plus
```

说明：

* `provider: alibaba`：表示使用 DashScope / Alibaba provider
* `default: qwen3.6-plus`：表示默认模型
* API key 不放这里，放 `.env`

如果你想换成别的 Qwen 模型，例如：

```yaml
model:
  provider: alibaba
  default: qwen3-coder-plus
```

也可以。

\---

### 3\. 配置原则

最终记住这一条就行：

* **模型、provider**：放 `config.yaml`
* **API key、base URL**：放 `.env`

\---

## 十一、启动 Hermes

执行：

```bash
hermes
```

或者直接单次测试：

```bash
hermes chat -q "你好"
```

如果返回正常内容，说明：

* Hermes 正常
* DashScope 正常
* Qwen 正常

\---

## 十二、最推荐的最终文件内容

### `\~/.hermes/.env`

```env
DASHSCOPE\_API\_KEY=你的DashScope\_API\_Key
DASHSCOPE\_BASE\_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
HERMES\_MAX\_ITERATIONS=90
```

### `\~/.hermes/config.yaml`

```yaml
model:
  provider: alibaba
  default: qwen3.6-plus
  base_url: https://dashscope.aliyuncs.com/compatible-mode/v1
```

\---

## 十三、完整命令清单

### Windows 里执行

```powershell
wsl --install
```

### Ubuntu 里执行

```bash
cd ~

mkdir -p ~/projects/hermes
cd ~/projects/hermes

sudo nano /etc/apt/sources.list.d/ubuntu.sources
sudo apt update

sudo apt install pipx -y
pipx install uv
pipx ensurepath
source ~/.bashrc
uv --version

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

hermes version
hermes doctor

nano ~/.hermes/.env
nano ~/.hermes/config.yaml

hermes
```

\---

## 十四、一句话总结

最终推荐的稳定做法是：

* **WSL + Ubuntu**
* **阿里云镜像源**
* **pipx 安装 uv （Hermes 安装脚本第一次失败，就是卡在自动安装 uv 这一步，所以现状uv。因为 Ubuntu 24：开了 PEP 668，pip安装失败，所以用pipx。）**
* **Hermes 官方安装脚本**
* **`.env` 配 DashScope key 和 base URL**
* **`config.yaml` 配 provider 和 model**

这样最稳，也最适合后面长期维护。


