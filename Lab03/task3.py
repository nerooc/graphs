"""
Grafy i ich zastosowania
Projekt 3, zadanie 3
Script by Tomasz Gajda
"""

import sys
from lab03 import generate_random_graph, add_int_weights, distance_matrix

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        raise Exception("Run as: task3.py [max_vertex_num]")

    max_vertex_num = int(sys.argv[1])

    graph = generate_random_graph(max_vertex_num)
    graph = add_int_weights(graph)

    for row in distance_matrix(graph):
        print(row)
