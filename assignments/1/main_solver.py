import math
import csv

from sqlalchemy import true
from sudoku_solver import solve
input_file="my.csv"
rows=[]
with open(input_file,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        row_int=[]
        for element in row:
            row_int.append(int(element))
        rows.append(row_int)
k=int(math.sqrt(len(rows)/2))
# print(k)
# rows1=[]
# rows2=[]
# for i in range(0,k*k):
#     rows1.append(rows[i])
# for i in range(k*k,2*k*k):
#     rows2.append(rows[i])
result=solve(rows,k)
if result:
    for i in result:
        print(i)
else:
    print(None)