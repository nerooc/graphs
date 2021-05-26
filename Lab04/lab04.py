import networkx as nx
import numpy as np
import copy as cp
import matplotlib.pyplot as plt
import random
import math
from lab03 import distance_matrix


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
		raise Exception("An error occured during conversion from np.array to Digraph")

	print('The number of components in this graph:', max(components))
	if max(components) > 13:
		print(f"WARNING: Components number exceeded a limit for coloring mode ({max(components)} > 13)")
		pos = nx.circular_layout(DG)
		nx.draw(DG, pos, with_labels=True, node_size=800)
	else:
		#defining 13 colors for each component
		colors = ['cyan', 'red', 'lime', 'yellow', 'blue', 'orange',  
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

# task 3 by Karol Szeliga

def generate_real_random_complement_digraph(max_vertices_num):
    random_probability = random.uniform(0.0, 1.0)
    adjacency_matrix = generate_random_digraph(max_vertices_num, random_probability)
    comp = kosaraju(adjacency_matrix)
    adjacency_matrix = [list(map(int, adjacency_matrix[i])) for i in range(len(adjacency_matrix))]  # map to int
    if max(comp) == 1:
        return adjacency_matrix
    else:
        return biggest_component(adjacency_matrix, comp)


def biggest_component(adjacency_matrix, comp):
    num_of_big_comp = max(set(comp), key=comp.count)
    places_of_big_comp = []
    for place in range(len(comp)):
        if comp[place] == num_of_big_comp:
            places_of_big_comp.append(place)
    final_length = len(places_of_big_comp)
    component_adjacency_matrix = np.zeros(shape=[final_length, final_length], dtype=int)
    for i in range(final_length):
        for j in range(final_length):
            if adjacency_matrix[places_of_big_comp[i]][places_of_big_comp[j]] == 1:
                component_adjacency_matrix[i][j] = 1
    return component_adjacency_matrix


def add_weights_digraph(adjacency_matrix, min_rand, max_rand):
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                adjacency_matrix[i][j] = random.choice(range(min_rand, max_rand))
    return adjacency_matrix


def bellman_ford(digraph, source_vertex):
    kd = [None for i in range(len(digraph))]
    pop = [None for i in range(len(digraph))]
    kd[source_vertex] = 0
    all_found = True  # fake
    for i in range(len(digraph)):
        for row in range(len(digraph)):
            for col in range(len(digraph)):
                if digraph[row][col] != 0:
                    if kd[col] is None:
                        if kd[row] is not None:
                            kd[col] = kd[row] + digraph[row][col]
                            all_found = False
                    elif kd[row] is not None:
                        if kd[col] > kd[row] + digraph[row][col]:
                            kd[col] = kd[row] + digraph[row][col]
                            pop[col] = row
                            all_found = False
        if all_found:
            break
        else:
            if i == len(digraph)-1:
                print("[bellman_ford: this graph has negative cycle, shortest paths cannot be found]")
        all_found = True  # fake
    return kd


############################################################################

# task 4 by Tomasz Gajda

def pretty_print_w_inf(matrix: list) -> None:
    '''Modified pretty print accepting inf values.

    Arguments:
        matrix {list} -- matrix to be printed
    '''
    if matrix is not None:
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    else:
        raise Exception("Matrix is empty.")

def swap_zero_to_n(graph: list) -> list:
    '''Function swapping all the zeroes to 'N' characters, to be able to
    differentiate weight of 0 and lack of directed edge

	Arguments:
		graph {list} -- adjacency matrix of a graph

    Returns:
		graph_n {list} -- input matrix with zeroes changed to 'N'
	'''
    graph_n = graph

    for r_i, r in enumerate(graph_n):
        for c_i, c in enumerate(r):
            if c == 0:
                graph_n[r_i][c_i] = 'N'
    return graph_n

def add_s(graph: list) -> list:
    '''Function adding a new vertex that is connected
    with all the others.

	Arguments:
		graph {list} -- adjacency matrix of a graph

    Returns:
		graph_n {list} -- input matrix with additional 's' vertex
	'''
    size = len(graph)
    graph_tmp = cp.deepcopy(graph)
    new_row = [0 for _ in range(size)]
    new_row.append('N')
    graph_tmp.append(new_row)

    for r in range(size):
        graph_tmp[r].append('N')

    return graph_tmp

def bellman_ford_2(graph: list, v_start: int) -> tuple:
    '''Function using Bellman-Ford algorithm to check if the graph contains
    a negative weight cycle, or return a list of shortest path from the new S vertex

	Arguments:
		graph {list} -- adjacency matrix of a graph
        v_start {int} -- index of starting vertex

    Returns:
		path_costs -- list of costs for each vertex in the graph
		predecessors -- predecessors of all vertices
	'''
    size = len(graph)
    distances = [math.inf for _ in range(size)]
    predecessors = [None for _ in range(size)]
    distances[v_start] = 0

    for _ in range(size - 1):
        for r_i in range(size):
            for c_i in range(size):
                if graph[r_i][c_i] != 'N':
                    if distances[r_i] + graph[r_i][c_i] < distances[c_i]:
                        distances[c_i] = distances[r_i] + graph[r_i][c_i]
                        predecessors[c_i] = r_i

    for r_i in range(size):
        for c_i in range(size):
            if graph[r_i][c_i] != 'N':
                if distances[r_i] + graph[r_i][c_i] < distances[c_i]:
                    raise Exception("Graph contains a negative weight cycle!")
    
    return distances, predecessors

def johnson(graph: list) -> list:
    '''Function using Johnson's algorithm to create a distance matrix safely, 
    while using both positive and negative weights

	Arguments:
		graph {list} -- adjacency matrix of a graph

    Returns:
		d_m -- distance matrix of a given graph
	'''
    graph = swap_zero_to_n(graph)
    graph_p = add_s(graph)
    weights, _ = bellman_ford_2(graph_p, len(graph))
    size = len(graph)
    for r_i in range(size):
        for c_i in range(size):
            if graph[r_i][c_i] != 'N':
                graph[r_i][c_i] = graph[r_i][c_i] + weights[r_i] - weights[c_i]
    d_m = distance_matrix(graph)
    for r_i in range(size):
        for c_i in range(size):
            d_m[r_i][c_i] = d_m[r_i][c_i] - weights[r_i] + weights[c_i]
    
    return d_m

############################################################################
