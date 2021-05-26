"""
Grafy i ich zastosowania
Projekt 4, zadanie 4
Script by Tomasz Gajda
"""

import sys
import copy as cp
from lab04 import *

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        raise Exception("Run as: task4.py [max_vertices_num]")

    #TESTING###########################################################################
    if(sys.argv[1] == "test"):
        print("\nTEST #1 - Test for hardcoded graph:\n")
        graph = [[0, 0, 3, 0, 1], [1, 0, 1, -1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0]]
        graph_cp = cp.deepcopy(graph)
        pretty_print_w_inf(johnson(graph))
        generate_graph_from_adjacency_matrix(graph_cp)

        sys.exit("End of testing")
    #TESTING###########################################################################
    
    max_vertices_num = int(sys.argv[1])

    digraph = generate_real_random_complement_digraph(max_vertices_num)
    digraph_cp = cp.deepcopy(digraph)
    digraph = swap_zero_to_n(digraph)

    add_weights_digraph(digraph, -5, 10)

    pretty_print_w_inf(digraph)
    print()
    pretty_print_w_inf(johnson(digraph))

    generate_graph_from_adjacency_matrix(digraph_cp)


