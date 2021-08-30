import openpyxl
# wb = openpyxl.load_workbook("order_import_template.xlsx")
# # sheet_names = excel_work_book.get_sheet_names()
# import_template = wb["Sheet1"]
# cell = import_template["A1"].value
# print(cell)
wb = openpyxl.load_workbook("order_import_template.xlsx")
# 获取sheet对象
sheet = wb["Sheet1"]
for i in range(2, 32):
    num_str = "B"+str(i)
    print(sheet[num_str].value)
    sheet[num_str] = "1111111"
    print(sheet[num_str].value)
wb.save("order_import_template.xlsx")
