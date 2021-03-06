
class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


start_state= [3,1,2,4,5,8,6,0,7]
goal_state = [0,1,2,3,4,5,6,7,8]

def printstate(state):
	print state[0],state[1],state[2]
	print state[3],state[4],state[5]
	print state[6],state[7],state[8]		 

printstate(start_state)



def ind(state):   
    return state.index(0)

def left(state):
    index = ind(state)
    state[index] = state[index-1]
    state[index-1] = 0
    return state

def up(state):
    index = ind(state)
    state[index] = state[index-3]
    state[index-3] = 0
    return state

def right(state):
    index = ind(state)
    state[index] = state[index+1]
    state[index+1] = 0
    return state

def down(state):
    index = ind(state)
    state[index] = state[index+3]
    state[index+3] = 0
    return state

def takeaction(state):   
    x = ind(state)
    
    s = []  

    if x == 0:
        s.append(right(state[:]))
        s.append(down(state[:]))
    elif x == 1:
        s.append(left(state[:]))
        s.append(right(state[:]))
        s.append(down(state[:]))
    elif x == 2:
        s.append(left(state[:]))
        s.append(down(state[:]))
    elif x == 3:
        s.append(up(state[:]))
        s.append(right(state[:]))
        s.append(down(state[:]))
    elif x == 4:
        s.append(left(state[:]))
        s.append(up(state[:]))
        s.append(right(state[:]))
        s.append(down(state[:]))
    elif x == 5:
        s.append(left(state[:]))
        s.append(up(state[:]))
        s.append(down(state[:]))   
    elif x == 6:
        s.append(up(state[:]))
        s.append(right(state[:]))
    elif x == 7:
        s.append(left(state[:]))
        s.append(up(state[:]))
        s.append(right(state[:]))
    else:   
        s.append(left(state[:]))
        s.append(up(state[:]))

    
    return s

def path(came_from,current):
	total_path=[current]
	while current in came_from:
		current = came_from[current]
		total_path.append(current)
	return total_path

#print "Path from initial state to goal state is \n",path(start_state,goal_state)


def printPath(start):
	result = ' '
	for i in range(len([start])):
		result = result + str([start])
		if i != len([start]) - 1:
			result = result + '->'
	return result

#def printpath(start):
#	while start is not None:
			

def BFS(start,goal):
	open_list=Queue()
	open_list.enqueue(start)
	closed_list=[]
	tracking={}
	path=[]

	while not open_list.isEmpty():
		parent=open_list.dequeue()
		if parent in closed_list:
			continue
		closed_list.append(parent)
		#print "\nClosed list ", closed_list
		if parent==goal:
			print "SUCCESS"
			return parent
			#print printPath(X)
		children = [child for child in takeaction(parent) if child not in closed_list]
		for c in children:
			#closed_list.append(children)
			open_list.enqueue(c)
			#print printPath(c)
		print "\nOpen list ", open_list.display()
		#print printPath(c) 
		#print "\nClosed list ", closed_list
	return "Failure"
		
		
print BFS(start_state,goal_state)
