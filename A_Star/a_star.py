#Aniket Shenoy
#ashenoy@iu.edu
#Python 2.7.10

import yaml 
import sys
import Queue as Q

def euclidian(start, end, cities):	#calculates euclidian dist b/w start and end cities
	(x1, y1) = cities[start]
	(x2, y2) = cities[end]
	func = ((x2-x1)**2 + (y2-y1)**2)**.5
	return func

def insert(fringe, s, priority):	#inserts item into priority q
	fringe.put((priority,s))
	return fringe

def remove(fringe):					#removes item from priority q
	s = fringe.get()
	return s, fringe

def children(s,highways, succ):		#returns successors of a node
	for sublist in highways:
		for elem in sublist:
			if elem==s:
				if sublist.index(elem)==0:
					succ[s-1].append(sublist[1])
				else:
					succ[s-1].append(sublist[0])
	return succ

f = open(sys.argv[1], "r")
data = yaml.load(f)					#reads i/p from yaml file into a dict
f.close()

cities = data['cities']	#nodes
highways = data['highways']	#edges
initial = data['start']	#start
goal = data['end']

N = len(cities)

visited = [0]*N 					#maitains list of visited nodes
h = [-1]*N 							#heuristic func
f = [0]*N
g = [0]*N
succ = [[] for i in range(N)] 		#maitains successors of each of the nodes
h[initial-1] = 0	

fringe = Q.PriorityQueue()

if initial==goal:
	print ("Initial state is goal state!")
	sys.exit()
fringe = insert(fringe, initial, 0)
visited[initial-1] = 1
#print fringe.queue 
while True:
	if fringe.empty():
		print "NO PATH EXISTS"
		#print fringe.queue 
		sys.exit()
	tup, fringe = remove(fringe)
	s = tup[1]
	#print "Removing", s, " from fringe"
	#print "Fringe is now: ", fringe.queue
	if s==goal:
		print f[s-1]
		sys.exit()
	succ = children(s, highways, succ)
	#print succ
	for sdash in succ[s-1]:			#iterate over all successors of current node
		if visited[sdash-1]==1:
			continue
		#print "City: ",sdash
		g[sdash-1] = g[s-1] + euclidian(s, sdash, cities)
		#print g[sdash-1]
		h[sdash-1] = euclidian(sdash, goal, cities)
		#print h[sdash-1]
		f[sdash-1] = g[sdash-1] + h[sdash-1]
		#print f[sdash-1]
		insert(fringe, sdash, f[sdash-1])
		visited[sdash-1] = 1
		#print "Inserting ", sdash, " in fringe"
		#print "Fringe is now: ", fringe.queue

