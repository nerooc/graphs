# -*- coding: utf-8-*-


'''
Grafy i ich zastosowania
Projekt 1, zadanie 3ab
Script by Bartosz Rogowski
'''

import numpy as np
from lab01 import is_integer_num, generate_graph

if __name__ == '__main__':

	number_of_vertices = input("Enter number of vertices: ")
	second_arg = input("Enter number of edges or probability that an edge exists between two vertices: ")
	try:
		G = generate_graph(int(number_of_vertices), float(second_arg))
	except ValueError:
		print("Wrong arguments")
		exit(-1)
	#save G to file
	np.savetxt("InputFiles/task3.txt", G, delimiter=" ", newline = "\n", fmt="%d")
	print("Output file has been saved to: 'task3.txt'")