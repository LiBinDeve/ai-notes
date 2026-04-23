---
id: "consolidated-python-doc-office"
name: "Python 文档与演示生成自动化速记"
description: "汇总 python-docx 与 python-pptx 在文档/演示生成中的高频 API、样式控制与导出实践。"
source_notes:
  - "python-pptx-常用构建细节速记_2026-04-01_11-50-08.md"
  - "python-docx-常用实现细节速记_2026-04-01_11-59-20.md"
metadata:
  created_at: "2026-04-03T09:39:27+08:00"
  updated_at: "2026-04-03T09:39:27+08:00"
---

## 条目 1：python-pptx 构建页面与组件速记
来源：`python-pptx-常用构建细节速记_2026-04-01_11-50-08.md`

- 文档与页面：`Presentation()` 创建文档，`prs.slides.add_slide(prs.slide_layouts[6])` 创建空白页。
- 位置与尺寸：统一使用 `Inches(...)`，常见 16:9 画布为 `13.333 x 7.5`。
- 文本框流程：`add_textbox` -> `text_frame` -> `paragraph` -> `run`，通过 `run.font` 设置字体名、字号、粗细与颜色。
- 形状与连线：`add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, ...)` 与 `add_connector(MSO_CONNECTOR.STRAIGHT, ...)`。
- 图片与保存：`add_picture(...)` 插图，`prs.save(output_path)` 输出文件。

## 条目 2：python-docx 排版、插图与转 PDF 速记
来源：`python-docx-常用实现细节速记_2026-04-01_11-59-20.md`

- 文档与样式：`Document()` 创建文档，`doc.styles.add_style(...)` 创建段落样式并复用到正文/标题。
- 中文字体关键：除 `font.name` 外，还需设置 `w:eastAsia` 以确保中文字体正确生效。
- 段落排版：`paragraph_format` 控制对齐、缩进、行距；`run` 级别处理局部字体/下划线等样式。
- 图像写入：可用 `io.BytesIO()` 缓冲 `matplotlib` 输出，再 `doc.add_picture(buf, ...)` 直接插图。
- 导出链路：`doc.save(docx_path)` 后用 `docx2pdf.convert(...)` 转 PDF，Windows 场景可加 `pythoncom.CoInitialize()`/`CoUninitialize()` 降低 COM 调用问题。
