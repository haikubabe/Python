goal_state = [1, 8, 7, 2, 0, 6, 3, 4, 5]
#goal_state = [1, 0, 7, 2, 8, 6, 3, 4, 5]
import sys
global count
def display_board( state ):
	#print "-------------"
	print " %i  %i  %i " % (state[0], state[3], state[6])
	#print "-------------"
	print " %i  %i  %i " % (state[1], state[4], state[7])
	#print "-------------"
	print " %i  %i  %i " % (state[2], state[5], state[8])
	#print "-------------"
def move_up( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [0, 3, 6]:
		temp = new_state[index - 1]
		new_state[index - 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None
def move_down( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [2, 5, 8]:
		temp = new_state[index + 1]
		new_state[index + 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None
def move_left( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [0, 1, 2]:
		temp = new_state[index - 3]
		new_state[index - 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None
def move_right( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [6, 7, 8]:
		temp = new_state[index + 3]
		new_state[index + 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None
def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )
def expand_node( node, nodes ):
	expanded_nodes = []
	expanded_nodes.append( create_node( move_up( node.state ), node, "u", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "d", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "l", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "r", node.depth + 1, 0 ) )
	# Filter the list and remove the nodes that are impossible (move function returned None)
	expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
	expanded_nodes = [node for node in expanded_nodes if node not in nodes] #list comprehension!
	#expanded_nodes = [node for node in expanded_nodes if node.state!= ((node.parent).parent).state] #list comprehension!
	expanded_nodes1 = []
	for node in expanded_nodes:
		temp=node
		temp=temp.parent
		temp=temp.parent
		if temp==None:
			expanded_nodes1.extend(expanded_nodes)
			break
	 	if node.state !=temp.state:
	 		expanded_nodes1.append(node)		 
	return expanded_nodes1
def bfs( start, goal ):
	nodes = []
	count=0
	# Create the queue with the root node in it.
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
	# We've run out of states, no solution.
		if len( nodes ) == 0: 
			return None
	# take the node from the front of the queue
		node = nodes.pop(0)
		count=count+1
		#display_board(node.state)
	# Append the move we made to moves
	# if this node is the goal, return the moves it took to get here.
		if node.state == goal:
			#display_board(node.state)
			moves = []
			temp = node
			print count, " nodes "
			while True:
				moves.insert(0, temp.operator)
				
				if temp.depth == 1:
					 break
				temp = temp.parent
			return moves
	# Expand the node and add all the expansions to the front of the stack
		#count=count+len(expand_node( node, nodes ))
		nodes.extend( expand_node( node, nodes ) )
	
def dfs( start, goal, depth=12 ):
	depth_limit = depth
	# A list (can act as a stack too) for the nodes.
	nodes = []
	count=0
	# Create the queue with the root node in it.
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
	# We've run out of states, no solution.
		if len( nodes ) == 0:
			return None
	# take the node from the front of the queue
		node = nodes.pop(0)
		count=count+1;
	#if this node is the goal, return the moves it took to get here.
		if node.state == goal:
			moves = []
			temp = node
			print count, " nodes "
			while True:
				moves.insert(0, temp.operator)
				if temp.depth <= 1: 
					break
				temp = temp.parent
			return moves #,count
	# Add all the expansions to the beginning of the stack if we are under the depth limit
		if node.depth < depth_limit:
			expanded_nodes = expand_node( node, nodes )
			expanded_nodes.extend( nodes )
			nodes = expanded_nodes
		
def ids( start, goal, depth=50 ):
#	"""Perfoms an iterative depth first search from the start state to the goal. Depth is optional."""
	
	for i in range( depth ):
		result = dfs( start, goal, i )
		#node_count=node_count+count
		if result != None:
			return result
def a_star( start, goal ):
#	"""Perfoms an A* heuristic search"""
	# ATTEMPTED: does not work :(
	nodes = []
	count=0
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
	# We've run out of states - no solution.
		if len( nodes ) == 0:
			return None
	# Sort the nodes with custom compare function.
		nodes.sort( cmp_a_star )
	# take the node from the front of the queue
		node = nodes.pop(0)
		count=count+1
		#display_board(node.state)
	# if this node is the goal, return the moves it took to get here.
		#print "Trying state", node.state, " and move: ", node.operator
		if node.state == goal:
			moves = []
			temp = node
			print count, " nodes "
			while True:
				moves.insert( 0, temp.operator )
				if temp.depth <=1: 
					break
				temp = temp.parent
			return moves
	#Expand the node and add all expansions to the end of the queue
		nodes.extend(expand_node( node, nodes ) )
def cmp_a_star( x, y ):
	# Compare function for A*. f(n) = g(n) + h(n). I use depth (number of moves) for g().
	if (x.depth + h( x.state, goal_state )) > (y.depth + h( y.state, goal_state )):
		return 1
	else:
		return -1	
def h( state, goal ):
#	"""Heuristic for the A* search. Returns an integer based on out of place tiles"""
	score = 0
	for i in range( len( state ) ):
		if state[i] != goal[i]:
			score = score + 1
	return score
def best_first( start, goal ):
#	"""Perfoms an A* heuristic search"""
	# ATTEMPTED: does not work :(
	nodes = []
	count=0
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
	# We've run out of states - no solution.
		if len( nodes ) == 0:
			return None
	# Sort the nodes with custom compare function.
		nodes.sort( cmp_bfs )
	# take the node from the front of the queue
		node = nodes.pop(0)
		#display_board(node.state)
		count=count+1
	# if this node is the goal, return the moves it took to get here.
		#print "Trying state", node.state, " and move: ", node.operator
		if node.state == goal:
			moves = []
			temp = node
			print count, "nodes"
			while True:
				moves.insert( 0, temp.operator )
				if temp.depth <=1: 
					break
				temp = temp.parent
			return moves
	#Expand the node and add all expansions to the end of the queue
		nodes.extend( expand_node( node, nodes ) )
def cmp_bfs( x, y ):
	if h(x.state,goal_state) >= h(y.state,goal_state):
		return 1
	return -1	
# Node data structure
class Node:
	def __init__( self, state, parent, operator, depth, cost ):
		# Contains the state of the node
		self.state = state
		# Contains the node that generated this node
		self.parent = parent
		# Contains the operation that generated this node from the parent
		self.operator = operator
		# Contains the depth of this node (parent.depth +1)
		self.depth = depth
		# Contains the path cost of this node from depth 0. Not used for depth/breadth first.
		self.cost = cost
def readfile( filename ):
	f = open( filename )
	data = f.read()
	# Get rid of the newlines
	data = data.strip( "\n" )
	#Break the string into a list using a space as a seperator.
	data = data.split( " " )
	state = []
	for element in data:
		state.append( int( element ) )
	return state
# Main method
def main():
	starting_state = [2, 1, 7,8, 6, 0, 3, 4, 5]                #goal_state = 1, 2, 3
	### CHANGE THIS FUNCTION TO USE bfs, dfs, ids or a_star      #            8, 0, 4
	print "Initial State"
	display_board(starting_state)
	print "Goal State"                                 #           7, 6, 5
	display_board(goal_state) 
	while True:
		
		print "1.BFS"
		print "2.DFS"
		print "3.IDS"
		print "4.Best-First"
		print "5.A*"
		choice=input("Choose Option:")
		print "-------------"
		if choice==1:                                                      	    
			result = bfs( starting_state, goal_state )
	#print count 
	 	if choice==2:                                                      	    #            7, 6, 5
			result= dfs( starting_state, goal_state )
			#print count,"nodes"
		if choice==3:                                                      	    #            7, 6, 5
			result = ids( starting_state, goal_state )
			#print count,"nodes"
		if choice==4:                                                      	    #            7, 6, 5
			result = best_first( starting_state, goal_state )
		if choice==5:                                                      	    #            7, 6, 5
			result = a_star( starting_state, goal_state )			                                            
		if result == None:
			print "No solution found"
		elif result == [None]:
			print "Start node was the goal!"
		else:
			
			print result
			print len(result), " moves"
			print "-------------"	
# A python-isim. Basically if the file is being run execute the main() function.
if __name__ == "__main__":
	main()
