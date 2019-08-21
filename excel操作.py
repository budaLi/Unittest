import xlrd

data = xlrd.open_workbook("data.xlsx")
tables = data.sheets()[0]


print(tables.nrows)