# -*- coding: utf-8-*-

'''
Grafy i ich zastosowania
Projekt 2, zadanie 3
Script by Bartosz Rogowski
'''

import numpy as np
from lab02 import *

if __name__ == '__main__':
	l = input('Please give an input sequence (numbers splitted by space, for example: 4 3 2 1):\n')
	try:
		l = [int(elem) for elem in l.split(' ')]
	except(ValueError):
		print('Given sequence must contain only numbers that are integers')
		exit(-1)
	if(isDegreeSequence(l)):
		G = degSeq2adjMat(l)
		components = COMPONENTS(G)
		#counting number of appearances of every component
		vrtx = find_vertices_of_biggest_component(components)
		print('The biggest component consists of vertices:', str(vrtx)[1:-1])
		#drawing graph
		drawGraph(G, components)
	else:
		print('Given sequence IS NOT a degree sequence')