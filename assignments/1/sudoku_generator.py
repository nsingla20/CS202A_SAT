# This file include core sudoku generator functions
import random,time
from pysat.solvers import Solver
from pysat.card import *
from sudoku_solver import solve,formula_gen,get_ans,assume_gen
from sudoku_checker import isValid
# This fills diagonal elements of empty sudokus S1, S2 randomly
def ran_fill(rows,k):
    for i in range(0,k):
        x=random.randint(1,k*k)
        rows[i*k][i*k]=x
        if k>1:
            y=random.randint(1,k*k)
            while y==x:
                y=random.randint(1,k*k)
            rows[(i+k)*k+k-1][i*k+k-1]=y

# This function checks if element at [x][y] can be removed (Uniqueness should not be disturbed)
# def can_remove(val,k,assume):
#     global s
#     fac=10**(int(math.log10(k*k)+1))
#     # c1=rows[x][y]
#     # rows[x][y]=0
#     # assume=assume_gen(rows,k)
#     # for i in range(1,k*k+1):
#     #     assume.append( (int(x/(k*k))+1)*(fac**3) 
#     #                     + (x%(k*k))*fac*fac 
#     #                     + y*fac 
#     #                     + i )
#     #     if i==c1:
#     #         del assume[-1]
#     #         continue
#     #     elif s.solve(assumptions=assume):
#     #         rows[x][y]=c1
#     #         del assume[-1]
#     #         return False
#     #     del assume[-1]
#     # rows[x][y]=c1
#     assume[0]=-assume[0]    
#     return not s.solve(assumptions=assume)

# This function removes random cells in a filled sudoku to maximal extent until it becomes impossible to maintain uniqueness
def remove(rows,k):
    global s
    # x=list(range(0,2*k*k))
    # y=list(range(0,k*k))
    # random.shuffle(x)
    # random.shuffle(y)
    # fac=10**(int(math.log10(k*k)+1))
    assume=[]
    # for i in x:
    #     for j in y:
    #         assume.append((int(i/(k*k))+1)*(fac**3) 
    #                     + (i%(k*k))*fac*fac 
    #                     + j*fac 
    #                     + rows[i][j] )
    # for i in x:
    #     for j in y:
    #         # temp=assume[0]
    #         # del assume[0]
    #         assume[0]=-assume[0]
    #         # if can_remove(rows,k,i,j,assume):
    #         if s.solve(assumptions=assume):
    #             assume.append(-assume[0])
    #             del assume[0]
    #         else:
    #             # assume[0]=-assume[0]
    #             del assume[0]
    #             rows[i][j]=0
    
    assume=assume_gen(rows,k)
    # rows=[[0 for j in range(k*k)] for i in range(2*k*k)]
    for i in range(2*k*k):
        for j in range(k*k):
            rows[i][j]=0
    random.shuffle(assume)
    len=assume.__len__()
    for i in range(len):
        assume[0]=-assume[0]
        if s.solve(assumptions=assume):
            assume.append(-assume[0])
        del assume[0]
    get_ans(assume,rows,k)
    
# main function of this script which fills a empty grid for valid sudoku, then start removing elements
def gen(k,use_dia):
    global s
    # assign a solver
    s=Solver(name="m22")
    s.append_formula(formula_gen(k,use_dia).clauses)
    # make a empty sudoku
    rows=[[0 for i in range(k*k)] for j in range(2*k*k)]
    
    ran_fill(rows,k)            #randomly fills sudoku's diagonal ele in S1, S2
    assume=assume_gen(rows,k)
    while not s.solve(assumptions=assume):    #fills till a valid sudoku is not formed
        ran_fill(rows,k)
        assume=assume_gen(rows,k)
    # print("random done")
    solve(rows,k,use_dia)
    # st=time.time()
    remove(rows,k)
    # end=time.time()
    # print(str(end-st))
    return rows