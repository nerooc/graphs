"""
Grafy i ich zastosowania
Projekt 3, zadanie 2
Script by Tomasz Gajda
"""

import sys
import copy as cp

from lab02 import draw_graph
from lab03 import dijkstra, print_dijkstra, generate_random_graph, add_int_weights
from random import randrange

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        raise Exception("Run as: task2.py [v_start]")

    graph = [[0,  3,  0,  2,  0,  0,  0,  0,  4],   
            [3,  0,  0,  0,  0,  0,  0,  4,  0],
            [0,  0,  0,  6,  0,  1,  0,  2,  0],
            [2,  0,  6,  0,  1,  0,  0,  0,  0],
            [0,  0,  0,  1,  0,  0,  0,  0,  8],
            [0,  0,  1,  0,  0,  0,  8,  0,  0],
            [0,  0,  0,  0,  0,  8,  0,  0,  0],
            [0,  4,  2,  0,  0,  0,  0,  0,  0],
            [4,  0,  0,  0,  8,  0,  0,  0,  0]]

    #TESTING###########################################################################
    #tests will be updated with task 1 finished
    if(sys.argv[1] == "test"):
        print("\nTEST #1 - Test for first vertex of the graph:\n")
        path_costs, predecessors = dijkstra(graph, 0)
        print_dijkstra(path_costs, predecessors, 0)
        print("\nTEST #2 - Test for last vertex of the graph:\n")
        path_costs, predecessors = dijkstra(graph, 8)
        print_dijkstra(path_costs, predecessors, 8)
        sys.exit("End of testing")
    #TESTING###########################################################################

    v_start = int(sys.argv[1])
    min_vertices = v_start

    #if we are looking for a path for the first vertex, let's give it a chance to generate a bigger graph
    if min_vertices < 6:
        min_vertices = 6 

    #graph generation
    graph = generate_random_graph(min_vertices)

    while len(graph) < v_start + 1:
        graph = generate_random_graph(min_vertices + 5)

    weightless_graph = cp.deepcopy(graph)
    graph = add_int_weights(graph)
    print(graph)

    path_costs, predecessors = dijkstra(graph, v_start)
    print_dijkstra(path_costs, predecessors, v_start)
    draw_graph(weightless_graph)
