import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

sheet['A1'].font = Font(name='Times New Roman', bold=True)
sheet['A1'] = 'Bold Times New Roman'

sheet['B2'].font = Font(size=24, italic=True)
sheet['B2'] = '24 pt Italic'

wb.save('./dist/styled.xlsx')
