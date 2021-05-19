"""
Grafy i ich zastosowania
Projekt 2, zadanie 6
Script by Tomasz Gajda
"""
import sys
from lab02 import prepare_for_hamilton, hamilton_cycle, draw_hamilton

if __name__ == "__main__":
   # TWO ARGUMENTS ARE REQUIRED
    if len(sys.argv) != 2:
        raise Exception("Run as: task6.py [file-name]")

    #TESTING###########################################################################
    if(sys.argv[1] == "test"):
        print("\nTEST #1 - Test for Hamiltonian graph")
        graph, graph_adj_mat = prepare_for_hamilton("InputFiles/hamilton_adj_mat.txt")
        result_cycle = hamilton_cycle(graph)
        print("Hamiltonian cycle: " + str(result_cycle))
        draw_hamilton(graph_adj_mat, result_cycle)
        
        print("\nTEST #2 - Test for non-Hamiltonian graph")
        graph, graph_adj_mat = prepare_for_hamilton("InputFiles/non_hamilton.txt")
        result_cycle = hamilton_cycle(graph)

        if result_cycle:
            print("The graph is Hamiltonian and the cycle is:")
            print(result_cycle)
            draw_hamilton(graph_adj_mat, result_cycle)
        else:
            print("There is no Hamiltonian cycle in the graph.")


        print("\nTEST #3 - Test for semi-Hamiltonian graph")
        graph, graph_adj_mat = prepare_for_hamilton("InputFiles/semi_hamilton_adj_list.txt")
        result_cycle = hamilton_cycle(graph)

        if result_cycle:
            print("The graph is Hamiltonian and the cycle is:")
            print(result_cycle)
            draw_hamilton(graph_adj_mat, result_cycle)
        else:
            print("There is no Hamiltonian cycle in the graph.")

        sys.exit("\nEnd of testing")
    #TESTING###########################################################################

    file_name = sys.argv[1]

    graph, graph_adj_mat = prepare_for_hamilton(file_name)
    result_cycle = hamilton_cycle(graph)

    if result_cycle:
        print("The graph is Hamiltonian and the cycle is:")
        print(result_cycle)
        draw_hamilton(graph_adj_mat, result_cycle)

    else:
        print("There is no Hamiltonian cycle in the graph.")
