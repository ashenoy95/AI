from copy import deepcopy
from itertools import chain

class Solver:
  def __init__(self, cnf):
    self.clauses = cnf
    all = list(chain(*self.clauses))
    #print (all)
    self.symbols = set([a for a in all if a>0])|set([abs(a) for a in all if a<0])

  def solve(self):
    return self.dpll(self.clauses,self.symbols)

  def reduce(self, clauses, p):
    #print('p:',p)
    #print("clauses passed as parameter:",clauses)
    alpha = deepcopy(clauses)
    for c in clauses:
        if p in c:
            alpha.remove(c)
        if -p in c:
          alpha[alpha.index(c)].remove(-p)
    #print('from reduce method', alpha)
    #print("clauses passed as parameter:",clauses)
    return alpha

  def dpll(self, clauses, symbols): 
    #print("clauses:",clauses)
    for c in clauses:
      if len(c)==1:
        #print ("unit:",c)
        p = list(c)[0]
        #print ("p:",p)
        alpha = list(clauses)
        s = symbols.copy()
        for c in clauses:
          if p in c:
            alpha.remove(c)
          if -p in c:
            alpha[alpha.index(c)].remove(-p)
        if abs(p) in symbols:
          #print("removing from unit_prop",p)
          s.remove(abs(p))
        symbols = s
        clauses = alpha
    if not clauses:
      return True
    for c in clauses:
      if len(c) == 0:
        return False

    clauses_cp = list(clauses)
    #print("\nsymbols:",symbols,"\n")
    s = symbols.copy()
    ctr = {i:0 for i in s}
    for c in clauses:
      for i in s:
        if i in c:
          ctr[i]+=1
    #print (ctr)
    m = ctr[i]
    for i in s:
      if ctr[i]>=m:
        m = ctr[i]
        p = i
    s.remove(abs(p))
    #print ("\nreducing",p)
    reduced1 = self.reduce(clauses,p)
    #print("rediced1:",reduced1)
    #print("clauses:",clauses)
    #print("copy of clauses:",clauses_cp)
    reduced2 = self.reduce(clauses_cp,-p)
    #print("rediced2:",reduced2)
    return (self.dpll(reduced1,s) or self.dpll(reduced2,s))

