
class Board:
  def __init__(self):										#constructor 
    self.b = [['0' for i in range(7)] for j in range(6)]	#initialize empty board
    self.played_moves = []
    self.p = '2'

  def generate_moves(self):									#returns available valid moves 
    available_moves = []
    for i in range(7):
      for j in range(6): 
        if(self.b[j][i]=='0'):
          available_moves.append(i)
          break
        else:
          continue
    return  available_moves

  def make_move(self, move):								#makes move in the specified column
    for i in range(5,-1,-1):
      if(self.b[i][move]=='0'):
        if(self.p=='2'):
          self.b[i][move] = '1'
          self.p = '1'
        else:
          self.b[i][move] = '2'
          self.p = '2'
        self.played_moves.append([i,move])
        break
    '''for i in range(6):
      print (self.b[i])
    print("")'''

  def unmake_last_move(self):
    last_move = self.played_moves.pop()
    self.b[last_move[0]][last_move[1]] = '0'
    if(self.p=='1'):
      self.p = '2'
    else:
      self.p = '1'
    '''for i in range(6):
      print (self.b[i])
    print ("")'''

  def last_move_won(self):									#checks if the last move was the winning move
    if not self.played_moves:
      return False
    last_move = self.played_moves[-1]
    row = last_move[0]
    col = last_move[1]
    #print (last_move, row, col)
    ctr = 0

    #check col
    for i in range(6):
      if(self.b[i][col]==self.p):
        ctr = ctr + 1
      else:
        ctr = 0
      if(ctr==4):
       return True

    #check row
    ctr = 0
    for i in range(7):
      if(self.b[row][i]==self.p):
        ctr = ctr + 1
      else:
        ctr = 0
      if(ctr==4):
        return True

    #top left to bottom right - lower triangle   
    for i in range(3):
      c = 0
      ctr = 0
      for r in range(i,6):
        if(self.b[r][c]==self.p):
          ctr = ctr + 1
        else:
          ctr = 0
        if(ctr==4):
          return True 
        c = c + 1

    #top left to bottom right - upper triangle   
    for i in range(1,4):
      r = 0
      ctr = 0
      for c in range(i,7):
        if(self.b[r][c]==self.p):
          ctr = ctr + 1
        else:
          ctr = 0
        if(ctr==4):
          return True
        r = r + 1

    #bottom left to top right - upper triangle
    for i in range(5,2,-1):
      ctr = 0
      c = 0
      for r in range(i,-1,-1):
        if(self.b[r][c]==self.p):
          ctr = ctr + 1
        else:
          ctr = 0
        if(ctr==4):
          return True
        c = c + 1

    #bottom left to top right - lower triangle
    for i in range(1,4):
      ctr = 0
      r = 5
      for c in range(i,7):
        if(self.b[r][c]==self.p):
          ctr = ctr + 1
        else:
          ctr = 0
        if(ctr==4):
          return True
        r = r - 1
    return False

  def __str__(self):  
    temp = ""
    for i in range(6):
      temp = temp + str(self.b[i]) + "\n"
    return temp
