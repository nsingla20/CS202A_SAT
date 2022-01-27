from pysat.solvers import Solver
from pysat.card import *
from pysat.formula import CNF
import math
import csv
def get_ans(model,k):
    fac=10**(int(math.log10(k*k)+1))
    ans=[[0 for i in range(k*k)] for j in range(k*k)]
    for i in model:
        value=i%fac
        i=int(i/fac)
        y=int(i%fac)
        x=int(i/fac)
        ans[x][y]=value
        print(x,y,value)
    return ans
def assume_gen(rows,k):
    fac=10**(int(math.log10(k*k)+1))
    assume=[]
    for i in range(0,k*k):
        for j in range(0,k*k):
            if(rows[i][j]!=0):
                assume.append(i*fac*fac+j*fac+rows[i][j])
    
    return assume

def formula_gen(k):
    cnf=CNF()
    fac=10**(int(math.log10(k*k)+1))
    for i in range(0,k*k):
        for j in range(0,k*k):
            l=[]
            for z in range(1,k*k+1):
                l.append(i*fac*fac+j*fac+z)
            # print(l)
            cnf.extend(CardEnc.equals(lits=l,bound=1,encoding=0))
    
    for ni in range(0,k):
        for nj in range(0,k):
            
            for n in range(1,k*k+1):
                l=[]
                for i in range(ni*k,ni*k+k):
                    for j in range(nj*k,nj*k+k):
                        l.append(i*fac*fac+j*fac+n)
                cnf.extend(CardEnc.equals(lits=l,bound=1,encoding=0))

    for i in range(0,k*k):
        for z in range(1,k*k+1):
            l=[]
            for j in range(0,k*k):
                l.append(i*fac*fac+j*fac+z)
            cnf.extend(CardEnc.equals(lits=l,bound=1,encoding=0))
    
    for j in range(0,k*k):
        for z in range(1,k*k+1):
            l=[]
            for i in range(0,k*k):
                l.append(i*fac*fac+j*fac+z)
            cnf.extend(CardEnc.equals(lits=l,bound=1,encoding=0))

    return cnf

input_file="hard.csv"
rows=[]
with open(input_file,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        row_int=[]
        for element in row:
            row_int.append(int(element))
        rows.append(row_int)
k=int(math.sqrt(len(rows)))
# print(k)
cnf=formula_gen(k)
# print(cnf.clauses)
s=Solver(name='m22')
s.append_formula(cnf.clauses)
solved=s.solve(assumptions=assume_gen(rows,k))
model=[ele for ele in s.get_model() if ele>0]
print(model)
ans=get_ans(model,k)

for i in ans:
    print(i)




