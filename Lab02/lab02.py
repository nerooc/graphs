import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time #for task 2
import random #for task 2
from lab01 import draw_graph #for task 3
from lab01 import convert_Adjacency_matrix_into_Adjacency_list #for task 2
from lab01 import convert_Adjacency_list_into_Adjacency_matrix #for task 2

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

	NOTE: Function can draw up to 10 different components

	Arguments:
		G {numpy array} -- adjacency matrix of a graph
		components {list} -- list containing number of component for every vertex
	'''
	#defining 10 colors for each component
	colors = ['blue', 'red', 'green', 'yellow', 'cyan', 
		'orange', 'purple', 'pink', 'brown', 'gold']
	node_colors = []
	for node in range(0, len(G)):
		number = components[node] - 1 #-1 cause components values start from 1
		node_colors.append(colors[number])
	print('The number of components in this graph:', max(components))
	draw_graph(G, node_colors)

########################################################################

#task 5 written by Piotr Matiaszewski 

def generateRandomizedKRegularGraph(L):
	'''Function generating random k-regular graphs from graph sequence given as a list L

	Arguments:
		L {list} -- graph sequence

	Returns:
		List -- adjacency representation of randomized graph
	'''
    if(isDegreeSequence(L.copy())):
        G = degSeq2adjMat(L.copy())
        np.savetxt("task1.txt", G, delimiter=" ", newline = "\n", fmt="%d")
    else: 
        print("Number of vertices and degrees is invalid.")
        exit(-1)
    with open('task1.txt', 'r') as f:
        Adjacency_matrix = [[int(num) for num in line.split()] for line in f]
    return graph_randomization(Adjacency_matrix)
