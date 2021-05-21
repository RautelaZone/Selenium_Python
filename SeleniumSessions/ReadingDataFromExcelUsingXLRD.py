"""
needed to install : xlrd==1.2.0 as The latest version of xlrd (2.0.1) only supports .xls files
"""

import xlrd

file_path = "C:/Automation/Files/DataDriven.xlsx"
sheet_name = "EMPDETAILS"
workbook = xlrd.open_workbook(file_path)
sheet = workbook.sheet_by_name(sheet_name)

# get the total numbers of row
rowCount = sheet.nrows
print("Total no of rows:",rowCount)

# get the total numbers of column
colCount = sheet.ncols
print("Total no of columns:",colCount)


'''
Printing all values
'''
for current_row in range(1,rowCount):
    for current_col in range(0,colCount):
        print(sheet.cell_value(current_row,current_col),end="  ")
    print()

'''
Printing row by row
'''
# for current_row in range(1,rowCount):
#     emp_id = sheet.cell_value(current_row,0)  # added ' before numeric value in the sheet else it will print 111.0
#     first_name = sheet.cell_value(current_row, 1)
#     print(emp_id," ", first_name)

