#!/usr/bin/python3
import random

# import csv
#
# str = ""
# with open('C:/Users/admin/Desktop/country', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         str = str + "name = '"+row[0] +"' or "
#
#
# print(str)


for i in range(20):
    print(chr(random.randint(0x4e00, 0x9fbf)))
