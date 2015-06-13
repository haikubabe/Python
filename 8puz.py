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

def actions(state):
	actions = []
	index = state.index(0)
	if index % 3 != 0:
		actions.append('left')
	if index % 3 != 2:
		actions.append('right')
	if index > 2:
		actions.append('up')
	if index < 6:
		actions.append('down')
	return actions


def takeaction(state,action):
	result = list(state)
	index = state.index(0)

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

def g(start,goal):
	count=0
	list1=[]
	if start==goal:
		return count
	if start!=goal:
		list1.extend(actions(start))
	#print list1	
print g(start_state,goal_state)
	
def Astar(state,goal):
	Found = False
	open_list = Queue.PriorityQueue()
	open_list.put(state,0)
	closed_list = []
	cost_so_far={}
	cost_so_far[start_state]=0
	#cost=[]
	#cost.append(state)
	#print cost[state]=0
	#g[state] 

	if goaltest(state):
		return ([state],f)

	while not open_list.empty():
		bestnode = open_list.get()
		closed_list.extend(best_node)
		
		if goaltest(best_node):
			Found = True
		else:
			list1 = []
			list1.extend(actions(best_node))
			for l in list1:
			     list2 = []
			     list3 = []
			     successor = takeaction(best_node,l)
			     list2.extend([successor])
			for succ in list2:
				g_of_succ = g(best_node,succ)
				h_of_succ = g(succ,goal_state)
				f_of_succ = g_of_succ + h_of_succ

				#if succ in open_list:
					
  


#print Astar(start_state,goal_state)
	
	
came_from = []	
def path(came_from,current):
	total_path = [current]
	while current in came_from:
		current = came_from[current]
		total_path.append(current)
	return total_path
	

