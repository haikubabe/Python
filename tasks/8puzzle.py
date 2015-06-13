

import copy

def successor(astate):
    """
    This function takes an instance of the 8 puzzel problem and generates all the legal successors.
    """
    up = copy.deepcopy(astate)
    """
    important note:
    I use [:] and list() to copy lists but it was not working fine, hence deecopy is used instead.
    """
    down = copy.deepcopy(astate)
    left = copy.deepcopy(astate)
    right = copy.deepcopy(astate)
    successors = []
    for i in range(3):
        for j in range(3):
            if astate[i][j] == 0:
                row = i
                col = j
    if row != 0:
        dummy = up[row][col]
        up[row][col] = up[row -1][col]
        up[row-1][col] = dummy
        successors.append(up)
    if row != 2:
        dummy = down[row][col]
        down[row][col] = down[row+1][col]
        down[row+1][col] = dummy
        successors.append(down)
    if col != 2:
        dummy = right[row][col]
        right[row][col] = right[row][col+1]
        right[row][col+1] = dummy
        successors.append(right)
    if col != 0:
        dummy = left[row][col]
        left[row][col] = left[row][col-1]
        left[row][col-1] = dummy
        successors.append(left)
    return successors


def puzzle(astate):
    """
    This function takes a given instance of the 8 puzzel problem and returns the path to the goal where the goal is defined as below.
    """
    goal = [[1,2,3],[8,0,4],[7,6,5]]    #The goal state.
    generation = [astate]    #Nodes generated at each level.
    tracking = {}    #Track the path to the goal.
    path = []    #The path from the root to the goal.
    parent = generation.pop(0)    #Takes the first element of the list!!
    successors = successor(parent)    #Generate successors.
    key = str(parent)    #keys odictionaries must be hashable and mutable. Lists are illegal keys.
    tracking[key] = successors    #Associate successors with their parent.
    for asuccessor in successors:
        generation.append(asuccessor)    #Generate the first level.
    if goal in generation:    #if the goal is among the successors returns the path to it.
        path.insert(0, key)
        path.insert(0, goal)
        return path
    else:
        while generation != []:    #keep searching!
            parent = generation.pop(0)
            successors = successor(parent)    #generate successors 
            key = str(parent)
            tracking[key] = successors
            if goal in [astate for astate in successors]:    #if the goal is among the successors backtrack its path.
                path.insert(0, str(goal))    #Just because path contains states as strings!!
                path.insert(0, key)
                for key in tracking.keys():
                    for value in tracking.get(key):
                        if str(parent) == str(value):    #If the current (parent) is among the values of (key) then (key) is its parent.
                            path.insert(0, key)
                            parent = key
                            break
                return  path
            else:    #keep searching
                for asuccessor in successors:
                    if asuccessor not in generation:    #If the current successors is already generated do not add it.
                        if str(asuccessor) not in tracking.keys():    #If the successor is a previous parent do not add it.
                            generation.append(asuccessor)
        return
