import random
from pysat.solvers import Solver
from pysat.card import *
from sqlalchemy import false, true
from sympy import assumptions
from sudoku_solver import solve,formula_gen,assume_gen,assume_gen_calc
def ran_fill(rows,k):
    for i in range(0,k):
        x=random.randint(1,k*k)
        rows[i*k][i*k]=x
        if k>1:
            y=random.randint(1,k*k)
            while y==x:
                y=random.randint(1,k*k)
            rows[(i+k)*k+k-1][i*k+k-1]=y

def can_remove(rows,k,x,y):
    global s
    c1=rows[x][y]
    rows[x][y]=0
    assume=assume_gen(rows,k)
    for i in range(1,k*k+1):
        assume.append(assume_gen_calc(i,k,x,y))
        if i==c1:
            continue
        elif s.solve(assumptions=assume):
            rows[x][y]=c1
            return False
        del assume[-1]
    rows[x][y]=c1
    return True

def remove(rows,k):
    global s
    x=list(range(0,2*k*k))
    y=list(range(0,k*k))
    random.shuffle(x)
    random.shuffle(y)
    for i in x:
        # print(rows)
        for j in y:
            # temp=rows[:][:]
            if can_remove(rows,k,i,j):
                rows[i][j]=0

def gen(k):
    global s
    s=Solver(name="m22")
    s.append_formula(formula_gen(k).clauses)
    rows=[[0 for i in range(k*k)] for j in range(2*k*k)]
    ran_fill(rows,k)
    
    while not solve(rows,k):
        ran_fill(rows,k)
    # print("random done")
    rows=solve(rows,k)
    remove(rows,k)
    return rows