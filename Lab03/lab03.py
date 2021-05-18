from queue import PriorityQueue # for task 2
import numpy as np #for task 5
import networkx as nx #for task 5
import matplotlib.pyplot as plt #for task 5

# import for task 1
import random
from lab01 import generate_graph_b
from lab02 import COMPONENTS, find_vertices_of_biggest_component, graph_randomization, pretty_print


# task 1 written by Karol Szeliga

#  cuts all connections of vertex v (sets all ones in row/col to zero)
def zeros_vertex_degree(adjacency_matrix, v):
    for j in range(len(adjacency_matrix[v])):
        adjacency_matrix[v][j] = 0
    for i in range(len(adjacency_matrix)):
        adjacency_matrix[i][v] = 0
    return adjacency_matrix


def delete_empty_vertices(adjacency_matrix):
    no_ones_in_row = True
    i = 0
    while i < len(adjacency_matrix):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1.0:
                no_ones_in_row = False
        if no_ones_in_row:
            adjacency_matrix.pop(i)
            for k in range(len(adjacency_matrix)):
                adjacency_matrix[k].pop(i)
            i -= 1
        no_ones_in_row = True
        i += 1
    adjacency_matrix_without_empty_vertices = adjacency_matrix
    return adjacency_matrix_without_empty_vertices


def add_int_weights(adjacency_matrix, min_int_weight=1, max_int_weight=10):
    if adjacency_matrix == 1:
        return int(random.choice(range(min_int_weight, max_int_weight)))
    for i in range(len(adjacency_matrix)):
        for j in range(i, len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                adjacency_matrix[i][j] = int(random.choice(range(min_int_weight, max_int_weight)))
            else:
                adjacency_matrix[i][j] = int(0)
    for i in range(len(adjacency_matrix)):
        for j in range(i):
            adjacency_matrix[i][j] = adjacency_matrix[j][i]
    adjacency_matrix_with_weights = adjacency_matrix
    return adjacency_matrix_with_weights


def generate_random_graph(max_vertex_num):
    random_probability = random.uniform(0.0, 1.0)
    adjacency_matrix = generate_graph_b(max_vertex_num, random_probability)
    mixed_adjacency_matrix = graph_randomization(adjacency_matrix)
    vertices_in_final_matrix = find_vertices_of_biggest_component(COMPONENTS(mixed_adjacency_matrix))
    if len(vertices_in_final_matrix) < 2:
        return [1]
    if len(vertices_in_final_matrix) < len(mixed_adjacency_matrix[0]):
        for v in range(len(mixed_adjacency_matrix[0])):
            if not vertices_in_final_matrix.__contains__(v+1):
                mixed_adjacency_matrix = zeros_vertex_degree(mixed_adjacency_matrix, v)
    component_mixed_adjacency_matrix = delete_empty_vertices(mixed_adjacency_matrix)
    return component_mixed_adjacency_matrix

########################################################################

# task 2 written by Tomasz Gajda

def get_neighbours(graph: list, v: int) -> list:
	'''Function finding all neighbours to a given vertex and returning
	them as a list
	Arguments:
		graph {list} -- graph in form of an adjacency matrix
		v {int} -- vertex for which we are looking for neighbours
	
	Returns:
		list -- list of neighbours of given vertex
	'''
	rank = len(graph)
	neighbours = []
	
	for i in range(rank):
		if graph[v][i] > 0:
			neighbours.append(i)
	
	return neighbours


def dijkstra(graph: list, v_start: int) -> tuple:
	'''Dijkstra algorithm implementation, finding costs of each path
	and predecessors of all vertices
	
	Arguments:
		graph {list} -- graph in form of an adjacency matrix
		v_start {int} -- vertex from which we start the process
	
	Returns:
		path_costs -- list of costs for each vertex in the graph
		predecessors -- predecessors of all vertices
	'''
	rank = len(graph)
	path_costs = [2**32 for _ in range(rank)]
	predecessors = [None for _ in range(rank)]
	path_costs[v_start] = 0

	Q = PriorityQueue()
	for v in range(rank):
		Q.put((path_costs[v], v))

	while not Q.empty():
		u_cost, u = Q.get()
		u_neighbours = get_neighbours(graph, u)
		
		for n in u_neighbours:
			if path_costs[n] > path_costs[u] + graph[u][n]:
				path_costs[n] = path_costs[u] + graph[u][n]
				predecessors[n] = u
				Q.put((path_costs[n], n))

	return path_costs, predecessors


def get_path(predecessors: list, v_start: int, v_end: int) -> list:
	'''Function finding shortest path from a given start vertex to a given end vertex
	Arguments:
		predecessors {list} -- predecessors of all vertices
		v_start {int} -- vertex from which we start the process
		v_end {int} -- vertex where we end the process
	Returns:
		path {list} -- shortest path in form of list of vertices
	'''
	path = []
	v_temp = v_end

	while v_temp != v_start:
		path.append(v_temp)
		v_temp = predecessors[v_temp]
	path.append(v_start)
	path.reverse()
	
	return path


def print_dijkstra(path_costs: list, predecessors: list, v_start: int) -> None:
	'''Function printing out all the shortest paths (to all different vertices) and costs
	Arguments:
		path_costs {list} -- list of costs for each vertex in the graph
		predecessors {list} -- predecessors of all vertices
		v_start {int} -- vertex from which we start the process
	'''
	rank = len(path_costs)
	print("START: s = " + str(v_start))

	for v in range(rank):
		print("d({0}) = {1} ==> {2}". format(v, path_costs[v], str(get_path(predecessors, v_start, v))))

########################################################################

# task 3 written by Tomasz Gajda

def distance_matrix(graph: list) -> list:
	'''Function printing out the distance matrix with distances between every pair of vertices
	Arguments:
		graph {list} -- graph in form of an adjacency matrix
    Returns:
        distance_matrix {list} -- constructed distance matrix
	'''
	distance_matrix = []
    
	for v in range(len(graph)):
		path_costs, _ = dijkstra(graph, v)
		distance_matrix.append(path_costs)
	
	return distance_matrix

########################################################################

# task 4 written by Piotr Matiaszewski

def get_graph_centre_from_distance_matrix(distance_matrix: list) -> dict:
	""" Function computing graph centre (vertex that has the smallest sum of distances to other vertices). If there is more than one, function returns all of them.
	Arguments: 
		distance_matrix {list} -- matrix of distances from every vertex to another (distance_matrix[i][j] equals distance_matrix[j][i])
	
	Returns:
		final_total_distances {dict} -- dictionary containing as keys number of vertex and as values total sum of distances from found graph centre (corresponding key) to all other vertices
	"""
	total_distance_from_others = {}
	final_total_distances={} #we have plural form here cause there might be more than one graph centre
	for index, row in enumerate(distance_matrix, start = 1):
		total_distance_from_others[index] = sum(row)
	minval = min(total_distance_from_others.values())
	indexes_of_centre_vertices = [k for k, v in total_distance_from_others.items() if v==minval]
	for i in indexes_of_centre_vertices:
		final_total_distances[i]=total_distance_from_others[i]
	return final_total_distances


def get_minimax_centre_from_distance_matrix(distance_matrix: list) -> dict:
	""" Function computing minimax centres (vertices that have the smallest distance to the farthest vertex).
	Arguments: 
		distance_matrix {list} -- matrix of distances from every vertex to another (distance_matrix[i][j] equals distance_matrix[j][i])
	
	Returns:
		final_total_distances {dict} -- dictionary containing as keys minimax centers and as values distances to the farthest vertex from current minimax centre(key)
	"""
	max_distances_to_farthest_vertex = {}
	final_total_distances={} #we have plural form here cause there might be more than one minimax centre
	for index, row in enumerate(distance_matrix, start = 1):
		max_distances_to_farthest_vertex[index] = max(row)
	minval = min(max_distances_to_farthest_vertex.values())
	indexes_of_centre_vertices = [k for k, v in max_distances_to_farthest_vertex.items() if v==minval]
	for i in indexes_of_centre_vertices:
		final_total_distances[i]=minval
	return final_total_distances

def print_centers_function(distance_matrix: list) -> None:
    """Function that prints centers and minimax centers for provided distance matrix of a graph

    Arguments:
		distance_matrix {list} -- distance matrix of a graph
    
    """
    pretty_print(distance_matrix)
    found_centres=get_graph_centre_from_distance_matrix(distance_matrix)
    if len(found_centres)>1:
        print("\nThere is more than one graph center!")
    for center in found_centres:
        print("\nCenter = " + str(center) + " (Distances sum = " +
            str(found_centres[center])+").")
    minimax_centers=get_minimax_centre_from_distance_matrix(distance_matrix)
    print("-------------------------------------------------------")
    if len(minimax_centers)>1:
        print("\nThere is more than one minimax center!")
    print()
    for minimax in minimax_centers:
        print("Minimax center = "+str(minimax)+" (Distance from the farthest: "+str(minimax_centers[minimax])+")\n")

########################################################################

#task 5 written by Bartosz Rogowski
def find(parents: list, u: int) -> int:
	'''Returns parent node of vertex u

	Arguments:
		parents {list} -- list containing parent fof each vertex
		u {int} -- vertex which parent will be returned
	'''
	if parents[u] == u:
		return u
	return find(parents, parents[u])

def make_union(parents: list, rank: list, u: int, v: int):
	'''Function making union of sets of vertices - u and v

	Arguments:
		parents {list} -- list containing parent fof each vertex
		rank {list} -- list containing number of rank for every vertex (needed for detecting cycles)
		u {int} -- vertex u
		v {int} -- vertex v
	'''
	u_parent = find(parents, u)
	v_parent = find(parents, v)
	if rank[u_parent] < rank[v_parent]:
		parents[u_parent] = v_parent
	elif rank[u_parent] > rank[v_parent]:
		parents[v_parent] = u_parent
	else:
		parents[v_parent] = u_parent
		rank[u_parent] += 1

def kruskal(adjacency_matrix: np.array) -> list:
	'''Implementation of Kruskal algorithm to find the minimal spanning tree in given graph

	Arguments:
		adjacency_matrix {np.array} -- adjacency matrix of graph (with weights)

	Returns:
		results {list} -- list of edges and their weights in form: 
			[(1, 4), 3] - edge from vertex 1 to 4 has weight of 3
	'''
	results = []
	parents = []
	rank = []

	G = nx.Graph()
	G = nx.from_numpy_matrix(adjacency_matrix, create_using=G)
	labels = nx.get_edge_attributes(G,'weight')
	if not labels:
		print("Sorry, graph does not contain a single edge")
		exit(-1) 
	#sorting edges by their weights
	sorted_labels = sorted(labels.items(), key = lambda x:(x[1], x[0]))
	#sorted_labels contains list of pairs of vertices and edge weight
	#for example: [(1, 4), 3] - edge from vertex 1 to 4 has weight of 3

	#Initial conditions os lists
	for node in range(len(G)):
		parents.append(node)
		rank.append(0)

	#Index variable used for sorted edges
	i = 0
	#Index variable used for result array
	e = 0

	#MST has (number_of_vertices - 1) edges
	while e < len(G) - 1:
		u = sorted_labels[i][0][0]
		v = sorted_labels[i][0][1]
		weight = sorted_labels[i][1]
		i += 1
		u_parent = find(parents, u)
		v_parent = find(parents, v)

		#If including this edge does not cause cycle, include it in result
		#and increment the index of result for next edge
		if u_parent != v_parent:
			e += 1
			results.append([(u, v), weight])
			make_union(parents, rank, u_parent, v_parent)

	return results

def visualizeMST(adjacency_matrix: np.array, weighted_edges: list):
	'''Function drawing MST of given graph if it exists based on weighted_edges already
	proven to be MST edges

	Arguments:
		adjacency_matrix {np.array} -- matrix representing graph
		weighted_edges {list} -- list on edges and their weights of MST
	'''

	G = nx.Graph()
	G = nx.from_numpy_matrix(adjacency_matrix, create_using=G)
	labels = nx.get_edge_attributes(G, 'weight')
	colors = [] #list of colors for MST edges
	labels2 = [] #needed for comparison of edges (for MST)
	for key, value in labels.items():
		temp = [key, value]
		labels2.append(temp)

	for element in labels2:
		if element in weighted_edges:
			colors.append('red')
		else:
			colors.append('gray')

	pos = nx.circular_layout(G)
	nx.draw(G, pos, node_size=800, with_labels=True, edge_color=colors)
	labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
	plt.show()
