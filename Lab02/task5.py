from lab02 import *
            
if __name__ == "__main__":
    print("Enter the amount of vertices and their degree (two integer numbers)")
    input_string=input()
    input_list=input_string.split()
    if len(input_list)!=2:
        print("Invalid number of arguments")
    else:
        try:
            number_of_vertices,degree_of_vertices=int(input_list[0]),int(input_list[1])
        except:
            print("Invalid input form")
        graph_sequence=[degree_of_vertices for i in range(number_of_vertices)]#here we dont know yet if this graph sequence is valid 
    randomized_graph=generateRandomizedKRegularGraph(graph_sequence)
    draw_graph(randomized_graph)
