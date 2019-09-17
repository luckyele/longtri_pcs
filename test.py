import xlrd


class XLS:
    
    def __init__(self):
        file_name = "2017_anhui_whg.xlsx"
        self.data = xlrd.open_workbook(file_name)

    def get_rowx(self):
        pass

    def get_colx(self):
        pass

    def get_area(self):
        pass

    def sheet_names(self):
# print sheet numbers
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
