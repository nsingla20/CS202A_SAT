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