import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time #for task 2
import random #for task 2
from lab01 import * #for task 2, 3, 6


# functions to task 1 written by Bartosz Rogowski
def isDegreeSequence(List_org: list):
	'''Function checking whether sequence in given argument is a degree sequence
	
	Arguments:
		List_org {list} -- list that contains int values
	Returns:
		boolean -- is List a degree sequence
	'''
	List = List_org.copy() #we dont want to modify original list
	if not all(isinstance(elem, int) for elem in List):
		print('WARNING: All elements in a list have to be integers.')
		return False
	
	List.sort(reverse=True)
	odd_elements_number = 0
	for i in range(len(List)):
		if List[i]%2 == 1:
			odd_elements_number += 1
	if odd_elements_number%2 == 1:
		return False
	
	while True:
		if all(value == 0 for value in List):
			return True
		if List[0] < 0 or List[0] >= len(List) or any(value < 0 for value in List):
			return False
		for i in range(1, List[0]+1):
			List[i] -= 1
		List.pop(0) #instead of List[0] = 0
		List.sort(reverse=True)

#############################################################

# task 2 by Karol Szeliga

def graph_randomization(adjacency_matrix):
	"""
	:param adjacency_matrix: 
	:return: randomised adjacency_matrix
	"""
	## some explanation
	# algorithm mixes edges in graph without changing vertex degrees

	# using adjacency list it finds randomly 4 vertices (A,B,C,D) with:
	# 1. edges between A-B and C-D
	# 2. not edges between A..C and C..D
	# When vertices are found edges are mixed:
	# A-B C-D are swapped to A-C B-D

	# algorithm repeats finding and swapping several times depend on size of the graph
	
	work_on_complement = False
	if count_edges(adjacency_matrix) > int(full_graph_edges(len(adjacency_matrix))/2):
		adjacency_matrix = graph_complement(adjacency_matrix)
		work_on_complement = True

	adjacency_list = convert_Adjacency_matrix_into_Adjacency_list(adjacency_matrix)

	all_selectable_ver = list(range(len(adjacency_list)))
	for i in range(len(all_selectable_ver)):  # sort out empty and full vertices
		if len(adjacency_list[i]) == 0 or len(adjacency_list[i]) == len(adjacency_list) - 1:
			all_selectable_ver.remove(i)
	# print("all selectable vertices -> ", all_selectable_ver)

	# number of finding and swapping
	mixes_number = random.choice(range(int(len(adjacency_list) / 2), int(len(adjacency_list))))
	for i in range(mixes_number):
		if len(all_selectable_ver) < 2:
			print("[This graph cannot be randomise, return with no swap]")
			break
		edgesAllA = all_selectable_ver.copy()
		foundAll = False
		iverA, iverD, verB, verC = [0, 0, 0, 0]
		graphImposibleToRand = False
		foundA = False
		while not foundA:
			iverA = random.choice(edgesAllA)  # iterator for first 'A' vertex (iverA = i -> i+1 vertex)
			edgesAllD = all_selectable_ver.copy()
			edgesAllD.remove(iverA)
			foundA = True
			foundD = False
			while not foundD:
				iverD = random.choice(edgesAllD)  # iterator for second 'D' vertex  (iverD = i -> i+1 vertex)
				if adjacency_list[iverA].__contains__(iverD + 1):  # if D-A then find another D
					if len(edgesAllD) <= 1:
						foundA = False
						foundD = True  # fake, return and try to find another A
					else:
						edgesAllD.remove(iverD)
				else:
					foundD = True
					edgesA = adjacency_list[iverA].copy()
					foundB = False
					while not foundB:
						verB = random.choice(edgesA)  # vertex B
						# B will never be D, because there is no A-D
						edgesD = adjacency_list[iverD].copy()
						if edgesD.__contains__(verB):
							if len(edgesD) <= 1:
								foundD = False
								foundB = True  # fake, return and try to find D again
								foundC = True  # fake, return and try to find D again
							else:
								edgesD.remove(verB)
								foundB = True
								foundC = False
						else:
							foundB = True
							foundC = False
						while not foundC:
							verC = random.choice(edgesD)  # vertex C
							if not adjacency_list[verC - 1].__contains__(verB):
								foundC = True
								foundAll = True  # if found C, then all vertices has correct edges
							else:
								if len(edgesD) <= 1:
									foundB = False
									foundC = True  # fake, return and try to find B and C again
								else:
									edgesD.remove(verC)  # try to find another C
						if not foundB:
							if len(edgesA) <= 1:
								foundD = False
								foundB = True  # fake, return and try to find D again
							else:
								edgesA.remove(verB)  # try to find another B
					if not foundD:
						if len(edgesAllD) <= 1:
							foundA = False
							foundD = True  # fake, return and try to find another A
						else:
							edgesAllD.remove(iverD)  # try to find another D
				if not foundA:
					if len(edgesAllA) <= 1:
						foundA = True  # fake, this graph cannot be randomise!!!
						graphImposibleToRand = True
					else:
						edgesAllA.remove(iverA)  # try to find another D

		if graphImposibleToRand:
			print("[This graph cannot be randomise, return with no swap]")
			break
		else:
			# mixing
			# print(iverA+1,"-X-", verB," ", verC,"-X-", iverD+1)
			# print(iverA+1,"-", iverD+1," ", verC,"-", verB)
			# print()
			iAB = adjacency_list[iverA].index(verB)
			adjacency_list[iverA][iAB] = iverD + 1
			iDC = adjacency_list[iverD].index(verC)
			adjacency_list[iverD][iDC] = iverA + 1

			iBA = adjacency_list[verB - 1].index(iverA + 1)
			adjacency_list[verB - 1][iBA] = verC
			iCD = adjacency_list[verC - 1].index(iverD + 1)
			adjacency_list[verC - 1][iCD] = verB

	if work_on_complement:
		return graph_complement(convert_Adjacency_list_into_Adjacency_matrix(adjacency_list))
	else:
		return convert_Adjacency_list_into_Adjacency_matrix(adjacency_list)


def count_edges(adjacency_matrix):
	count = 0
	for i in range(len(adjacency_matrix) - 1):
		for j in range(i + 1, len(adjacency_matrix)):
			if adjacency_matrix[i][j] == 1:
				count += 1
	return count


def set_opposite(cell):
	if cell == 0:
		return 1
	else:
		return 0


def graph_complement(adjacency_matrix):
	complement_adjacency_matrix = [[set_opposite(cell) for cell in row] for row in adjacency_matrix]
	for i in range(len(complement_adjacency_matrix)):
		complement_adjacency_matrix[i][i] = 0
	return complement_adjacency_matrix


def full_graph_edges(length):
	return length*(length-1)/2

####################################################################################

# functions to task 3 written by Bartosz Rogowski
def degSeq2adjMat(List_org: list):
	''' Function converting degree sequence to adjacency matrix.
	
	NOTE: I assume that sequence is already proven to be a degree sequence
	Arguments:
		List_org {list} -- degree sequence
	Returns:
		A {numpy array} -- adjacency matrix made of degree sequence
	'''

	List = List_org.copy() #we dont want to modify original list
	n = len(List)
	A = np.zeros((n, n))
	d = zip(list(range(0, n)), List)
	d = [list(elem) for elem in d]
	d = sorted(d, key=lambda obj: obj[1], reverse=True)
	for _ in range(0, n):
		for i in range(1, d[0][1]+1):
			A[d[0][0], d[i][0]] = 1
			A[d[i][0], d[0][0]] = 1
			d[i][1] -= 1
		d.pop(0)
		d = sorted(d, key=lambda obj: obj[1], reverse=True)
	return A

def COMPONENTS_R(nr: int, v: int, G: np.array, comp: list):
	'''Depth-first search starting from node v
	Arguments:
		nr {int} -- actual number of component
		v {int} -- number of actual node
		G {numpy array} -- adjacency matrix
		comp {list} -- components list
	Returns:
		<does not return anything>
	'''
	u_list = []
	#finding neighbours of node v
	for i in range(0, len(G)):
		if i != v and G[v][i] > 0:
			u_list.append(i)
	#

	for u in u_list:
		if comp[u] == -1:
			comp[u] = nr
			COMPONENTS_R(nr, u, G, comp)
		

def COMPONENTS(G: np.array):
	'''Function finding components of the graph 
	Arguments:
		G {numpy array} -- adjacency matrix of a graph
	Returns:
		comp {list} -- every element is a number of component for every node in graph G
	'''
	comp = []
	nr = 0
	# -1 means that vertex has not been visited yet
	for node in range(0, len(G)):
		comp.append(-1)
	for node in range(0, len(G)):
		if comp[node] == -1:
			nr += 1
			comp[node] = nr
			COMPONENTS_R(nr, node, G, comp)
	return comp


def drawGraph(G: np.array, components: list):
	'''Function drawing graph components with different colors 
	using function from previous project

	NOTE: Function can draw up to 13 different components with colors

	Arguments:
		G {numpy array} -- adjacency matrix of a graph
		components {list} -- list containing number of component for every vertex
	'''
	print('The number of components in this graph:', max(components))
	if max(components) > 13:
		print("WARNING: Components number exceeded a limit for coloring mode")
		draw_graph(G)
	else:
		#defining 13 colors for each component
		colors = ['blue', 'red', 'lime', 'yellow', 'cyan', 'orange',  
			'purple', 'green', 'pink', 'brown', 'magenta', 'gold', 'silver']
		node_colors = []
		for node in range(0, len(G)):
			number = components[node] - 1 #-1 cause components values start from 1
			node_colors.append(colors[number])
		draw_graph(G, node_colors)

def find_vertices_of_biggest_component(components: list):
	'''Function finding numbers of vertices of the biggest component in graph 
	defined by a components list

	Arguments:
		components {list} -- every element is a number of component for every node in graph G

	Returns:
		{list} -- vertices that are parts of the biggest component
	'''
	number_of_appearances = []
	unique = set(components)
	for i in unique:
		number_of_appearances.append(components.count(i))
	#choosing component that has max number of appearances
	idx = number_of_appearances.index(max(number_of_appearances))
	unique = list(unique) #set does not support indexing
	positions = []
	for i in range(len(components)):
		if components[i] == unique[idx]:
			positions.append(i)
	return [x+1 for x in positions]

########################################################################
 
# task 4 written by Tomasz Gajda

def is_consistent(deg_seq: list) -> bool:
    '''Function checking if the graph presented by degree sequence is consistent

	Arguments:
		deg_seq {list} -- degree sequence in form of a degree list

	Returns:
		{bool} -- boolean stating if the graph is consistent
	'''
    return len(list(filter(lambda x: x == 0, deg_seq))) == 0

def is_euler(deg_seq: list) -> bool:
    '''Function checking if the graph is Eulerian by chcecking if the degrees are even
    and the graph is consistent

	Arguments:
		deg_seq {list} -- degree sequence in form of a degree list

	Returns:
		{bool} -- boolean stating if the graph is Eulerian
	'''
    return is_consistent(deg_seq) and len(list(filter(lambda x: x > 0 and x % 2 == 1, deg_seq))) == 0

def generate_eulerian(n: int) -> list:
    '''Function generating Eulerian graph from requested number of vertices, 
    returns graph in form of an adjacency matrix

	Arguments:
		n {int} -- vertices count

	Returns:
		{list} -- adjacency matrix of generated Eulerian graph
	'''
    while True:
        deg_seq = [random.randint(1, n) for x in range(n)]
        if(isDegreeSequence(deg_seq) and is_euler(deg_seq)):
            return degSeq2adjMat(deg_seq).astype(int).tolist()


def euler_cycle(graph: list) -> list:
    '''Function finding Euler cycle using DFS 

	Arguments:
		graph {list} -- graph in form of an adjacency matrix

	Returns:
		{list} -- list presenting the Euler cycle by consecutive vertices
	'''
    cycle = []

    def euler_dfs(v):
        for u in range(len(graph)):
            if graph[v][u] > 0:
                graph[v][u] -= 1
                graph[u][v] -= 1
                euler_dfs(u)
        cycle.append(v)

    euler_dfs(0)

    return [x+1 for x in cycle]

########################################################################

#task 5 written by Piotr Matiaszewski 

def generateRandomizedKRegularGraph(L: list) -> list:
	'''Function generating random k-regular graphs from graph sequence given as a list L
	Arguments:
		L {list} -- graph sequence
	Returns:
		List -- adjacency representation of randomized graph
	'''
	if(isDegreeSequence(L)):
		G = degSeq2adjMat(L)
	else: 
		print("Number of vertices and degrees is invalid.")
		exit(-1)
	Adjacency_matrix = G
		
	return graph_randomization(Adjacency_matrix)

########################################################################
 
# task 6 written by Tomasz Gajda
 
def prepare_for_hamilton(file_name: str) -> tuple:
    '''Function preparing graph represantation for hamilton cycle recursive function
 
    Arguments:
        file_name {str} -- name of the file with graph representation
 
    Returns:
        graphs {tuple} -- tuple holding one graph with original 
        indexing and second prepared for the recursive algorithm
    '''
 
    graph_adj_mat = read_graph_file_return_Adjacency_matrix(file_name)
    graph = convert_Adjacency_matrix_into_Adjacency_list(graph_adj_mat)
 
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] -= 1
 
    return (graph, graph_adj_mat)
 
def hamilton_cycle(graph: list, v: int = 0, stack: list = None) -> list:
    '''Function finding Hamilton cycle of the graph (if it exists)
 
    Arguments:
        graph {list} -- adjacency matrix of a graph
        v {int} -- current vertex (0 by default)
        stack {list} -- list of vertices forming current cycle
 
    Returns:
        hamilton_cycle {list} -- list of vertices forming Hamiltonian cycle (if it exists)
    '''
 
    if stack is None:
        stack = []
    
    size = len(graph)
 
    if v not in set(stack):
        stack.append(v)
 
        if len(stack) == size:
            if stack[-1] in graph[stack[0]]:
                stack.append(stack[0])
                return [x+1 for x in stack]
            else:
                stack.pop()
                return None
 
        for v_n in graph[v]:
            stack_copy = stack[:]
            hamilton_result = hamilton_cycle(graph, v_n, stack_copy)
            if hamilton_result is not None:
                return hamilton_result
 
def draw_hamilton(g_am: list, cycle: list):
    """Function drawing a graph with the Hamilton cycle steps (if it exists)
    Arguments:
        g_am {list} -- adjacency matrix of a graph
        cycle {list} -- Hamiltonian cycle
    """
    g = nx.Graph()
    node_value = 1 
    labels = {}
    number_of_nodes = len(g_am)
    coordinates=[(np.sin(np.pi * 2 * i / number_of_nodes) * number_of_nodes, np.cos(np.pi * 2 * i / number_of_nodes) * number_of_nodes) for i in range(number_of_nodes)]
 
    for i in g_am:
        node_label = str(node_value) + "(" + str(cycle.index(node_value) + 1) +")"
        labels[node_value] = node_label
        g.add_node(node_value, pos = coordinates[node_value - 1])
        node_value += 1 
 
    for i in range(len(g_am)):
        for j in range(i + 1 , len(g_am)):
            if(g_am[i][j] == 1):
                g.add_edge(i + 1, j + 1)
 
    pos = nx.get_node_attributes(g,'pos')
    nx.draw(g, pos, node_size = 10000/len(pos), with_labels = False)
    nx.draw_networkx_labels(g, pos, labels)
    plt.axis('square')
    plt.show()
 
########################################################################
