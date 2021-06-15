from lab03 import kruskal, visualizeMST
import numpy as np
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
			matrix = np.loadtxt(file_name, delimiter=" ")
			matrix = np.array(matrix)
		except ValueError:
			print(f"{file_name} contains incorrect data (probaly not separated by spaces)")
			exit(-1)
	else:
		print(f"Sorry, there is no file named {file_name}.")
		exit(-1)
	
	weighted_edges = kruskal(matrix)
	print("Sum of MST weights:", sum(weight[1] for weight in weighted_edges))
	visualizeMST(matrix, weighted_edges)