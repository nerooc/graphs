import random
import time
import sys
from pandas import *
from lab01 import read_graph_file_return_Adjacency_matrix
from lab01 import generate_graph_b
from lab01 import draw_graph
from lab02 import *



# main
if __name__ == "__main__":
    # # some tests
    # prop = [0.01, 0.2, 0.4, 0.6, 0.8, 0.99]
    # ver = [20, 100, 300, 500]
    # arrTime = [[0 for i in range(len(prop))] for row in range(len(ver))]
    # print("Some tests...")
    # for i in range(len(prop)):
    #     for j in range(len(ver)):
    #         Adjacency_matrix = generate_graph_b(ver[j], prop[i])
    #         start = time.time()
    #         Adjacency_matrix2 = graph_randomization(Adjacency_matrix)
    #         end = time.time()
    #         arrTime[j][i] = end - start
    #
    # print(DataFrame(arrTime))
    # print()


    print("This is graph randomization. Path to graph data file should be typed in input args")
    file_name = 'InputFiles/input.txt'
    if len(sys.argv) == 1:
        print("No input in program args, trying to open file \'InputFiles/input.txt\'...\n")
    else:
        file_name = sys.argv[1]  # path to file with graph data

    Adjacency_matrix = read_graph_file_return_Adjacency_matrix(file_name)
    draw_two_graphs(Adjacency_matrix, graph_randomization(Adjacency_matrix),
                    'before randomization:', 'after randomization:')
