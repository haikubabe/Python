state1 = [0,1,2,3,4,5,6,7,8]
state2 = [3,1,2,0,4,5,6,7,8]
state3 = [3,1,2,4,5,8,6,0,7]
#state4=[2,8,3,1,6,4,7,0,5]

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

goal_state = [0,1,2,3,4,5,6,7,8]

def goaltest(state):
	if(state==goal_state):
		return True
	else:
		return False


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

print "\nStart state "
printstate(start_state)
print "\nGoal state "
printstate(goal_state)
print "\noutput: ",DLS(start_state,goal_state,5)

