"""
Grafy i ich zastosowania
Projekt 3, zadanie 2
Script by Tomasz Gajda
"""

import sys
import copy as cp

from lab01 import draw_graph_with_weights
from lab03 import dijkstra, print_dijkstra, generate_random_graph, add_int_weights, read_graph
from random import randrange

if __name__ == "__main__": 

    #TESTING###########################################################################
    if(sys.argv[1] == "test"):
        graph = [[0,  3,  0,  2,  0,  0,  0,  0,  4],   
            [3,  0,  0,  0,  0,  0,  0,  4,  0],
            [0,  0,  0,  6,  0,  1,  0,  2,  0],
            [2,  0,  6,  0,  1,  0,  0,  0,  0],
            [0,  0,  0,  1,  0,  0,  0,  0,  8],
            [0,  0,  1,  0,  0,  0,  8,  0,  0],
            [0,  0,  0,  0,  0,  8,  0,  0,  0],
            [0,  4,  2,  0,  0,  0,  0,  0,  0],
            [4,  0,  0,  0,  8,  0,  0,  0,  0]]

        print("\nTEST #1 - Test for first vertex of the graph:\n")
        path_costs, predecessors = dijkstra(graph, 0)
        print_dijkstra(path_costs, predecessors, 0)
        print("\nTEST #2 - Test for last vertex of the graph:\n")
        path_costs, predecessors = dijkstra(graph, 8)
        print_dijkstra(path_costs, predecessors, 8)
        sys.exit("End of testing")
    #TESTING###########################################################################

    if len(sys.argv) != 3:
        raise Exception("Run as: task2.py InputFiles/[file-name] [start-vertex]")

    try: 
        start_vertex = int(sys.argv[2])
    except ValueError:
        print("[start-vertex] has to be an integer!")

    file_name = sys.argv[1]

    graph = read_graph(file_name)
    
    path_costs, predecessors = dijkstra(graph, start_vertex)
    print_dijkstra(path_costs, predecessors, start_vertex)
    draw_graph_with_weights(graph)
