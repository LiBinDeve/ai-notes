---
id: "consolidated-git-version-control"
name: "Git 版本控制与远程协作速记"
description: "汇总 Git 本地工作流、分支合并、撤销策略与远程协作命令。"
source_notes:
  - "Git-学习总结：本地与远程命令（两日）_2026-03-20_10-41-46.md"
metadata:
  created_at: "2026-03-25T00:00:00+08:00"
  updated_at: "2026-03-25T00:00:00+08:00"
---

## 条目 1：本地仓库初始化与首提交流程
来源：`Git-学习总结：本地与远程命令（两日）_2026-03-20_10-41-46.md`

- 环境与身份配置：`git --version`、`git config --global user.name`、`git config --global user.email`、`git config --list`。
- 仓库创建与初始化：`mkdir`、`cd`、`git init`。
- 首次提交链路：`git add` -> `git commit` -> `git log`。

## 条目 2：分支开发、合并与冲突处理
来源：`Git-学习总结：本地与远程命令（两日）_2026-03-20_10-41-46.md`

- 分支切换与开发：`git switch -c feature/greet`、`git switch master`。
- 合并流程：`git merge feature/greet` 后手动处理冲突标记，再 `git add` 与 `git commit`。
- 冲突处理原则：保留目标内容、删除冲突标记、重新提交合并结果。

## 条目 3：历史审计、标签与撤销策略
来源：`Git-学习总结：本地与远程命令（两日）_2026-03-20_10-41-46.md`

- 历史查看：`git log --oneline --decorate --graph --all`、`git show HEAD`。
- 版本标签：`git tag -a v0.1.0 -m "..."`、`git show v0.1.0`。
- 错误提交回滚：`git revert HEAD` 通过新增反向提交撤销变更。

## 条目 4：远程仓库连接与推拉顺序
来源：`Git-学习总结：本地与远程命令（两日）_2026-03-20_10-41-46.md`

- 首次绑定远程：`git remote add origin <url>`，用 `git remote -v` 验证。
- 分支对齐：`git branch -M main`。
- 同步顺序：远程有内容时先 `git pull origin main --allow-unrelated-histories`，再 `git push -u origin main`。
- 跟踪关系建立后可直接使用 `git push` / `git pull`。
