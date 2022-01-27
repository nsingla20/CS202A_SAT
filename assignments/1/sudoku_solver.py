from pysat.solvers import Solver
from pysat.card import *
from pysat.formula import CNF
import math
def get_ans(model,k):
    fac=10**(int(math.log10(k*k)+1))
    ans=[[0 for i in range(k*k)] for j in range(2*k*k)]
    for i in model:
        value=i%fac
        i=int(i/fac)
        y=int(i%fac)
        i=int(i/fac)
        x=int(i%fac)
        n=int(i/fac)-1
        ans[x+k*k*n][y]=value
    return ans
def assume_gen(rows,k):
    fac=10**(int(math.log10(k*k)+1))
    assume=[]
    for i in range(0,2*k*k):
        for j in range(0,k*k):
            if(rows[i][j]!=0):
                if i<k*k:
                    assume.append(fac**3+i*fac*fac+j*fac+rows[i][j])
                else:
                    assume.append(2*(fac**3)+(i-k*k)*fac*fac+j*fac+rows[i][j])
    
    return assume

def formula_gen(k):
    cnf=CNF()
    fac=10**(int(math.log10(k*k)+1))
    for i in range(0,k*k):
        for j in range(0,k*k):
            l1=[]
            l2=[]
            for z in range(1,k*k+1):
                l1.append(fac**3+i*fac*fac+j*fac+z)
                l2.append(2*fac**3+i*fac*fac+j*fac+z)
            # print(l)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))
    
    for ni in range(0,k):
        for nj in range(0,k):
            
            for n in range(1,k*k+1):
                l1=[]
                l2=[]
                for i in range(ni*k,ni*k+k):
                    for j in range(nj*k,nj*k+k):
                        l1.append(fac**3+i*fac*fac+j*fac+n)
                        l2.append(2*fac**3+i*fac*fac+j*fac+n)
                cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
                cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))

    for i in range(0,k*k):
        for z in range(1,k*k+1):
            l1=[]
            l2=[]
            for j in range(0,k*k):
                l1.append(fac**3+i*fac*fac+j*fac+z)
                l2.append(2*fac**3+i*fac*fac+j*fac+z)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))
    
    for j in range(0,k*k):
        for z in range(1,k*k+1):
            l1=[]
            l2=[]
            for i in range(0,k*k):
                l1.append(fac**3+i*fac*fac+j*fac+z)
                l2.append(2*fac**3+i*fac*fac+j*fac+z)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))

    for i in range(0,k*k):
        for j in range(0,k*k):
            for z in range(1,k*k+1):
                cnf.extend(CardEnc.atmost([fac**3+i*fac*fac+j*fac+z,2*fac**3+i*fac*fac+j*fac+z],encoding=0))
    return cnf
def solve(rows,k):
    cnf=formula_gen(k)
    # print(cnf.clauses)
    s=Solver(name='m22')
    s.append_formula(cnf.clauses)
    solved=s.solve(assumptions=assume_gen(rows,k))
    if solved:
        model=[ele for ele in s.get_model() if ele>0]
        # print(model)
        ans=get_ans(model,k)
        s.delete()
        return ans
    else:
        s.delete()
        return None

