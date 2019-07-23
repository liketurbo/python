import sys
import openpyxl
from os import path

N = int(sys.argv[1])
M = int(sys.argv[2])
NAME = sys.argv[3]

wb = openpyxl.load_workbook(NAME)
sheet = wb.get_active_sheet()

sheet.insert_rows(N, M)

wb.save(path.join('.', 'dist', path.basename(NAME)))
