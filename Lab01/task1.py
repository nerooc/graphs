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
        # input was Adjacency matrix
        print()
        adj_list = convert_Adjacency_matrix_into_Adjacency_list(data_matrix)
        print("Adjacency matrix -> Adjacency list:")
        for i in range(len(adj_list)):
            print(i+1, end=". ")
            for j in range(len(adj_list[i])):
                print(adj_list[i][j], end=" ")
            print()

        print()
        print("Adjacency matrix -> Incidence matrix:")
        incidence_matrix = convert_Adjacency_matrix_into_Incidence_matrix(data_matrix)
        print(*incidence_matrix, sep="\n")
        
        graph = draw_graph(adjacency_matrix)

    elif graph_rep_type == "adjacency list":
        # input was Adjacency list
        adjacency_matrix = convert_Adjacency_list_into_Adjacency_matrix(data_matrix)
        print()
        print("Adjacency list -> Adjacency matrix:")
        print(*adjacency_matrix,sep="\n")

        incidence_matrix = convert_Adjacency_list_into_Incidence_matrix(data_matrix)
        print()
        print("Adjacency list -> Incidence matrix:")
        print(*incidence_matrix,sep="\n")
        
        graph = draw_graph(adjacency_matrix)

    elif graph_rep_type == "incidence matrix":    
        # input was Incidence matrix
        adjacency_matrix = convert_Incidence_matrix_into_Adjacency_matrix(data_matrix)
        print("Incidence matrix -> Adjacency matrix:")
        print(*adjacency_matrix, sep="\n")

        adj_list = convert_Incidence_matrix_into_Adjacency_list(data_matrix)
        print()
        print("Incidence matrix -> Adjacency list:")
        for i in range(len(adj_list)):
            print(i+1,end=". ")
            for j in range(len(adj_list[i])):
                print(adj_list[i][j],end=" ")
            print()
        
        draw_graph(adjacency_matrix)

