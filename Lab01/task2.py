import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from lab01 import *

if __name__ == "__main__":
    file_name=get_info_from_user()
    data_matrix=read_graph_file_return_Adjacency_matrix(file_name) #using the function from task 1
    graph=draw_nodes(data_matrix)
    graph=draw_edges_from_adjacency_matrix(graph,data_matrix)
    display_graph(graph)
