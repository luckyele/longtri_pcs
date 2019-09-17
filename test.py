import xlrd



def get_rowx():
	pass

def get_colx():
	pass

def get_area():
	pass


file_name = "2017_anhui_whg.xlsx"

data = xlrd.open_workbook(file_name)

# print sheet numbers
print(data.sheet_names())

table = data.sheets()[0] #return xlrd.sheet.Sheet() object

nrows, ncols = table.nrows, table.ncols  #获取该sheet中的有效行数

print(nrows,ncols)

print(table.cell_value(8,0))


# COL
#table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
#table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
#table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表
#table.col_values(colx, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表

# CELL
#table.cell(rowx,colx)   #返回单元格对象
#table.cell_type(rowx,colx)    #返回单元格中的数据类型
#table.cell_value(rowx,colx)   #返回单元格中的数据
#table.cell_xf_index(rowx, colx)   # 暂时还没有搞懂
