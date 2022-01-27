# from pysat.card import *
# cnf = CardEnc.equals(lits=[1, 2, 3],bound=1)
# print(cnf.clauses)
from sudoku_solver import solve
k=3
ans=[[0 for i in range(k*k)] for j in range(k*k)]
result=solve(ans,ans,k)
if result:
    for i in result:
        print(i)
else:
    print(None)