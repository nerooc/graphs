# -*- coding: utf-8-*-


'''
Grafy i ich zastosowania
Projekt 4, zadanie 2
Script by Bartosz Rogowski
'''

import numpy as np
from lab04 import kosaraju, drawDigraph

if __name__ == '__main__':
	try:
		file_name = input("Please type file name:\n")
		G = np.loadtxt(file_name, delimiter=" ")
	except OSError:
		print(f"{file_name} has not been found")
		exit(-1)
	except ValueError:
		print(f"{file_name} contains incorrect data (probaly not separated by spaces)")
		exit(-1)
	comp = kosaraju(G)
	drawDigraph(G, comp)