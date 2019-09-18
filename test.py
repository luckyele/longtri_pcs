import xlrd
import csv
from matplotlib import pyplot as plt
import numpy

class XLS:
    def __init__(self):
        file_name = "2017_anhui_whg.xlsx"
        self.data = xlrd.open_workbook(file_name)
        self.table_num = 0
        self.table = None

    def rowx(self, rowx=9):
        '''output a row, default row(9)
        '''
        return self.table.row_values(rowx)

    def colx(self, colx=0):
        return self.table.col_values(colx)

    def sheet_names(self):
        self.table_num = len(self.data.sheet_names())
        return self.data.sheet_names()

    def tables(self, i=0):
        self.table = self.data.sheets()[i]
        return self.table

    def rowcol_num(self):
        return (self.table.nrows, self.table.ncols)

def del_a(array, i, j):
    for k in range(i,j):
        del array[i+k]

    return array

def test():
    x = XLS()

    x.tables(0)
    rx, cx  = x.rowcol_num()
   # print(x.table.cell(9,1).value)

    data = []

    for i in range(9, rx):
        if x.table.cell(i, 1).value == '----':
            continue
        data.append(x.rowx(i))

    print(data)
    print(len(data))

    for i in range(len(data)):
        data[i][0] = data[i][0].strip()
        for k in range(0,12):
            del data[i][0]
    for i in range(len(data)):
        print(data[i])

    v1 = []
    for i in range(len(data)):
        if data[i][0] == '':
            data[i][0] = 0
        v1.append(int(data[i][0]))
    print(v1)
    v1.sort()
    plt.hist(v1, bins=numpy.arange(1,40))
    plt.show()

if __name__ == '__main__':
    test()
