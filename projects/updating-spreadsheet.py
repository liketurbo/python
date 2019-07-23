import openpyxl

wb = openpyxl.load_workbook('./data/produce-sales.xlsx')
sheet = wb.get_active_sheet()

PRICE_UPDATES = {
    'Garlic': 3.07,
    'Celery': 1.19,
    'Lemon': 1.27
}

for row in range(2, sheet.max_row):
  product = sheet['A' + str(row)].value

  if product in PRICE_UPDATES:
    sheet['B' + str(row)].value = PRICE_UPDATES[product]

wb.save('./dist/produce-sales(copy).xlsx')
