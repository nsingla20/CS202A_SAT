# main file for solver that interacts with user
import math
import csv
import time
from print_sudoku import *

from sudoku_solver import solve
input_file=input("Input the path to csv file : ")               # input file must be in test_cases folder
k=-1
rows=[]

# take input from csv file
try:
    with open("test_cases/"+input_file,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            row_int=[]
            for element in row:
                row_int.append(int(element))
            rows.append(row_int)
    k=int(math.sqrt(len(rows)/2))
    print("INPUT:")
    print_main(rows,k)                                          # print the input
except :
    print("\nWrong csv file")
    exit()

start_time=time.time()
result=solve(rows,k)                                            # solve the sudoku
end_time=time.time()

print("\nOUTPUT:")
if result :
    print_main(result,k)                                        # print the output
else:
    print("None")
print("\nTime Taken: "+str(end_time-start_time))