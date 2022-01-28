import math
import csv
from print_sudoku import *

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
print("INPUT:")
print_main(rows,k)
result=solve(rows,k)
print("\nOUTPUT:")
print_main(result,k)