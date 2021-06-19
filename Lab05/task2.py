import sys
from lab04 import read_matrix_from_file
from lab05 import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
            raise Exception("Run as: task2.py <path-to-file> or task2.py test")

    #TESTING###########################################################################
    if(sys.argv[1] == "test"):
        test_graph = [
            [0, 10, 3, 6, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 8, 0, 8, 6, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 10, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 8, 1, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        print("\nTEST #1 - Test for hardcoded matrix from the exemplary input file:\n")
        result, residual_network = ford_fulkerson(test_graph, 0, 10)
        print("Max flow of the given network: " + str(result))
        display_result_max_flow(test_graph, residual_network)
        sys.exit("\nEnd of testing")
    #TESTING###########################################################################

    file_name = sys.argv[1]
    digraph = read_matrix_from_file(file_name)
    for r_i, r in enumerate(digraph):
        for c_i, c in enumerate(r):
            digraph[r_i][c_i] = int(digraph[r_i][c_i])
    digraph2 = np.array(digraph)
    pretty_print(digraph)
    print()
    result, residual_network = ford_fulkerson(digraph, 0, len(digraph) - 1)
    print("Max flow of the given network: " + str(result))
    display_result_max_flow(digraph2, residual_network)
    
