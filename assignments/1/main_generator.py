import time
import random
import csv
from sudoku_generator import gen
from sudoku_solver import solve
from print_sudoku import *
file_name=str(int(time.time()))
# k=random.randint(2,4)
k=3
question=gen(k)
print("Question:")
print_main(question,k)
with open("test/"+str(k)+"_"+file_name+"_q.csv","w",newline="") as csvfile:
    csv.writer(csvfile).writerows(question)

solution=solve(question,k)
print("\nSolution:")
print_main(solution,k)
with open("test/"+str(k)+"_"+file_name+"_s.csv","w",newline="") as csvfile:
    csv.writer(csvfile).writerows(solution)
