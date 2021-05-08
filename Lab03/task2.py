"""
Grafy i ich zastosowania
Projekt 3, zadanie 2
Script by Tomasz Gajda
"""

import sys
from lab03 import dijkstra, print_dijkstra

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        raise Exception("Run as: task2.py [v_start]")

    #graph will be generated after task 1 will be finished :)

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
        path_costs, predecessors = dijkstra(graph, 1)
        print_dijkstra(path_costs, predecessors, 1)
        print("\nTEST #2 - Test for last vertex of the graph:\n")
        path_costs, predecessors = dijkstra(graph, 1)
        print_dijkstra(path_costs, predecessors, 1)
        sys.exit("End of testing")
    #TESTING###########################################################################
    
    v_start = int(sys.argv[1])

    

    path_costs, predecessors = dijkstra(graph, v_start)
    print_dijkstra(path_costs, predecessors, v_start)

