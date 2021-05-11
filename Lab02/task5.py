import sys
from lab02 import *

            
if __name__ == "__main__":
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        sys.exit()
    
    if len(sys.argv)==1:
        print('You did not specify enough arguments')
        sys.exit()

    if len(sys.argv) < 3:
        if len(sys.argv)==2:
            if sys.argv[1]!='test':
                print('You did not specify enough arguments')
                sys.exit()
    
    #TESTING###########################################################################
    if sys.argv[1]=='test' and len(sys.argv)==2:
        print("---TEST MODE---")
        print()
        #-------------------------------test 1--------------------------

        print("-----Test for simple case: 5 vertices, degree of every vertex = 2:-----")
        try:
            number_of_vertices,degree_of_vertices=5,2
            graph_sequence=[degree_of_vertices for i in range(number_of_vertices)]
            randomized_graph=generateRandomizedKRegularGraph(graph_sequence)
            draw_graph(randomized_graph) 
        except ValueError as e:
            print("Invalid input form, run the program with 2 ints next time.")
        except Exception as e:
            print("Sorry, an error occured, error message: " + str(e))

        #-------------------------------test 2--------------------------
        print()
        print("-----Test for corner case: 5 vertices, degree of every vertex = 4 (graph cannot be randomised):-----")
        try:
            number_of_vertices,degree_of_vertices=5,4
            graph_sequence=[degree_of_vertices for i in range(number_of_vertices)]
            randomized_graph=generateRandomizedKRegularGraph(graph_sequence)
            draw_graph(randomized_graph) 
        except ValueError as e:
            print("Invalid input form, run the program with 2 ints next time.")
        except Exception as e:
            print("Sorry, an error occured, error message: " + str(e))

        #-------------------------------test 3--------------------------
        print()
        print("-----Test for wrong input: 5 vertices, degree of every vertex = 5:-----")
        try:
            number_of_vertices,degree_of_vertices=5,5
            graph_sequence=[degree_of_vertices for i in range(number_of_vertices)]
            randomized_graph=generateRandomizedKRegularGraph(graph_sequence)
            draw_graph(randomized_graph) 
        except ValueError as e:
            print("Invalid input form, run the program with 2 ints next time.")
        except Exception as e:
            print("Sorry, an error occured, error message: " + str(e))

        #-------------------------------test 4--------------------------
        print()
        print("-----Test for wrong input: 5 vertices, degree of every vertex = 'd':-----")
        try:
            number_of_vertices,degree_of_vertices=5,'d'
            graph_sequence=[degree_of_vertices for i in range(number_of_vertices)]
            randomized_graph=generateRandomizedKRegularGraph(graph_sequence)
            draw_graph(randomized_graph) 
        except ValueError as e:
            print("Invalid input form, run the program with 2 ints next time.")
        except Exception as e:
            print("Sorry, an error occured, error message: " + str(e))

        

    #END OF TESTING###########################################################################
    else:
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
                print("Invalid input form, run the program with 2 ints next time.")
            except Exception as e:
                print("Sorry, an error occured, error message: " + str(e))