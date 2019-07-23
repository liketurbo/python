import openpyxl
import os

wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()

col = 0

for folder, folders, filenames in os.walk(os.getcwd()):

  for filename in filenames:
    if filename.endswith('.txt'):
      file = open(os.path.join(folder, filename))
      lines = file.readlines()
      file.close()

      col += 1

      for row in range(1, len(lines) + 1):
        sheet.cell(row, col).value = lines[row - 1]

wb.save('./dist/all-texts.xlsx')
