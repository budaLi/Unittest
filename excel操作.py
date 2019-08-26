import xlrd

data = xlrd.open_workbook("data.xls")


tables = data.sheets()[0]
tables2 = data.sheet_by_index(0)
# tables3= data.sheet_by_name('sheet1')


#表格的行数
print(tables.nrows)
#表格的列数
print(tables2.ncols)

# #某行的值  从0开始
# print(tables.row_values(3))
# #某列的值
# print(tables.col_values(0))
#
# #获取某行某列单元格的值  cell(rows,cols)
# print(tables.cell(2,0).value)


#写单元格
# import xlwt
# #创建workbook 其实就是excel
# workbook= xlwt.Workbook(encoding='ascii')
# #创建工作表
# work_sheet =workbook.add_sheet("xx")
# #往单元格写入内容
# work_sheet.write(0,0,label="XXXX")
# #保存  这里要注意保存为xls
# workbook.save("newbook.xls")

#向已存在的单元格中存入数据
# workbook1 = xlwt.