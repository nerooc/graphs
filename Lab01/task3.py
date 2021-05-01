# -*- coding: utf-8-*-


'''
Grafy i ich zastosowania
Projekt 1, zadanie 3ab
Script by Bartosz Rogowski
'''

import numpy as np
from lab01 import generate_graph_a, generate_graph_b

if __name__ == '__main__':
	mode = input("Please type mode: \n- 'a' if second argument will be number of edges\n- 'b' - if probability\n")
	if mode == 'a':
		number_of_vertices = input("Enter number of vertices: ")
		number_of_edges = input("Enter number of edges: ")
		try:
			G = generate_graph_a(int(number_of_vertices), int(number_of_edges))
		except ValueError:
			print("Wrong arguments")
			exit(-1)
	elif mode == 'b':
		number_of_vertices = input("Enter number of vertices: ")
		probability = input("Enter probability that an edge exists between two vertices: ")
		try:
			G = generate_graph_b(int(number_of_vertices), float(probability))
		except ValueError:
			print("Wrong arguments")
			exit(-1)
	else:
		print("Incorrect mode, please try again.")
		exit(-1)
	
	#save G to file
	np.savetxt("InputFiles/task3.txt", G, delimiter=" ", newline = "\n", fmt="%d")
	print("Output file has been saved to: 'InputFiles/task3.txt'")
