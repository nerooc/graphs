import networkx as nx #for task2, task3
import matplotlib.pyplot as plt #for task2, task3
import numpy as np #for task2, task3
import random #for task3


# functions to task1 written by Karol Szeliga

def read_graph_file_return_Adjacency_matrix(file_name, return_input_info=False):
	"""input:
	   file_name - file with correct representation of graph, for example:
	   Adjacency matrix:    Adjacency list:    Incidence matrix:
	   0 1 1                1  2 3             1 1
	   1 0 0                2  1               1 0
	   1 0 0                3  1               0 1
	   return_input_info - change output
	  output (if return_input_info: a) else b) :
	   a) [Adjacency matrix]
	   b) [representation used in file, info which representation it is]
		 possible representations:
		 "adjacency matrix"
		 "adjacency list"
		 "incidence matrix" """

	try:
		with open(file_name, "r") as f:
			file_data = [[int(num) for num in line.split()] for line in f]
			# decode which representation is in input
			itIsList = False
			for row in file_data:
				for i in row:
					if i not in [0, 1]:
						itIsList = True
						f.seek(0)
						file_data2 = [[int(num) for num in remove_first(line.split())] for line in f]  # first int is number of vertex, must be removed
						if return_input_info:
							return file_data, "adjacency list"
						else:
							return convert_Adjacency_list_into_Adjacency_matrix(file_data2)

			if len(file_data) == len(file_data[0]):
				isSymmetric = True  # only a suspicion so far
			else:
				if return_input_info:
					return file_data, "incidence matrix"
				else:
					return convert_Incidence_matrix_into_Adjacency_matrix(file_data)

			for i in range(len(file_data) - 1):
				for j in range(i + 1, len(file_data)):
					if file_data[i][j] != file_data[j][i]:
						isSymmetric = False
						if return_input_info:
							return file_data, "incidence matrix"
						else:
							return convert_Incidence_matrix_into_Adjacency_matrix(file_data)

			diagonalOnlyZero = True
			for i in range(len(file_data)):
				if file_data[i][i] != 0:
					diagonalOnlyZero = False
					if return_input_info:
						return file_data, "incidence matrix"
					else:
						return convert_Incidence_matrix_into_Adjacency_matrix(file_data)

			isTwoOneInCol = True
			count = 0
			for i in range(len(file_data)):
				for j in range(len(file_data)):
					if file_data[j][i] == 1:
						count += 1
				if count != 2:
					isTwoOneInCol = False
					if return_input_info:
						return file_data, "adjacency matrix"
					else:
						return file_data
				else:
					count = 0

			if all([not itIsList, isSymmetric, diagonalOnlyZero, isTwoOneInCol]):
				print("Your matrix could be render as Adjacency matrix or Incidence matrix!\nType 'a' if you mean Adjacency matrix and 'b' if you mean Incidence matrix:")
				while True:
					chosen_option = input()
					if chosen_option in ["a", "b"]:
						break
					else:
						print("Mistyped! Choose again.\nType 'a' if you mean Adjacency matrix and 'b' if you mean Incidence matrix:")
				if chosen_option == "a":
					if return_input_info:
						return file_data, "adjacency matrix"
					else:
						return file_data
				else:
					if return_input_info:
						return file_data, "incidence matrix"
					else:
						return convert_Incidence_matrix_into_Adjacency_matrix(file_data)

	except FileNotFoundError:
		print("\nSorry, there is no file called '" + file_name + "'\n")
		exit(-1)


def remove_first(_list):  # used in read_graph
	_list.pop(0)
	return _list


def convert_Adjacency_matrix_into_Adjacency_list(data_matrix):
	for row in data_matrix:  # loop through a matrix if there is '1' somewhere, print with which vertex
		adj_list = [[set_num(i, row[i]) for i in range(len(row))] for row in data_matrix]
		for _list in adj_list:
			for i in range(len(_list)):
				if -1 in _list:
					_list.remove(-1)
		return adj_list


def set_num(i, num):  # used in convert_Adjacency_matrix_into_Adjacency_list
	if num != 0:
		return i + 1
	else:
		return -1


def convert_Adjacency_matrix_into_Incidence_matrix(data_matrix):
	# count number of edges
	count = 0
	for i in range(len(data_matrix) - 1):
		for j in range(i + 1, len(data_matrix)):
			if data_matrix[i][j] != 0:
				count += 1

	# make incidence matrix
	incidence_matrix = [[0 for x in range(count)] for y in range(len(data_matrix))]
	curr_edge = 0
	for i in range(len(data_matrix) - 1):
		for j in range(i + 1, len(data_matrix)):
			if data_matrix[i][j] != 0:
				incidence_matrix[i][curr_edge] = 1
				incidence_matrix[j][curr_edge] = 1
				curr_edge += 1

	return incidence_matrix


def convert_Adjacency_list_into_Adjacency_matrix(data_matrix):
	adjacency_matrix = [[0 for x in range(len(data_matrix))] for y in range(len(data_matrix))]
	for i in range(len(data_matrix)):
		for j in data_matrix[i]:
			adjacency_matrix[i][j - 1] = 1
	return adjacency_matrix


def convert_Incidence_matrix_into_Adjacency_matrix(data_matrix):
	adjacency_matrix = [[0 for x in range(len(data_matrix))] for y in range(len(data_matrix))]

	w = -1
	h = -1
	for j in range(len(data_matrix[0])):
		for i in range(len(data_matrix)):
			if data_matrix[i][j] != 0:
				if w == -1:
					w = i
				else:
					h = i
		adjacency_matrix[w][h] = 1
		adjacency_matrix[h][w] = 1
		w = -1
		h = -1
	return adjacency_matrix


def convert_Incidence_matrix_into_Adjacency_list(data_matrix):
	temp_adj_matrix = convert_Incidence_matrix_into_Adjacency_matrix(data_matrix)
	return convert_Adjacency_matrix_into_Adjacency_list(temp_adj_matrix)


def convert_Adjacency_list_into_Incidence_matrix(data_matrix):
	temp_adj_matrix = convert_Adjacency_list_into_Adjacency_matrix(data_matrix)
	return convert_Adjacency_matrix_into_Incidence_matrix(temp_adj_matrix)

###############################################################################################

#task2 written by Piotr Matiaszewski

def compute_node_coordinates(number_of_nodes,radius):
	'''Function computing node coordinates from given number of nodes and graphical(visual) radius of one node in final picture.
	Arguments:
		number_of_nodes {int} -- number of nodes in the graph which position will be computed 
		radius {integer or float} --  value determining the size of every node in the final picture
	Returns:
		list -- list containing nodes' coordinates
	'''
	coordinates=[(np.sin(np.pi*2*i/number_of_nodes)*radius, np.cos(np.pi*2*i/number_of_nodes)*radius) for i in range(number_of_nodes)]
	return coordinates


def draw_nodes(data_matrix):
	'''Function creating a graph from given adjacency matrix and positioning every node in correct position.
	Arguments:
		data_matrix {list} -- adjacency matrix representation of graph
	Returns:
		graph {networkx.classes.graph.Graph} -- graph object with properly positioned nodes
	'''
	g=nx.Graph()
	node_value=1 
	number_of_nodes=len(data_matrix)
	coordinates=compute_node_coordinates(number_of_nodes,number_of_nodes*1.0)
	for i in data_matrix:
		g.add_node(node_value,pos=coordinates[node_value-1]) 
		node_value+=1 
	return g


def draw_edges_from_adjacency_matrix(g,data_matrix): #we assume the matrix is symmetrical, what allows us to iterate through its half only
	'''Function adding edges to graph g. Edges are read from adjacency matrix representation of the graph
	Arguments:
		g {networkx.classes.graph.Graph} -- graph object with nodes that are already set and positioned
		data_matrix {list} -- adjacency matrix representation of graph
	Returns:
		g {networkx.classes.graph.Graph} -- graph object with properly positioned nodes and edges
	'''
	for i in range(len(data_matrix)):
		for j in range(i+1,len(data_matrix)):
			if(data_matrix[i][j]==1):
				g.add_edge(i+1,j+1)
	return g

def display_graph(g):
	'''Function displaying graph to user
	Arguments:
		g {networkx.classes.graph.Graph} -- graph object with properly positioned nodes and edges
	'''
	nodes=g.nodes.data()
	edges=g.edges.data()
	number_of_nodes=len(nodes)
	print("Graph will be displayed soon")
	figure, axes = plt.subplots()
	for edge in edges: #drawing edges
		node1=nodes[edge[0]]['pos']
		node2=nodes[edge[1]]['pos']
		plt.plot([node1[0],node2[0]],[node1[1],node2[1]],marker='o',color='black',zorder=1)
	for node in nodes: #drawing nodes
		node_number=node[0]
		node_x_position=node[1]['pos'][0]
		node_y_position=node[1]['pos'][1]
		node_size=number_of_nodes*0.06
		draw_circle = plt.Circle((node_x_position, node_y_position), node_size,zorder=2)
		axes.add_patch(draw_circle)
		label = axes.annotate(node_number, xy=(node_x_position, node_y_position),va="center", ha="center")
		axes.add_artist(draw_circle)
	plt.axis('off')
	plt.axis('square') # square plot provides the real circle shape of graph
	plt.xlim([-1.2*number_of_nodes,1.2*number_of_nodes])
	plt.ylim([-1.2*number_of_nodes,1.2*number_of_nodes])
	plt.show()

def display_graph_coloured_sequences(g,node_colors_tab): #used in previous labs
	'''Function displaying graph with colored nodes to user. It is all commented since it will be useful since lab2
	Arguments:
		g {networkx.classes.graph.Graph} -- graph object with properly positioned nodes and edges
		node_colors_tab {list} -- list containing color of every node   
	'''
	pass
	#pos=nx.get_node_attributes(g,'pos')
	#nx.draw_networkx_nodes(g,pos,node_size=10000/len(pos),node_color=node_colors_tab)#empirycznie
	#nx.draw_networkx_edges(g,pos)
	#nx.draw_networkx_labels(g,pos)
	#plt.axis('square') # square plot provides the real circle shape of graph
	#plt.show()

def draw_graph(data_matrix,node_colors_tab=None):
	''' "Main" function calling other functions in order to draw graph. Depending on the second argument graph will have colored nodes or not
	Arguments:
		data_matrix {list} -- adjacency matrix representation of graph
		node_colors_tab {list} -- list containing color of every node. If not provided, nodes will have default color   
	'''
	graph=draw_nodes(data_matrix)
	graph=draw_edges_from_adjacency_matrix(graph,data_matrix)
	if node_colors_tab == None:
		display_graph(graph)
	#else: #else never happens in lab3, we do not want to color anything
	#	display_graph_coloured_sequences(graph,node_colors_tab)

# ------------------------------THREE FUNCTIONS FOR Lab03 ------------------


def draw_edges_from_adjacency_matrix_with_weights(g,data_matrix): #we assume the matrix is symmetrical, what allows us to iterate through its half only
	'''Function adding edges with weights to graph g. Edges and weights are read from adjacency matrix representation of the graph. 
	Arguments:
		g {networkx.classes.graph.Graph} -- graph object with nodes that are already set and positioned
		data_matrix {list} -- adjacency matrix representation of graph
	Returns:
		g {networkx.classes.graph.Graph} -- graph object with properly positioned nodes and edges
	'''
	for i in range(len(data_matrix)):
		for j in range(i+1,len(data_matrix)):
			if(data_matrix[i][j]!=0):
				g.add_edge(i+1,j+1,weight=data_matrix[i][j])
	return g

def display_graph_with_networkx(g):
	'''Function displaying graph to user using networkx functions
	Arguments:
		g {networkx.classes.graph.Graph} -- graph object with properly positioned nodes and edges
	'''
	pos = nx.circular_layout(g)
	nx.draw(g, pos, node_size=800, with_labels=True)
	labels = nx.get_edge_attributes(g,'weight')
	nx.draw_networkx_edge_labels(g,pos, edge_labels=labels)
	plt.axis('square') # square plot provides the real circle shape of graph
	plt.show()

def draw_graph_with_weights(data_matrix):
	''' Alternative "Main" function calling other functions in order to draw graph with weights.
	Arguments:
		data_matrix {list} -- adjacency matrix representation of graph
		node_colors_tab {list} -- list containing color of every node. If not provided, nodes will have default color   
	'''
	graph=draw_nodes(data_matrix)
	graph=draw_edges_from_adjacency_matrix_with_weights(graph,data_matrix)
	display_graph_with_networkx(graph)

###############################################################################################

#task3 written by Bartosz Rogowski


def generate_graph_a(num_of_vertices: int, num_of_edges: int):
	'''Function generating random graph (number of edges version)
	Arguments:
		num_of_vertices {integer} -- number of vertices
		num_of_edges {integer} -- number of edges
	Returns:
		numpy array -- incidence matrix representing graph
	'''

	if num_of_edges >= 0:
		max_number_of_edges = int(num_of_vertices*(num_of_vertices-1)/2)
		if(num_of_edges > max_number_of_edges):
			raise Exception(f"Number of edges is greater than max value ({max_number_of_edges})")
		G = np.zeros((num_of_vertices, num_of_edges))
		pairing_set = set() #contains pairs of vertices between which edge already exists
		for edge in range(0, num_of_edges):
			try:
				#random.sample generates 2 unique values of given range
				vertex = tuple(random.sample(range(0, num_of_vertices), 2))
				#edge must be singular (simple graph) therefore we need to check whether 
				# it already exists or not 
				if vertex not in pairing_set:
					#adding pairs for example: (1, 4) and (4, 1) since both are the same edge
					pairing_set.add(vertex)
					pairing_set.add(vertex[::-1])
				else:
					while vertex in pairing_set:
						vertex = tuple(random.sample(range(0, num_of_vertices), 2))
					pairing_set.add(vertex)
					pairing_set.add(vertex[::-1])
			except ValueError:
				raise Exception("Number of vertices is too small")
			for i in range(0, 2):
				G[vertex[i], edge] += 1
	else:
		raise Exception("Second argument is not valid (must be positive integer)")
	return G

def generate_graph_b(num_of_vertices: int, probability: float):
	'''Function generating random graph (probability version)
	Arguments:
		num_of_vertices {integer} -- number of vertices
		num_of_edges {integer} -- probability that an edge exists between two vertices
	Returns:
		numpy array -- adjacency matrix representing graph
	'''
	if(probability >= 0 and probability <= 1):
		G = np.zeros((num_of_vertices, num_of_vertices))
		for a in range(0, num_of_vertices-1):
			for b in range(0, num_of_vertices-1-a):
				if random.random() <= probability:
					G[a, a+b+1] = 1
				else:
					G[a, a+b+1] = 0
		for a in range(0, num_of_vertices):
			for b in range(a, num_of_vertices):
				G[b, a] = G[a, b]
		
		count = 0
		for a in range(0, num_of_vertices):
			for b in range(0, num_of_vertices):
				if G[a, b] == 1:
					count += 1

	else:
		raise Exception("Second argument is not valid (must be float in range [0, 1])")
	return G

