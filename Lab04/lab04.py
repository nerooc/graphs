import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random


#task1 written by Piotr Matiaszewski
def read_matrix_from_file(file_name : str):
	"""Function that reads matrix from file and returns list of lists (matrix) with values provided in file.

	Arguments:
		file_name {str} - path to file 
	
	Returns:
		file_data {list} - list of lists (matrix) with values from provided file splitted by whitespaces 
	"""
	try:

		with open(file_name, "r") as f:

			file_data = [[num for num in line.split()] for line in f]
			return file_data

	except Exception as e:

		raise Exception("Sorry, an error while reading file occured: "+str(e))


def check_if_matrix_has_numbers_only_and_convert_to_ints(matrix : list):

	""" Function checks if 2D matrix [list of lists] contains strings with ints only and if so, converts them to ints
	
	Arguments:
		matrix {list} - matrix that will be converted to matrix of int values
	
	Returns:
		mat {list} - matrix with only int values

	
	"""

	for row in matrix:

		for field in row:

			if(str(field).isdigit()):
				pass
			else:

				raise ValueError("Item "+str(field)+" in given matrix is NOT an int")
	mat=[[int(x) for x in row] for row in matrix]	

	return mat


def check_zeros_on_diag(matrix : list):
	"""Function that checks if given matrix has only zeros on its diagonal.
	
	Arguments: 
		matrix {list} - any matrix to check

	Returns:
		{bool} - True if matrix has only zeros on diagonal, otherwise False
	"""
	only_zeros=True
	for i in range(len(matrix)):

		for j in range(len(matrix[i])):

			if i==j and matrix[i][j]!=0:

				only_zeros=False

	return only_zeros				


def read_digraph_file_return_adjacency_matrix(filename):
	""" Function reads given graph file and if it contains valid data, returns its adjacency matrix. NOTE: The only valid input that may be given in  graph file for this function to work is adjacency matrix representation
	
	Arguments:
		filename {str} - path to file with data

	Returns: 
		matrix {list} - adjacency matrix representation of a graph
	
	"""

	try:

		matrix = read_matrix_from_file(filename)

		matrix = check_if_matrix_has_numbers_only_and_convert_to_ints(matrix)

		only_zeros_on_diag=check_zeros_on_diag(matrix)

		if only_zeros_on_diag:
			return matrix
		else:

			raise Exception("There are some numbers on diagonal that are not equal 0")

	except Exception as e:

		raise Exception("ERROR WHILE READING YOUR MATRIX FILE: \n"+str(e))


def generate_graph_from_adjacency_matrix(matrix):
	""" Function that generates visual representation of a graph and displays it to user. Graph should be provided as an argument and should be in a form of adjacency matrix.
	
	Arguments:
		matrix {list} - adjacency matrix representation of a graph
	"""
	G = nx.DiGraph()
	for i in range(len(matrix)):

		G.add_node(i+1)
	for i in range(len(matrix)):

		for j in range(len(matrix[i])):

			if matrix[i][j]:

				G.add_edge(i+1,j+1)

	pos = nx.circular_layout(G)

	nx.draw(G, pos, with_labels=True, node_size=800)

	plt.show()


def convert_digraph_adjacency_matrix_to_adjacency_list(matrix):
	""" Function that converts adjacency matrix to adjacency list
	Arguments:
		matrix {list} - adjacency matrix of a graph

	Returns: 
		matrix {list} - adjacency list of a graph
	
	"""
	adj_list=[[] for i in matrix]
	for i in range(len(matrix)):

		for j in range(len(matrix[i])):

			if matrix[i][j]:

				adj_list[i].append(j+1)

	return adj_list


def convert_digraph_adjacency_matrix_to_incidence_matrix(matrix):
	""" Function that converts adjacency matrix to incidence matrix
	Arguments:
		matrix {list} - adjacency matrix of a graph

	Returns: 
		matrix {list} - incidence matrix of a graph
	
	"""
	matrix_np=np.array(matrix)

	count=(matrix_np!=0).sum()

	inc_matrix=[[0 for j in range(count)] for i in matrix]

	curr_edge = 0
	for i in range(len(matrix)):

		for j in range(len(matrix[i])):

			if matrix[i][j]:

				inc_matrix[i][curr_edge] =-1

				inc_matrix[j][curr_edge] = 1

				curr_edge += 1
	return inc_matrix

def generate_random_digraph(num_of_vertices, probability):
	""" Function that generates a random digraph.
	Arguments:
		num_of_vertices {int} - number of vertices that generated graph will have
		probability {float} - probability of edge existance between two vertices

	Returns: 
		adj_matrix {list} - adjacency matrix of a generated graph
	
	"""
	if(probability >= 0 and probability <= 1):
		adj_matrix = np.zeros((num_of_vertices, num_of_vertices))

		for a in range(num_of_vertices):

			for b in range(num_of_vertices):

				if random.random() <= probability:
					adj_matrix[a, b] = 1
				else:
					adj_matrix[a, b] = 0

		for a in range(num_of_vertices):

			for b in range(num_of_vertices):

				if(a==b):
					adj_matrix[a][b]=0
	else:

		raise Exception("Probability is not valid (must be float in range [0, 1])")
	return adj_matrix

def pretty_print_adjacency_list(adj_list):
	"""Function that prints adjacency list in a more readible way

	Arguments:
		adj_list {list} - adjacency list representation of the graph
	"""
	if adj_list is not None:
		print('\n'.join([str(index)+".\t"+'\t'.join([str(int(cell)) for cell in row]) for index,row in enumerate(adj_list,start=1)]))
	else:
		raise Exception("Adjacency list is empty.")

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