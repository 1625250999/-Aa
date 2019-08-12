# encoding: utf-8
import xlrd

# 操作excel
excel = xlrd.open_workbook("D://test//a.xlsx")
excel.sheet_names() # 获取excel里的工作表sheet名称数组
sheet = excel.sheet_by_index(0) #根据下标获取对应的sheet表


print(sheet.row_values(0), "第一行的数据为：")#获取第一行的数据
print (sheet.col_values(0), "第一列的数据为：") #获取第一列的数据
print((sheet.nrows), "总共的行数")
print("总共的列数：", (sheet.ncols)) #


for i in range(1, sheet.nrows):
    row_list = sheet.row_values(i) # 每一行的数据在row_list 数组里
    print(row_list)


#特殊情况展示 合并单元格
#对于单个的单元格可以通过sheet.cell(row,col) 参数就是row-行、col-列，这个方法得到的是cell对象，sheet.cell(0,0).value value是对应的单元格内容。

print("合并的单元格", (sheet.merged_cells))
#sheet.merged_cells 可以查看合并单元格的情况