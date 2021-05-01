import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

from lab01 import *

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You did not specify the location of input file')
    sys.exit()

if __name__ == "__main__":
    file_name=sys.argv[1]
    if(os.path.isfile(file_name)):
        data_matrix=read_graph_file_return_Adjacency_matrix(file_name) #using the function from task 1
        graph=draw_nodes(data_matrix)
        graph=draw_edges_from_adjacency_matrix(graph,data_matrix)
        display_graph(graph)
    else:
        print("Sorry, there is no file named "+file_name+".")
