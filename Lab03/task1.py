import sys
from lab02 import draw_two_graphs
from lab03 import generate_random_graph, add_int_weights

if __name__ == "__main__":
    print("This program generates random complement graph. In input args set max vertices number.")
    max_vertices_num = 9
    if len(sys.argv) == 1:
        print("No input in program args, max_vertices_num = 9")
    else:
        max_vertices_num = sys.argv[1]  # path to file with graph data
    # max_vertices_num = 4
    adjacency_matrix1 = generate_random_graph(max_vertices_num)
    draw_two_graphs(adjacency_matrix1, generate_random_graph(max_vertices_num))
    adjacency_matrix_with_weights = add_int_weights(adjacency_matrix1)
    print("graph1 weights: ", adjacency_matrix_with_weights)
