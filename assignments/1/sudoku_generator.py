import random
from pysat.solvers import Solver
from pysat.card import *
from sqlalchemy import false, true
from sympy import assumptions
from sudoku_solver import solve,formula_gen,assume_gen
def ran_fill(rows,k):
    for i in range(0,k):
        x=random.randint(1,k*k)
        rows[i*k][i*k]=x
        if k>1:
            y=random.randint(1,k*k)
            while y==x:
                y=random.randint(1,k*k)
            rows[(i+k)*k+k-1][i*k+k-1]=y

def can_remove(rows,k,x,y,s):
    c1=rows[x][y]
    rows[x][y]=0
    for i in range(1,k*k+1):
        rows[x][y]=i
        if i==c1:
            continue
        elif s.solve(assumptions=assume_gen(rows,k)):
            rows[x][y]=c1
            return False
    rows[x][y]=c1
    return True

def remove(rows,k,s):
    for i in range(0,2*k*k):
        # print(rows)
        for j in range(0,k*k):
            # temp=rows[:][:]
            if can_remove(rows,k,i,j,s):
                rows[i][j]=0

def gen(k):
    s=Solver(name="m22")
    s.append_formula(formula_gen(k).clauses)
    rows=[[0 for i in range(k*k)] for j in range(2*k*k)]
    ran_fill(rows,k)
    
    while not solve(rows,k):
        ran_fill(rows,k)
    rows=solve(rows,k)
    print("Solution:")
    for i in rows:
        print(i)
    remove(rows,k,s)
    return rows