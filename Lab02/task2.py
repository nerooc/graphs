import random
import time
from pandas import *
from lab01 import read_graph_file_return_Adjacency_matrix
from lab01 import generate_graph
from lab01 import draw_graph

if __name__ == "__main__":
    # # some tests
    # prop = [0.01, 0.2, 0.4, 0.6, 0.8, 0.99]
    # ver = [20, 100, 300, 500]
    # arrTime = [[0 for i in range(len(prop))] for row in range(len(ver))]
    # print("start!")
    # for i in range(len(prop)):
    #     for j in range(len(ver)):
    #         Adjacency_matrix = generate_graph(ver[j], prop[i])
    #         start = time.time()
    #         Adjacency_matrix2 = graph_randomization(Adjacency_matrix)
    #         end = time.time()
    #         arrTime[j][i] = end - start
    #
    # print(DataFrame(arrTime))

    print("This is graph randomization.\nType the name of your graph representation file:")
    file_name = input()
    Adjacency_matrix = read_graph_file_return_Adjacency_matrix(file_name)
    print("Before randomization... (to see effect close first image)")
    draw_graph(Adjacency_matrix)
    print("After randomization")
    draw_graph(graph_randomization(Adjacency_matrix))
