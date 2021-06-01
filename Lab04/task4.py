"""
Grafy i ich zastosowania
Projekt 4, zadanie 4
Script by Tomasz Gajda
"""

import sys
import argparse
import copy as cp

from lab04 import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Using Johnson\'s algorithm to find the distance matrix of a graph')
    parser.add_argument('-f', action='store_true', help='load graph from external file')
    parser.add_argument('number_of_vertices', metavar='number_of_vertices/file_name/test', help='amount of vertices in the graph/name of the file containing graph/turn on testing')

    args = parser.parse_args()
    
    n = args.number_of_vertices

    #TESTING###########################################################################
    if(n == "test"):
        print("\nTEST #1 - Test for hardcoded graph:\n")
        graph = [['.', '.', 3, '.', 1], [1, '.', 1, -1, 1], [1, 0, '.', '.', -1], ['.', '.', '.', '.', '.'], ['.', 1, '.', 1, '.']]
        pretty_print_w_inf(graph)
        graph_cp = cp.deepcopy(graph)
        print("\nDistance matrix:\n")
        pretty_print_w_inf(johnson(graph))
        generate_graph_from_adjacency_matrix(graph_cp)

        sys.exit("End of testing")
    #TESTING###########################################################################

    if args.f:
        print("Using graph from file!")
        digraph = read_matrix_from_file(n)

        for r_i, r in enumerate(digraph):
            for c_i, c in enumerate(r):
                if c != '.':
                    digraph[r_i][c_i] = int(digraph[r_i][c_i])

        digraph_cp = cp.deepcopy(digraph)

        pretty_print_w_inf(digraph)
        print()
        pretty_print_w_inf(johnson(digraph))

        generate_graph_from_adjacency_matrix(digraph_cp)
    else:
        print("Generating a graph")
        max_vertices_num = int(n)

        digraph = generate_real_random_complement_digraph(max_vertices_num)
        
        if not isinstance(digraph, list):
            digraph = digraph.tolist()

        digraph_cp = cp.deepcopy(digraph)
        digraph = swap_zero_to_dot(digraph)

        add_weights_digraph(digraph, -5, 10)


        pretty_print_w_inf(digraph)
        print()
        pretty_print_w_inf(johnson(digraph))

        generate_graph_from_adjacency_matrix(digraph_cp)



