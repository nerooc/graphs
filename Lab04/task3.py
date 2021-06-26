from lab04 import generate_real_random_complement_digraph, add_weights_digraph, drawDigraph, kosaraju, bellman_ford, read_matrix_from_file, conv_str_to_0_1, pretty_print_w_inf
import sys

if __name__ == '__main__':
    print("This program generates random coherent digraph.\nIn input args set [max vertices number and source vertex for bellman_ford], [file with graph] or nothing")
    max_vertices_num = 7
    source_vertex = 0
    digraph = []
    if len(sys.argv) == 2:
        digraph = read_matrix_from_file(sys.argv[1])
        source_vertex = int(input("Choose source vertex to Bellman-Ford (first vertex is 0): "))
    else:
        if len(sys.argv) == 3:
            max_vertices_num = int(sys.argv[1])
            source_vertex = int(sys.argv[2])
        else:
            print("No correct input in program args, max_vertices_num = 7, source_vertex = 0")
        digraph = generate_real_random_complement_digraph(max_vertices_num)
        digraph = add_weights_digraph(digraph, -5, 40)
    print()
    print("Graph with weights: ")
    pretty_print_w_inf(digraph)
    print()
    bellman_ford(digraph, source_vertex, True)
    drawDigraph(conv_str_to_0_1(digraph), kosaraju(conv_str_to_0_1(digraph)))

