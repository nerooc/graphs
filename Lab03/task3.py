"""
Grafy i ich zastosowania
Projekt 3, zadanie 3
Script by Tomasz Gajda
"""

import sys
from lab03 import generate_random_graph, add_int_weights, distance_matrix

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        raise Exception("Run as: task3.py [max-vertex-num]")

    #TESTING###########################################################################
    if(sys.argv[1] == "test"):
        print("\nTEST #1 - Test for 5 vertices:\n")
        test_graph1 = generate_random_graph(5)
        test_graph1 = add_int_weights(test_graph1)
        for row in distance_matrix(test_graph1):
            print(row)

        print("\nTEST #2 - Test for 30 vertices:\n")
        test_graph2 = generate_random_graph(30)
        test_graph2 = add_int_weights(test_graph2)
        for row in distance_matrix(test_graph2):
            print(row)

        sys.exit("End of testing")
    #TESTING###########################################################################

    max_vertex_num = int(sys.argv[1])

    graph = generate_random_graph(max_vertex_num)
    graph = add_int_weights(graph)

    for row in distance_matrix(graph):
        print(row)
