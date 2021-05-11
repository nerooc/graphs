import sys
from lab02 import *

            
if __name__ == "__main__":
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 3:
        print('You did not specify enough arguments')
        sys.exit()

    input_list=[sys.argv[1],sys.argv[2]]
    if len(input_list)!=2:
        print("Invalid number of arguments")
    else:
        try:
            number_of_vertices,degree_of_vertices=int(input_list[0]),int(input_list[1])
            graph_sequence=[degree_of_vertices for i in range(number_of_vertices)] #we create degree sequence by adding to it degree of vertices n times, where n is the number of vertices
            randomized_graph=generateRandomizedKRegularGraph(graph_sequence)
            draw_graph(randomized_graph) #graph should be random
        except ValueError as e: #e.g. if user runs the program with args that are float and int
            print("Invalid input form, enter 2 ints next time, error message: " + str(e))
        except Exception as e:
            print("Sorry, an error occured, error message: " + str(e))
