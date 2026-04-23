from openpyxl import Workbook
from openpyxl.styles import Side, Border, Font, Alignment

def create_sheet(wb, name):
    ws = wb.create_sheet(name)
    thin = Side(style='thin')
    border_a = Border(left=thin, right=thin, top=thin, bottom=thin)
    font_a = Font(name='黑体', size=18, bold=True, color='FF0000')
    align_vertical = Alignment(horizontal='center', vertical='center', text_rotation=255, wrap_text=True)
    ws.merge_cells('B1:G1')        # ws.merge_cells返回的对象是空，只是执行合并内容，真正要对合并单元格操作，需要写到左上角单元格
    c = ws['B1'] 
    c.value = "问话"
    c.font = font_a
    c.alignment = align_vertical
    c.border = border_a
    ws.column_dimensions['A'].width = 2
    ws.row_dimensions[1].height = 84

wb = Workbook()

create_sheet(wb, "test")

wb.save("demo.xlsx")