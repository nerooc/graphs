# -*- coding: utf-8-*-

'''
Grafy i ich zastosowania
Projekt 2, zadanie 1
Script by Bartosz Rogowski
'''

from lab02 import *

if __name__ == '__main__':
	l = input('Please give an input sequence (numbers splitted by space, for example: 4 3 2 1):\n')
	try:
		l = [int(elem) for elem in l.split(' ')]
	except(ValueError):
		print('Given sequence must contain only numbers that are integers')
		exit(-1)
	if(isDegreeSequence(l)):
		print('Given sequence IS a degree sequence')
		G = degSeq2adjMat(l)
		print("Adjacency matrix:")
		try:
			pretty_print(G)
		except Exception as e:
			print(e)
	else:
		print('Given sequence IS NOT a degree sequence')
