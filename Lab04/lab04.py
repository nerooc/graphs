import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#task2 written by Bartosz Rogowski

def find_components(nr: int, vertex: int, G: np.array, components: list):
	'''Modification of DFS algorithm assigning number of component to every vertex

	Arguments:
		nr {integer} -- actual number of component
		vertex {integer} -- vertex represented by a number
		G {np.array} -- digraph represented by adjacency matrix
		components {list} -- list of integers representing number of component for every vertex
	'''
	u_list = []
	#finding neighbours of node vertex
	for i in range(0, len(G)):
		if i != vertex and G[vertex][i] > 0:
			u_list.append(i)

	for i in u_list:
		if components[i] == -1:
			components[i] = nr
			find_components(nr, i, G, components)


def DFS(G: np.array, visited: list, vertex: int, stack: list):
	'''DFS algorithm (stack version)

	Arguments:
		G {np.array} -- adjacency matrix representing digraph
		visited {list} -- boolean list containing information which vertices has been visited
		vertex {integer} -- vertex represented by a number
		stack {list} -- contains sequence of vertices to visit in the next part of algorithm
	'''
	visited[vertex] = True
	u_list = []
	#finding neighbours of node v
	for i in range(0, len(G)):
		if i != vertex and G[vertex][i] > 0:
			u_list.append(i)

	for i in u_list:
		if visited[i] == False:
			DFS(G, visited, i, stack)
	stack.append(vertex)


def kosaraju(G: np.array):
	'''Kosaraju algorithm using two helper functions: DFS and find_components

	Arguments:
		G {np.array} -- adjacency matrix representing digraph

	Returns:
		comp {list} -- ready list of integers representing number of component for every vertex 
	'''
	### First part: DFS
	visited = []
	stack = []
	for _ in range(len(G)):
		visited.append(False)

	for i in range(0, len(G)):
		if visited[i] == False:
			DFS(G, visited, i, stack)
	
	### Second part: Transpose
	G = G.T
	
	### Third part: DFS with finding components
	comp = []
	for _ in range(len(G)):
		comp.append(-1)

	nr = 0
	for i in stack[::-1]:
		if comp[i] == -1:
			nr += 1
			comp[i] = nr
			find_components(nr, i, G, comp)
			
	return comp


def drawDigraph(G: np.array, components: list):
	'''Function drawing graph components with different colors 
	using function from previous project 

	NOTE: Function can draw up to 13 different components with colors

	Arguments:
		G {numpy array} -- adjacency matrix of a graph
		components {list} -- list containing number of component for every vertex
	'''
	try:
		#creating digraph - needed only for display
		DG = nx.DiGraph()
		DG = nx.from_numpy_matrix(G, create_using=DG)
	except:
		print("An error occured during conversion from np.array to Digraph")

	print('The number of components in this graph:', max(components))
	if max(components) > 13:
		print("WARNING: Components number exceeded a limit for coloring mode")
		pos = nx.circular_layout(DG)
		nx.draw(DG, pos, with_labels=True, node_size=800)
	else:
		#defining 13 colors for each component
		colors = ['blue', 'red', 'lime', 'yellow', 'cyan', 'orange',  
			'purple', 'green', 'pink', 'brown', 'magenta', 'gold', 'silver']
		node_colors = []
		for node in range(0, len(G)):
			number = components[node] - 1 #-1 cause components values start from 1
			node_colors.append(colors[number])
		#drawing graph
		pos = nx.circular_layout(DG)
		nx.draw(DG, pos, node_color=node_colors, with_labels=True, node_size=800)
	plt.show()

############################################################################