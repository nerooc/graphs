from lab01 import *
import sys


if __name__ == "__main__":
    print("Welcome to graph decoder. Path to graph data file should be typed in input args")
    file_name = 'input.txt'
    if len(sys.argv) == 1:
        print("No input in program args, trying to open file \'input.txt\'...\n")
    else:
        file_name = sys.argv[1]  # path to file with graph data

    data_matrix, graph_rep_type = read_graph_file_return_Adjacency_matrix(file_name, True)

    if graph_rep_type == "adjacency matrix":
        print()
        print("input is Adjacency matrix:")
        print_matrix(data_matrix)
        print()
        print("Adjacency matrix -> Adjacency list:")
        adjacency_list = convert_Adjacency_matrix_into_Adjacency_list(data_matrix)
        print_adjacency_list(adjacency_list)
        print()
        print("Adjacency matrix -> Incidence matrix:")
        incidence_matrix = convert_Adjacency_matrix_into_Incidence_matrix(data_matrix)
        print_matrix(incidence_matrix)
        print()
        graph = draw_graph(data_matrix)

    elif graph_rep_type == "adjacency list":
        adjacency_list = data_matrix
        print()
        print("input is Adjacency list:")
        print_adjacency_list(adjacency_list)
        print()
        print("Adjacency list -> Adjacency matrix:")
        adjacency_matrix = convert_Adjacency_list_into_Adjacency_matrix(data_matrix)
        print_matrix(adjacency_matrix)
        print()
        print("Adjacency list -> Incidence matrix:")
        incidence_matrix = convert_Adjacency_list_into_Incidence_matrix(data_matrix)
        print_matrix(incidence_matrix)
        print()
        graph = draw_graph(adjacency_matrix)

    elif graph_rep_type == "incidence matrix":
        incidence_matrix = data_matrix
        print()
        print("input is Incidence matrix:")
        print_matrix(incidence_matrix)
        print()
        print("Incidence matrix -> Adjacency matrix:")
        adjacency_matrix = convert_Incidence_matrix_into_Adjacency_matrix(data_matrix)
        print_matrix(adjacency_matrix)
        print()
        print("Incidence matrix -> Adjacency list:")
        adjacency_list = convert_Incidence_matrix_into_Adjacency_list(data_matrix)
        print_adjacency_list(adjacency_list)
        print()
        draw_graph(adjacency_matrix)
