"""
Grafy i ich zastosowania
Projekt 2, zadanie 6
Script by Tomasz Gajda
"""

from lab02 import prepare_for_hamilton, hamilton_cycle, draw_hamilton

if __name__ == "__main__":
    print("Hamilton cycle finder - Please type the name of your file:")
    file_name = input()
    graph, graph_adj_mat = prepare_for_hamilton(file_name)
    result_cycle = hamilton_cycle(graph)

    if result_cycle:
        print("The graph is Hamiltonian and the cycle is:")
        print(result_cycle)
        draw_hamilton(graph_adj_mat, result_cycle)

    else:
        print("There is no Hamiltonian cycle in the graph.")
