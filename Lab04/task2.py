# -*- coding: utf-8-*-


'''
Grafy i ich zastosowania
Projekt 4, zadanie 2
Script by Bartosz Rogowski
'''

import numpy as np
from lab04 import kosaraju, drawDigraph
import os
import sys

if len(sys.argv) > 2:
	print('You have specified too many arguments')
	sys.exit()

if len(sys.argv) < 2:
	print('You did not specify the location of input file')
	sys.exit()

if __name__ == '__main__':
	file_name=sys.argv[1]
	if(os.path.isfile(file_name)):
		if(os.path.getsize(file_name) == 0):
			print(f"Sorry, file named {file_name} is empty.")
			exit(-1)
		try:
			G = np.loadtxt(file_name, delimiter=" ")
			comp = kosaraju(G)
			drawDigraph(G, comp)
		except ValueError:
			print(f"{file_name} contains incorrect data (probaly not separated by spaces)")
			exit(-1)
		except Exception as e:
			print(e)
			exit(-1)
	else:
		print(f"Sorry, there is no file named {file_name}.")
		exit(-1)

	