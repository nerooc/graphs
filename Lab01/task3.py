# -*- coding: utf-8-*-


'''
Grafy i ich zastosowania
Projekt 1, zadanie 3ab
Script by Bartosz Rogowski
'''

import numpy as np
import argparse
from lab01 import generate_graph_a, generate_graph_b

def parserFunction():
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('-v', '--vertices', type=int, help=u'''Number of vertices''', required=True)
	parser.add_argument('-e', '--edges', type=int, help=u'''Number of edges''')
	parser.add_argument('-p', '--probability', type=float, help=u'''Probability that an edge exists between two vertices''')

	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parserFunction()

	if args.edges == None and args.probability == None:
		print("No second argument provided")
		exit(-1)
	if args.edges != None:
		try:
			G = generate_graph_a(args.vertices, args.edges)
		except ValueError:
			print("Wrong arguments")
			exit(-1)
		except Exception as e:
			print(e)
			exit(-1)
	elif args.probability != None:
		try:
			G = generate_graph_b(args.vertices, args.probability)
		except ValueError:
			print("Wrong arguments")
			exit(-1)
		except Exception as e:
			print(e)
			exit(-1)
	else:
		print("Incorrect mode, please try again.")
		exit(-1)
	
	#save G to file
	np.savetxt("InputFiles/task3.txt", G, delimiter=" ", newline = "\n", fmt="%d")
	print("Output file has been saved to: 'InputFiles/task3.txt'")