import time
import random
import csv
from sudoku_generator import gen
from sudoku_solver import solve
from print_sudoku import *
file_name=str(int(time.time()))
# k=random.randint(2,4)
k=1
while k<2 :
    k=int(input("Provide parameter valid k : "))
if(k>4):
    print("NOTE: Larger k values take time to execute. Please be patient.")
else :
    print("Please maximize your window for better view.")

start_time=time.time()
question=gen(k)
end_time=time.time()
print("Here is your generated sudoku pair:")
print_main(question,k)
with open("test/"+str(k)+"_"+file_name+"_q.csv","w",newline="") as csvfile:
    csv.writer(csvfile).writerows(question)

solution=solve(question,k)
print("\nHere is its unique answer:")
print_main(solution,k)
with open("test/"+str(k)+"_"+file_name+"_s.csv","w",newline="") as csvfile:
    csv.writer(csvfile).writerows(solution)

print("\nTime Taken for generation : "+str(end_time-start_time)+"s")