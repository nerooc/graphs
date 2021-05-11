"""
Grafy i ich zastosowania
Projekt 2, zadanie 4
Script by Tomasz Gajda
"""

import sys
import copy as cp

from lab01 import draw_graph
from lab02 import isDegreeSequence, degSeq2adjMat, generate_eulerian, euler_cycle

if __name__ == "__main__":
    # TWO ARGUMENTS ARE REQUIRED
    if len(sys.argv) != 2:
        raise Exception("Run as: task4.py [number_of_vertices]")

    #TESTING###########################################################################
    if(sys.argv[1] == "test"):
        print("\nTEST #1 - Test for minimal amount of vertices (3):")
        graph_adj_mat = generate_eulerian(3)
        graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)
        result_cycle = euler_cycle(graph_adj_mat_cp)
        print(result_cycle)
        draw_graph(graph_adj_mat)

        print("\nTEST #2 - Test for maximal amount of vertices (16):")
        graph_adj_mat = generate_eulerian(60)
        graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)
        result_cycle = euler_cycle(graph_adj_mat_cp)
        print(result_cycle)
        draw_graph(graph_adj_mat)

        print("\nTEST #3 - Test for a hardcoded matrix:")
        graph_adj_mat = [[0, 1, 1, 1, 1, 0, 1, 1],
                        [1, 0, 1, 1, 1, 1, 0, 1],
                        [1, 1, 0, 1, 0, 1, 0, 0],
                        [1, 1, 1, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0]]
        graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)
        result_cycle = euler_cycle(graph_adj_mat_cp)
        print(result_cycle)
        draw_graph(graph_adj_mat)
        sys.exit("End of testing")
    #TESTING###########################################################################

    n = int(sys.argv[1])

    if n < 3 or n > 60:
        raise Exception("Invalid number of vertices! Correct number is in the range 3 <= n <= 60")

    graph_adj_mat = generate_eulerian(n)
    graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)

    result_cycle = euler_cycle(graph_adj_mat_cp)
    print(result_cycle)
    draw_graph(graph_adj_mat)
