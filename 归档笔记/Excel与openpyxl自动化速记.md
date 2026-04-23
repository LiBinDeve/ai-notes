---
id: "consolidated-excel-automation"
name: "Excel 与 openpyxl 自动化速记"
description: "汇总 openpyxl 建表代码片段与 Excel 数据看板公式实践。"
source_notes:
  - "openpyxl-库学习笔记（表格建立）_2026-03-12_17-25-17.md"
  - "Excel-数据看板常用公式总结_2026-03-18_10-07-40.md"
metadata:
  created_at: "2026-03-19T09:39:17+08:00"
  updated_at: "2026-03-30T10:01:09+08:00"
---

## 条目 1：openpyxl 建表关键 API（历史版）
来源：`openpyxl-库学习笔记（表格建立）_2026-03-12_17-25-17.md`

- 状态：`replaced`
- 替代说明：该条为早期摘要，已由同源笔记在后续补充的“条目 4/5”覆盖，包含更完整的样式、图片锚定与返回值说明。

## 条目 2：看板常用公式族
来源：`Excel-数据看板常用公式总结_2026-03-18_10-07-40.md`

- 查找：`INDEX+MATCH`、`VLOOKUP`。
- 统计：`COUNTA`、`COUNTIF`、`COUNTIFS`。
- 筛选与拼接：`FILTER`、`TEXTJOIN`、`&`。
- 稳定性处理：复杂公式外层加 `IFERROR`，并确保日期列是“真实日期格式”。

## 条目 3：看板公式易错点
来源：`Excel-数据看板常用公式总结_2026-03-18_10-07-40.md`

- 无未来日期会导致最近培训公式报错。
- 日期重复时 `MATCH(...,0)` 默认仅返回第一条。
- 可用 `FILTER+TEXTJOIN` 汇总同日多条课程。

## 条目 4：openpyxl 工作簿、样式与打印设置（更新版）
来源：`openpyxl-库学习笔记（表格建立）_2026-03-12_17-25-17.md`

- 工作簿基础：`Workbook()`、`remove(wb.active)`、`create_sheet(...)`、`wb.save(...)`。
- 样式与版式：`Font`、`Alignment`、`Border/Side`、行高列宽、合并单元格与标题样式。
- 打印参数：`ws.page_setup.orientation='portrait'` 与 `ws.page_setup.paperSize=ws.PAPERSIZE_A4`。

## 条目 5：openpyxl 图片锚定与返回值速记（更新版）
来源：`openpyxl-库学习笔记（表格建立）_2026-03-12_17-25-17.md`

- 图片对象：`from openpyxl.drawing.image import Image as XLImage`，可设置 `img.width/img.height`。
- 锚定行为：`ws.add_image(img, 'B2')` 为左上角锚定，图片是浮动对象，不等同单元格内容。
- 返回值：`ws.cell()` / `ws['A1']` 返回 `Cell`，`ws.merge_cells()` 返回 `None`。
