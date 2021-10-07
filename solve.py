from re import S
import xlrd
from xlrd import sheet

workbook = xlrd.open_workbook("market_data.xlsx")
sheet = workbook.sheet_by_index(0)
ncols = sheet.nrows
file = open("data.txt", "w")
for i in range(ncols):
    file.write(str(sheet.cell_value(i, 4)) + "\n")
file.close()