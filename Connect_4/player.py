
import random
import board
import search
import time

class Player:
  def __init__(self): #constructor
    self.b = board.Board()
    self.ans = 0
    self.start = 0
    self.limit = 4.499

  def name(self):     #player name
    return 'phant0m'

  def make_move(self, move):
  	self.b.make_move(move)

  def get_move(self): #iterative deepening 
    self.start = time.time()
    #timeout = self.start + 3
  	#move = self.AlphaBeta(self.b,-1000,1000,6)
    for depth in range(1000):
      try:
        self.AlphaBeta(self.b,-1000,1000,depth)
      except:
        #print ("Timed out in ALpha Beta func. Returning move: " + str(self.ans))
        break
      if time.time()-self.start>self.limit:
        #print("Timed out in iterative deepening")
        break
    return self.ans
  	
  #check time at beginning & end  
  def AlphaBeta(self,board,alpha,beta,depth):
    if time.time()-self.start>self.limit:
      raise
      print ("test")
    if(board.last_move_won()):
      if(board.p=='1'):
  			#print ("Printing in p=1")
        return -1
      else:
  			#print ("Printing in p=2")
        return 1
    if not board.generate_moves():
  		#print("Board full")
      return 0
    if depth==0:
  		#print("depth=0")
      return 0
    for m in board.generate_moves():
      board.make_move(m)
      v = -self.AlphaBeta(board,-beta,-alpha,depth-1)
  		#print ("v:",v)
      board.unmake_last_move()
      if v>=beta:
  			#print ("v>=beta")
        return beta
      if v>alpha:
        self.ans=m
        alpha = v
  	#print ("returning alpha")
    return alpha
