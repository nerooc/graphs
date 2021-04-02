# -*- coding: utf-8-*-


'''
Grafy i ich zastosowania
Projekt 1, zadanie 3ab
Script by Bartosz Rogowski
'''

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

description='''This script generates random graphs based on given arguments:
	* number of vertices
	* second argument
		- number of edges (case a)
		- probability that an edge exists between two vertices (case b)

Depending on the second argument, script returns graph represented by:
case a) incidence matrix 
case b) adjacency matrix
'''


def is_integer_num(obj):
	'''Function checking if the given argument is an integer

	Arguments:
		obj {any} -- argument that will be checked
		arg2 {integer or float} --  number of edges or probability that an edge exists between two vertices

	Returns:
		bool -- information whether given argument is an integer
	'''
	if isinstance(obj, int):
		return True
	elif isinstance(obj, float):
		return obj.is_integer()
	else:
		print("Argument is neither integer nor float")
		exit(-1)

def generate_graph(n: int, arg2):
	'''Function generating graph

	Arguments:
		n {integer} -- number of vertices
		arg2 {integer or float} --  number of edges or probability that an edge exists between two vertices

	Returns:
		numpy array -- matrix representing graph
	'''

	if(is_integer_num(arg2) and arg2 > 0):
		l = int(arg2)
		if(l > n*(n-1)/2):
			print("Number of edges is too big")
			exit(-1)
		G = np.zeros((n, l))
		pairing_set = set() #contains pairs of vertices between which edge already exists
		for edge in range(0, l):
			try:
				#random.sample generates 2 unique values of given range
				vertex = tuple(random.sample(range(0, n), 2))
				#edge must be singular (simple graph) therefore we need to check whether it already exists or not 
				if vertex not in pairing_set:
					#adding pairs for example: (1, 4) and (4, 1) since both are the same edge
					pairing_set.add(vertex)
					pairing_set.add(vertex[::-1])
				else:
					while vertex in pairing_set:
						vertex = tuple(random.sample(range(0, n), 2))
					pairing_set.add(vertex)
					pairing_set.add(vertex[::-1])
			except ValueError:
				print("Number of vertices is too small")
				exit(-1)
			for i in range(0, 2):
				G[vertex[i], edge] += 1

	elif(arg2 >= 0 and arg2 < 1):
		p = arg2
		G = np.zeros((n, n))
		for a in range(0, n-1):
			for b in range(0, n-1-a):
				if random.random() <= p:
					G[a, a+b+1] = 1
				else:
					G[a, a+b+1] = 0
		for a in range(0, n):
			for b in range(a, n):
				G[b, a] = G[a, b]
		
		count = 0
		for a in range(0, n):
			for b in range(0, n):
				if G[a, b] == 1:
					count += 1
		print(f"{100*count/(n**2)}%")

	else:
		print("Second argument is not valid")
		exit(-1)
	return G


if __name__ == '__main__':

	number_of_vertices = input("Enter number of vertices: ")
	second_arg = input("Enter number of edges or probability that an edge exists between two vertices: ")
	try:
		G = generate_graph(int(number_of_vertices), float(second_arg))
	except ValueError:
		print("Wrong arguments")
		exit(-1)
	#save G to file
	np.savetxt("task3.txt", G, delimiter=" ", newline = "\n", fmt="%d")
	print("Output file has been saved to: 'task3.txt'")