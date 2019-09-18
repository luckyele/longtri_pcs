import xlrd
import csv


class XLS:
    
    def __init__(self):
        file_name = "2017_anhui_whg.xlsx"
        self.data = xlrd.open_workbook(file_name)

    def rowx(self):
        pass


    def colx(self):
        pass

    def cells(self):
        pass

    def sheet_names(self):
        return self.data.sheet_names()

    def tables(self,i):
        table = self.data.sheets()[i] #return xlrd.sheet.Sheet() object
        return table

    def rowcol_num(self,table):
        if table == None:
            print("table can't be None")
            return

        return (table.nrows,table.ncols)


if __name__ == '__main__':

    x = XLS()
    print(x.sheet_names())
    t = x.tables(0)

    print(x.rowcol_num(t))
    print(t.cell_value(8,0))       #返回单元格中的数据
    print(t.row_values(8,0,5))
  
    
# ROW
# nrows = table.nrows  #获取该sheet中的有效行数
# table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
# table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
# table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
# table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
# table.row_len(rowx) #返回该列的有效单元格长度

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
