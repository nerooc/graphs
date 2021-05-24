from lab04 import generate_real_random_complement_digraph, add_weights_digraph, drawDigraph, kosaraju, bellman_ford, generate_random_digraph
from lab02 import pretty_print
import numpy as np
import sys

if __name__ == '__main__':
    print("This program generates random complement digraph.\nIn input args set max vertices number and source vertex for bellman_ford")
    max_vertices_num = 5
    source_vertex = 0
    if len(sys.argv) != 2:
        print("No input in program args, max_vertices_num = 5, source_vertex = 0")
    else:
        max_vertices_num = int(sys.argv[1])
        source_vertex = int(sys.argv[2])

    digraph = generate_real_random_complement_digraph(max_vertices_num)
    array = np.array(digraph)
    add_weights_digraph(digraph, -5, 40)
    pretty_print(digraph)
    print()
    print("belman_ford: ", bellman_ford(digraph, source_vertex))
    drawDigraph(array, kosaraju(array))
