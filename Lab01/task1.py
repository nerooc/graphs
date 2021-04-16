import os
from lab01 import *

if __name__ == "__main__":
	print("Welcome to graph reader.\nType the name of your input file:")
	file_name=input()
	data_matrix, chosen_option = read_graph_file_return_Adjacency_matrix(file_name,True)

	if chosen_option == "a":
		# input was Adjacency matrix
		print()
		adj_list = convert_Adjacency_matrix_into_Adjacency_list(data_matrix)
		print("Adjacency matrix -> Adjacency list:")
		for i in range(len(adj_list)):
			print(i+1,end=". ")
			for j in range(len(adj_list[i])):
				print(adj_list[i][j],end=" ")
			print()

		print()
		print("Adjacency matrix -> Incidence matrix:")
		incidence_matrix = convert_Adjacency_matrix_into_Incidence_matrix(data_matrix)
		print(*incidence_matrix, sep="\n")
 
		#######################################

	elif chosen_option == "b":
		# input was Adjacency list
		adjacency_matrix = convert_Adjacency_list_into_Adjacency_matrix(data_matrix)
		print()
		print("Adjacency list -> Adjacency matrix:")
		print(*adjacency_matrix,sep="\n")

		incidence_matrix = convert_Adjacency_list_into_Incidence_matrix(data_matrix)
		print()
		print("Adjacency list -> Incidence matrix:")
		print(*incidence_matrix,sep="\n")

		#######################################

	elif chosen_option == "c":	
		# input was Incidence matrix
		adjacency_matrix = convert_Incidence_matrix_into_Adjacency_matrix(data_matrix)
		print("Incidence matrix -> Adjacency matrix:")
		print(*adjacency_matrix, sep="\n")

		adj_list = convert_Incidence_matrix_into_Adjacency_list(data_matrix)
		print()
		print("Incidence matrix -> Adjacency list:")
		for i in range(len(adj_list)):
			print(i+1,end=". ")
			for j in range(len(adj_list[i])):
				print(adj_list[i][j],end=" ")
			print()