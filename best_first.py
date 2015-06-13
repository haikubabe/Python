import Queue


start_state = [2,8,3,1,6,4,7,0,5]
goal_state = [1,2,3,8,0,4,7,6,5]


coordinates = {0:(0,0), 1:(1,0), 2:(2,0),
               3:(0,1), 4:(1,1), 5:(2,1),
               6:(0,2), 7:(1,2), 8:(2,2)}

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

print "Start state is "
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


def goaltest(state):
	if(goal_state == state):
		return True;
	else:
		return False;


def distance(start,goal):
	no_misplaced_tiles = 0
	for i in range(1,9):
		if start.index(i)!=goal.index(i):
			no_misplaced_tiles += 1
	return no_misplaced_tiles

print "No. of misplaced tiles are:",distance(start_state,goal_state)


def mhd(n, m):
    x1,y1 = coordinates[n]
    x2,y2 = coordinates[m]
    return abs(x1-x2) + abs(y1-y2)


def h(start,goal):
	sum = 0
	for c in range(1,9):
		sum += mhd(start.index(c),goal.index(c))
	return sum

print "Manhattan distance is given by:",h(start_state,goal_state)


def best_first(start,goal):
	open_list = Queue.PriorityQueue()
	open_list.put(state,0)
	closed_list = []

	while not open_list.empty():
		X = open_list.get()
		#closed_list.extend(best_node)
		
		if X==goal:
			return "SUCCESS"
			return X
		else:
			children = [child for child in takeaction(X) if child not in closed_list]
			for c in children:
				a=h(c,goal)
				open_list.put(c,0)
		print "Open list\n",open_list.display()
	return "FAILURE"

print best_first(start_state,goal_state)
