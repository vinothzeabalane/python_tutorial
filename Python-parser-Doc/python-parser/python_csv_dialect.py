'''
Created on Jun 24, 2018

@author: ozeabalx
'''

import csv

csv.register_dialect("hashes", delimiter="#")

f = open(r"C:\Users\ozeabalx\Desktop\python-sesion\sample_csv_write.csv", 'w')

with f:
    writer = csv.writer(f, dialect="hashes")
    writer.writerow(("pens", 4)) 
    writer.writerow(("plates", 2))
    writer.writerow(("bottles", 4))
    writer.writerow(("cups", 1))
print("Execution completed.....")
            
#------------------------------------------------------------------------
# print (csv.list_dialects())
# csv.unregister_dialect("excel-tab")
# print (csv.list_dialects())
#-----------------------------------------------------------------------
# print (csv.get_dialect("excel"))
# print (csv.field_size_limit())