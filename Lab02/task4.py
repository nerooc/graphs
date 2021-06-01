"""
Grafy i ich zastosowania
Projekt 2, zadanie 4
Script by Tomasz Gajda
"""

import sys
import argparse
import copy as cp

from lab01 import convert_Adjacency_matrix_into_Adjacency_list, draw_graph
from lab02 import generate_eulerian, euler_cycle_dfs, euler_cycle_fleury

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Finding Euler cycle in random Euler Graph (by default with DFS).')
    parser.add_argument('-f', action='store_true', help='using different algorithm (Fleury)')
    parser.add_argument('number_of_vertices', metavar='number_of_vertices/test', help='amount of vertices in the graph/turn on testing')

    args = parser.parse_args()
    if args.f:
        print("Using Fleury's algorithm!")
        euler_cycle = euler_cycle_fleury
    else:
        print("Using DFS algorithm!")
        euler_cycle = euler_cycle_dfs

    n = args.number_of_vertices

    #TESTING###########################################################################
    if(n == "test"):
        print("\nTEST #1 - Test for minimal amount of vertices [DFS] (3):")
        graph_adj_mat = generate_eulerian(3)
        graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)
        result_cycle = euler_cycle_dfs(graph_adj_mat_cp)
        print(result_cycle)
        draw_graph(graph_adj_mat)

        print("\nTEST #2 - Test for maximal amount of vertices [DFS] (16):")
        graph_adj_mat = generate_eulerian(60)
        graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)
        result_cycle = euler_cycle_dfs(graph_adj_mat_cp)
        print(result_cycle)
        draw_graph(graph_adj_mat)

        print("\nTEST #3 - Test for a hardcoded matrix [DFS]:")
        graph_adj_mat = [[0, 1, 1, 1, 1, 0, 1, 1],
                        [1, 0, 1, 1, 1, 1, 0, 1],
                        [1, 1, 0, 1, 0, 1, 0, 0],
                        [1, 1, 1, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0]]
        graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)
        result_cycle = euler_cycle_dfs(graph_adj_mat_cp)
        print(result_cycle)
        draw_graph(graph_adj_mat)
        sys.exit("End of testing")
    #TESTING###########################################################################

    n = int(n)

    if n < 3 or n > 60:
        raise Exception("Invalid number of vertices! Correct number is in the range 3 <= n <= 60")

    graph = generate_eulerian(n)
    graph_cp = cp.deepcopy(graph)

    if(args.f):
        graph_cp = convert_Adjacency_matrix_into_Adjacency_list(graph_cp)

    result_cycle = euler_cycle(graph_cp)
    print(result_cycle)
    draw_graph(graph)
