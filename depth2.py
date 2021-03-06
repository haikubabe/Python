
class Stack:

    def __init__(self):
        self.items = []
	
    def __iter__(self):
        return iter(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        return self.items




start_state = [2,8,3,1,6,4,7,0,5]

def printstate(state):
        print state[0],state[1],state[2]
        print state[3],state[4],state[5]
        print state[6],state[7],state[8]


def z(state):   
    return state.index(0)

def left(state):
    zeroLoc = z(state)
    state[zeroLoc] = state[zeroLoc-1]
    state[zeroLoc-1] = 0
    return state

def up(state):
    zeroLoc = z(state)
    state[zeroLoc] = state[zeroLoc-3]
    state[zeroLoc-3] = 0
    return state

def right(state):
    zeroLoc = z(state)
    state[zeroLoc] = state[zeroLoc+1]
    state[zeroLoc+1] = 0
    return state

def down(state):
    zeroLoc = z(state)
    state[zeroLoc] = state[zeroLoc+3]
    state[zeroLoc+3] = 0
    return state

def takeaction(state):
    x = z(state)
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
    elif x == 8:
        s.append(left(state[:]))
        s.append(up(state[:]))

    return s

goal_state = [1,2,3,8,0,4,7,6,5]

def goaltest(state):
	if(state==goal_state):
		return True
	else:
		return False
visited=[]

def DLS(node,goal,limit):
    if limit == 0 and node == goal:
        print "SUCCESS------ Goal state is reached"
        return node
    elif limit > 0:
        visited.append(node)
        children = [x for x in takeaction(node) if x not in visited]
        print "\n limit =", limit, "---",children
        for child in children:
            child_result = DLS(child, goal, limit - 1)
            if child_result != "No Solution":
                #print "Success"
                return child_result


    return "No Solution"

def ids(start,goal,maxdepth):
        #for depth in range(1,maxdepth):
                #if start!=goal:
                depth=1
                while (start!=goal and depth<maxdepth):
                        visited = []
                        start=DLS(start,goal,depth,visited)
                #       if start == goal:
                #               return start
                        depth=depth+1


def DFS(start,goal,depth):
	visited=Stack()
	visited.push(start)
	tracking={}
	path=[]
	parent=visited.pop()
	children=[child for child in takeaction(parent)]
	key=str(parent)
	tracking[key]=children
	for c in children:
		visited.push(c)
	if depth==0 and goal in visited.__iter__():
		path.insert(0,key)
		path.insert(0,goal)
		return path
	elif depth>0:
		while not visited.isEmpty():
			parent=visited.pop()
			children=[child for child in takeaction(parent) if child not in visited.__iter__()]
			for c in children:
				if str(c) not in tracking.keys():
					visited.push(c)
			key=str(parent)
			tracking[key]=children
			if goal in [start for start in children]:
				path.insert(0,str(goal))
				path.insert(0,key)
				for key in tracking.keys():
					for value in tracking.get(key):
						if str(parent)==str(value):
							path.insert(0,key)
							parent=key
							break
				return path
			else:
				for c in children:
					#if c not in visited.__iter__():
					#	if str(c) not in tracking.keys():
					#		visited.push(c)
					child_result=DFS(c,goal,depth-1)
					if child_result!="No Solution":
						return child_result
		return "No Solution"
													        	
	
print "\nStart state "
printstate(start_state)
print "\nGoal state "
printstate(goal_state)
print "\noutput: ",DLS(start_state,goal_state,5)

