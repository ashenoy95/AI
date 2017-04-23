import math
import random

class Solver:
  def __init__(self, mdp):
    self.mdp = mdp
    self.policy = {}
    self.states = self.mdp.S()
    self.actions = self.mdp.A()
    self.gamma = self.mdp.gamma()
    self.V = dict([(s,0) for s in self.states])
    self.theta = random.uniform(.1,.01)

  def summation(self, state, action):
    sum = 0
    for sdash in self.states:
      val = self.mdp.P(state, action, sdash)*(self.mdp.R(sdash) + self.gamma * self.V[sdash])
      sum+= val
      #print("R(",sdash[0],",",sdash[1],"):",self.mdp.R(sdash))
      #print('(',state[0],',',state[1],')->(',sdash[0],",",sdash[1],'):',val)
    #print(sum)
    return sum

  def val_iter(self):
    while True:
      delta = 0
      for s in self.states:
        v = self.V[s]
        m = -math.inf
        optimal = ""
        for a in self.actions:
          current = self.summation(s,a)
          #print("for",a,"sum=",current,"\n")
          if current>m:
            m = current
            optimal = a
        #print("Optimal:",optimal)
        self.V[s] = m
        self.policy[s] = optimal
        #print("policy:",self.policy,"\n")
        delta = max(delta, abs(v - self.V[s]))
      if delta<self.theta:
        return 

  def solve(self):
    # returns a random policy
    #return {s : random.choice(self.mdp.A()) for s in self.mdp.S()}
    self.val_iter()
    return self.policy



