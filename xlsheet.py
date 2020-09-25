
import xlwt 
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(1, 0, 'Shivam') 
sheet1.write(2, 0, 'Haris') 
sheet1.write(3, 0, 'Arjun') 
sheet1.write(4, 0, 'Noman') 
sheet1.write(5, 0, 'Anish') 
sheet1.write(0, 1, 'anil') 
sheet1.write(0, 2, 'Kaus') 
sheet1.write(0, 3, 'aman') 
sheet1.write(0, 4, 'Anurag') 
sheet1.write(0, 5, 'sarvesh') 

wb.save('xlwt example.xls') 
