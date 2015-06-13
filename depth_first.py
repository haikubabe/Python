

class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()
	
	def display(self):
		return self.items
	
	def index(self,item):
		return self.items.index(item)
	def length(self):
		return self.items.len()

open_list = Stack()
open_list.push(start_state)
open_list.display
start_state = [2,8,3,1,6,4,7,0,5]
goal_state = [1,2,3,8,0,4,7,6,5]

print len(start_state)

graph = {1:[2,3],
	 2:[1,4,5,6],
	 3:[1,4],
	 4:[2,3,5],
	 5:[2,4,6],
	 6:[2,5]}


def printstate(state):
	print state[0],state[1],state[2]
	print state[3],state[4],state[5]
	print state[6],state[7],state[8]


def z(state):
	return state.index(0)


def actions(state):
	actions = []
	#index = state.index(0)
	index=z(state)
	if index % 3 != 0:
		actions.append('left')
	if index % 3 != 2:
		actions.append('right')
	if index > 2:
		actions.append('up')
	if index < 6:
		actions.append('down')
	return actions

print
print "Start state:"
printstate(start_state)
#list4 = []
#list4.append(actions(start_state))
#print list4 
print actions(start_state)


def takeaction(state,action):
	result = list(state)
	#index = state.index(0)
	index=z(state)

	if action == 'left':
		tmp = result[index-1]
		result[index-1] = result[index]
		result[index] = tmp
	elif action == 'right':
		tmp = result[index+1]
		result[index+1] = result[index]
		result[index] = tmp
	elif action == 'up':
		tmp = result[index-3]
		result[index-3] = result[index]
		result[index] = tmp
	elif action == 'down':
		tmp = result[index+3]
		result[index+3] = result[index]
		result[index] = tmp
	return result
		

#printstate(takeaction(start_state,'up'))


def goaltest(state):
	if(state == goal_state):
		return True;
	else:
		return False;

#list4 = []
#childrens = []
#list4.extend(actions(start_state))
#for l in list4:
#	a = takeaction(start_state,l)
#	childrens.append(a)
#print childrens
#print goaltest(start_state)
print
print

#def printPath(start):
#	result = ' '
#	for i in range(len([start])):
#		result = result + str([start])
#		if i != len([start]) - 1:
#			result = result + '->'
#	return result

#print "Path is", printPath(start_state)
#print
#print

def dfs(start,goaltest,depth):
	closed_list = [] 
	#child=[]

	if depth == 0 and goaltest(start):
		print "hi"
		return start
	elif depth>0:
		closed_list.append(start)
		for action in actions(start):
			children = takeaction(start,action)
			c = [child for child in takeaction(start,action) if child not in closed_list]
			print "\n Depth = ",depth ,"---", c
		        for b in c:
        			child_result = dfs(b,goaltest,depth - 1)
       				if child_result != "No Solution":
            				return child_result

# note, "else" removed here, so you can fall through to the return from above
	return "No Solution"				



print dfs(start_state,goaltest,5)
