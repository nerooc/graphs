import sys
import numpy as np
from lab01 import draw_graph
from lab02 import draw_two_graphs, pretty_print
from lab03 import generate_random_graph, add_int_weights, visualizeMST

if __name__ == "__main__":
    print("This program generates random complement graph. In input args set max vertices number.")
    max_vertices_num = 9
    if len(sys.argv) == 1:
        print("No input in program args, max_vertices_num = 9")
    else:
        max_vertices_num = int(sys.argv[1])
    adjacency_matrix1 = generate_random_graph(max_vertices_num)
    adjacency_matrix_with_weights = add_int_weights(adjacency_matrix1)
    if len(adjacency_matrix1) == 1:
        draw_graph(adjacency_matrix1)
    else:
        visualizeMST(np.array(adjacency_matrix_with_weights), [0])
    with open("graph.txt", "w") as f:
        if len(adjacency_matrix1) == 1:
            f.write(str(adjacency_matrix1[0]))
        else:
            for row in adjacency_matrix1:
                for col in row:
                    f.write(str(col)+" ")
                f.write("\n")
        f.close()
    print("graph1 weights: ")
    if len(adjacency_matrix1) == 1:
        print(adjacency_matrix1[0])
    else:
        pretty_print(adjacency_matrix_with_weights)
