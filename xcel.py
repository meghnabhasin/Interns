import xlsxwriter

workbook = xlsxwriter.Workbook('output1.xlsx')
worksheet = workbook.add_worksheet()
row=0
col=0
worksheet.write(row, col, 'First Name')
worksheet.write(row, col + 1, 'Last Name')
worksheet.write(row, col + 2, 'Birthday')
worksheet.write(row, col + 3, 'City')
row=1
for i in range(10):
    col=0
    fname=input("Enter First name")
    lname=input("Enter last name")
    bday=input("Enter Birthday")
    city=input("Enter City")
    worksheet.write_string(row, col, fname)
    worksheet.write_string(row, col + 1, lname)
    worksheet.write_string(row, col + 2, bday)
    worksheet.write_string(row, col + 3, city)
    row=row+1
workbook.close()