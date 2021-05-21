"""
Grafy i ich zastosowania
Projekt 3, zadanie 3
Script by Tomasz Gajda
"""

import sys
from lab03 import generate_random_graph, add_int_weights, distance_matrix, read_graph, pretty_print

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        raise Exception("Run as: task3.py InputFiles/[file-name]")

    #TESTING###########################################################################
    if(sys.argv[1] == "test"):
        print("\nTEST #1 - Test for < 5 vertices:\n")
        test_graph1 = generate_random_graph(5)
        test_graph1 = add_int_weights(test_graph1)
        pretty_print(distance_matrix(test_graph1))

        print("\nTEST #2 - Test for < 30 vertices:\n")
        test_graph2 = generate_random_graph(30)
        test_graph2 = add_int_weights(test_graph2)
        pretty_print(distance_matrix(test_graph2))

        sys.exit("End of testing")
    #TESTING###########################################################################

    file_name = sys.argv[1]
    graph = read_graph(file_name)

    pretty_print(distance_matrix(graph))
