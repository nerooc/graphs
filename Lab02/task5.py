from task_b import degSeq2adjMat
from task_b import isDegreeSequence
from task_karol.task2 import graphRandomization
from task_karol.conversions import read_graph_file_return_Adjacency_matrix
from task_karol.draw import draw_graph
import numpy as np


def generateRandomizedKRegularGraph(L):
    """ Function generating random k-regular graphs from graph sequence given as a list L"""
    if(isDegreeSequence(L.copy())):
        G = degSeq2adjMat(L.copy())
        np.savetxt("task1.txt", G, delimiter=" ", newline = "\n", fmt="%d")
    else: 
        print("Number of vertices and degrees is invalid.")
        exit(-1)
    with open('task1.txt', 'r') as f:
        Adjacency_matrix = [[int(num) for num in line.split()] for line in f]
    return graphRandomization(Adjacency_matrix)
            
if __name__ == "__main__":
    print("Enter the amount of vertices and their degree (two integer numbers)")
    input_string=input()
    input_list=input_string.split()
    if len(input_list)!=2:
        print("Invalid number of arguments")
    else:
        try:
            number_of_vertices,degree_of_vertices=int(input_list[0]),int(input_list[1])
        except:
            print("Invalid input form")
        graph_sequence=[degree_of_vertices for i in range(number_of_vertices)]#here we dont know yet if this graph sequence is valid 
    randomized_graph=generateRandomizedKRegularGraph(graph_sequence)
    draw_graph(randomized_graph)
