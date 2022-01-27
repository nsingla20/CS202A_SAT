from pysat.card import *
cnf = CardEnc.equals(lits=[1, 2, 3],bound=1)
print(cnf.clauses)