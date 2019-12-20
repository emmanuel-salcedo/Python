import os
from xlwt.compat import xrange
from xlwt import Workbook, Formula, easyxf

print(os.getcwd())
os.mkdir('Script9LabAssignment')

file = open("Script9LabAssignment/lab9.txt", "w")
file.write(
    "This is my assignment for Lab 9.\n"
    "I know that it is easy to create text files in Python\n"
    "I just need to relax and follow the yellow brick road")
file.close()

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')
Style1 = easyxf('pattern: pattern solid, fore_colour yellow;')
wb.save('Script9LabAssignment/Lab9.xls')

sheet1.write(0, 0, 'Column1')
sheet1.write(0, 1, 'Column2')
sheet1.write(0, 2, 'Column3')

for i in xrange(10):
    sheet1.write(i + 1, 0, i + 1)
    sheet1.write(i + 1, 1, (100 + 10 * i))
    sheet1.write(i + 1, 2, (1500 + 1500 * i))

sheet1.write(11, 0, 55, Style1)
sheet1.write(11, 1, 1450, Style1)
sheet1.write(11, 2, 82500, Style1)

wb.save('Script9LabAssignment/Lab9.xls')
