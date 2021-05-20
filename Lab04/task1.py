import sys
from lab04 import *
from lab02 import pretty_print
import optparse

def parserFunction():
    parser = optparse.OptionParser()
    parser.add_option('-n','--noprinting',action="store_true")
    options, arguments = parser.parse_args()
    return options,arguments

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

if __name__ == '__main__':
    options,args = parserFunction()
    if len(args)==0:
        print("Zero arguments not allowed. You must provide \n-one argument (filename to convert graph in it into other representations and draw it)\n-two arguments (number of vertices and probability of existance of the edge) for generating adjacency matrix for randomly generated graph")
    elif len(args)==1:
        try:
            adj_matrix=read_digraph_file_return_adjacency_matrix(args[0])
            incidence_matrix=convert_digraph_adjacency_matrix_to_incidence_matrix(adj_matrix)
            adj_list=convert_digraph_adjacency_matrix_to_adjacency_list(adj_matrix)
            if not options.noprinting:
                print("----Adjacency matrix of generated graph:----")
                print()
                pretty_print(adj_matrix)
                print()
                print("----Incidence matrix of generated graph:----")
                print()
                pretty_print(incidence_matrix)
                print()
                print("----Adjacency list of generated graph:----")
                pretty_print_adjacency_list(adj_list)
                print()
            print("Your graph will be drawn in a moment.")
            generate_graph_from_adjacency_matrix(adj_matrix)
        except Exception as e:
            print(str(e))
    elif len(args)==2:
        if not args[0].isdigit() or not isfloat(args[1]):
            print("If you specify 2 arguments, you must provide number of vertices(int) and probability of edge (float)")
        else:
            try:
                adj_matrix=generate_random_digraph(int(args[0]), float(args[1]))
                adj_list=convert_digraph_adjacency_matrix_to_adjacency_list(adj_matrix)
                incidence_matrix=convert_digraph_adjacency_matrix_to_incidence_matrix(adj_matrix)
                if not options.noprinting:
                    print("----Adjacency matrix of generated graph:----")
                    print()
                    pretty_print(adj_matrix)
                    print()
                    print("----Incidence matrix of generated graph:----")
                    print()
                    pretty_print(incidence_matrix)
                    print()
                    print("----Adjacency list of generated graph:----")
                    pretty_print_adjacency_list(adj_list)
                    print()
                print("Your graph will be drawn in a moment.")
                generate_graph_from_adjacency_matrix(adj_matrix)
                np.savetxt("InputFiles/task1_output.txt", adj_matrix, delimiter=" ", newline = "\n", fmt="%d")
                print("Adjacency matrix of generated graph has been saved to: 'InputFiles/task1_output.txt'")
            except Exception as e:
                print("Sorry, unexpected error occured: "+str(e))
    else:
        print("Unsupported number of arguments, read README.md")
    

