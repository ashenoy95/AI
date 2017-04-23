
import board
import random

def perft(board, depth):	#performance test - verifies working of last_move_won()
	if(depth==0 or board.last_move_won()):
		return 1
	ctr = 0
	moves = board.generate_moves()
	if not moves:
		return 1
	for m in moves:
		board.make_move(m) 
		ctr+=perft(board, depth-1)
		board.unmake_last_move()
	return ctr

def find_win(board, depth):
	ans = negamax_root(board,depth)
	if(ans[0]==1):
		s = "WIN BY PLAYING " + str(ans[1])
		return s
	if(ans[0]==-1):
		return "ALL MOVES LOSE"
	if(ans[0]==0):
		s = "NO FORCED WIN IN " + str(depth) + " MOVES"
		return s

def negamax(board,depth):
	if(board.last_move_won()):
		if(board.p=='1'):
			return -1
		else:
			return 1
	if not board.generate_moves():
		return 0
	if depth==0:
		return 0
	values = []
	for m in board.generate_moves():
		board.make_move(m)
		temp = -negamax(board,depth-1)
		values.append(temp)
		board.unmake_last_move()
	return max(values)

def negamax_root(board,depth):
	if(board.last_move_won()):
		if(board.p=='1'):
			return -1
		else:
			return 1
	if not board.generate_moves():
		return 0
	values = []
	for m in board.generate_moves():
		board.make_move(m)
		values.append((-negamax(board,depth-1),m))
		board.unmake_last_move()
	return max(values)
