import sys
from lab02 import draw_graph
from lab03 import generate_random_graph
from lab03 import add_weights

if __name__ == "__main__":
    print("This program generates random coherent graph. In input args set max vertices number.")
    max_vertices_num = 9
    if len(sys.argv) == 1:
        print("No input in program args, max_vertices_num = 9")
    else:
        max_vertices_num = sys.argv[1]  # path to file with graph data
    adjacency_matrix1 = generate_random_graph(max_vertices_num)
    draw_graph(adjacency_matrix1)
    adjacency_matrix1 = add_weights(adjacency_matrix1)
    print(adjacency_matrix1)
