'''
Created on Jun 24, 2018

@author: ozeabalx
'''

import csv


# with open(r"C:\Users\ozeabalx\Desktop\python-sesion\sample_csv.csv", 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

        

ifile  = open(r"C:\Users\ozeabalx\Desktop\python-sesion\sample_csv.csv", "r")
reader = csv.reader((line.replace('@|@', '|') for line in ifile), delimiter=',')
ofile  = open(r"C:\Users\ozeabalx\Desktop\python-sesion\sample_csv_write.csv", "w")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
# writer = csv.writer(ofile, delimiter='|', quotechar='"', quoting=csv.QUOTE_NONE)
for row in reader:
    writer.writerow(row)
ifile.close()
ofile.close()
print("Execution completed.....")

"""
csv.QUOTE_ALL - Quote everything, regardless of type.
csv.QUOTE_MINIMAL - Quote fields with special characters
csv.QUOTE_NONNUMERIC - Quote all fields that are not integers or floats
csv.QUOTE_NONE - Do not quote anything on output

"""
# Reference URL - https://pymotw.com/2/csv/
