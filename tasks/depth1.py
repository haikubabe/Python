
p1 = [0,1,2,3,4,5,6,7,8]
p2 = [3,1,2,0,4,5,6,7,8]
p3 = [3,1,2,4,5,8,6,0,7]
p4 = [2,8,3,1,6,4,7,0,5]
def z(p):   #returns the location of the blank cell, which is represented by 0
    return p.index(0)

def left(p):
    zeroLoc = z(p)
    p[zeroLoc] = p[zeroLoc-1]
    p[zeroLoc-1] = 0
    return p

def up(p):
    zeroLoc = z(p)
    p[zeroLoc] = p[zeroLoc-3]
    p[zeroLoc-3] = 0
    return p

def right(p):
    zeroLoc = z(p)
    p[zeroLoc] = p[zeroLoc+1]
    p[zeroLoc+1] = 0
    return p

def down(p):
    zeroLoc = z(p)
    p[zeroLoc] = p[zeroLoc+3]
    p[zeroLoc+3] = 0
    return p

def expand1(p):   #version 1, which generates all successors at once by copying parent
    x = z(p)
    #p[:] will make a copy of parent puzzle
    s = []  #set s of successors

    if x == 0:
        s.append(right(p[:]))
        s.append(down(p[:]))
    elif x == 1:
        s.append(left(p[:]))
        s.append(right(p[:]))
        s.append(down(p[:]))
    elif x == 2:
        s.append(left(p[:]))
        s.append(down(p[:]))
    elif x == 3:
        s.append(up(p[:]))
        s.append(right(p[:]))
        s.append(down(p[:]))
    elif x == 4:
        s.append(left(p[:]))
        s.append(up(p[:]))
        s.append(right(p[:]))
        s.append(down(p[:]))
    elif x == 5:
        s.append(left(p[:]))
        s.append(up(p[:]))
        s.append(down(p[:]))   
    elif x == 6:
        s.append(up(p[:]))
        s.append(right(p[:]))
    elif x == 7:
        s.append(left(p[:]))
        s.append(up(p[:]))
        s.append(right(p[:]))
    else:   #x == 8
        s.append(left(p[:]))
        s.append(up(p[:]))

    #returns set of all possible successors
    return s

goal = [0,1,2,3,4,5,6,7,8]

def DFS(root, goal):    #iterative deepening DFS
    limit = 1 
    while True:
        result = DLS(root, goal, limit)
        if result == goal:
            return result
        limit = limit + 1

visited = []

def DLS(node, goal, limit):    #limited DFS
    if limit == 0 and node == goal:
        print "hi"
        return node
    elif limit > 0:
        visited.append(node)
        children = [x for x in expand1(node) if x not in visited]
        print "\n limit =", limit, "---",children   #for testing purposes only
        for child in children:
            child_result=DLS(child, goal, limit - 1)     
	    if child_result!="No solution":
		return child_result
    
    return "No Solution"



#Below are tests

#print "\ninput: ",p1
#print "output: ",DFS(p1, goal)

#print "\ninput: ",p2
#print "output: ",DLS(p2, goal, 1)
#print "output: ",DFS(p2, goal)

print "\ninput: ",p3
print "output: ",DLS(p3, goal, 50)
#print "output: ",DFS(p4, goal)
