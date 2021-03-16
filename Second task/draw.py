import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def compute_node_coordinates(number_of_nodes,radius):
    coordinates=[(np.sin(np.pi*2*i/number_of_nodes)*radius, np.cos(np.pi*2*i/number_of_nodes)*radius) for i in range(number_of_nodes)]
    return coordinates


def read_graph_representation_from_file(file_name, option):
    try:
        with open(file_name,"r") as f:
            l = [[int(num) for num in line.split()] for line in f] #simple fetching the matrix or list from the file and putting it into a variable
        return l
    except FileNotFoundError:
        print("Sorry, there is no file called '"+file_name+"'")
        return []


def get_info_from_user():
    print("Welcome to graph builder. Choose which one type of input you want to pass to the program (include the data in the file) (type a, b or c):\n a) Adjacency matrix \n b) Adjacency list \n c) Incidence matrix")
    while True:
        chosen_option=input()
        if chosen_option in ["a","b","c"]:
             break
        else:
            print("Mistyped! Choose again (type a, b or c):\n a) Adjacency matrix \n b) Adjacency list \n c) Incidence matrix")
    print("Type the name of your file:")
    file_name=input()
    return (file_name,chosen_option)


def draw_nodes(data_matrix):
    g=nx.Graph()
    node_value=1 
    number_of_nodes=len(data_matrix)
    coordinates=compute_node_coordinates(number_of_nodes,10)
    for i in data_matrix:
        g.add_node(node_value,pos=coordinates[node_value-1]) 
        node_value+=1 
    return g


def draw_edges_from_adjacency_matrix(g,data_matrix): #we assume the matrix is symmetrical, what allows us to iterate through its half only
    for i in range(len(data_matrix)):
        for j in range(i+1,len(data_matrix)):
            if(data_matrix[i][j]==1):
                g.add_edge(i+1,j+1)
    return g


def draw_edges_from_adjacency_list(g,data_matrix): # I need to mention that this particular file input differs from original - I got rid of the dots after the first number. In this format the first number represents the value of current node and the next ones indicate the nodes connected (attached) to it.
    for i in range(len(data_matrix)):
        for j in data_matrix[i]:
            if i!=j:
                g.add_edge(i+1,j)
    return g


def draw_edges_from_incidence_matrix(g,data_matrix):
    transposed_matrix=[[data_matrix[j][i] for j in range(len(data_matrix))] for i in range(len(data_matrix[0]))] #transposing the matrix simplifies operating on it later
    for i in range(len(transposed_matrix)):
        first_node=-1
        second_node=-1
        for j in range(len(transposed_matrix[i])):
            if transposed_matrix[i][j]==1 and first_node==-1:
                first_node=j
            elif transposed_matrix[i][j]==1 and first_node!=-1:
                second_node=j
                break
        if first_node==-1 or second_node==-1:
            print("Your file contains data that cannot be converted to graph.")
        g.add_edge(first_node+1,second_node+1)
    return g    


def draw_edges(g,data_matrix,data_type):
    if data_type=="a": # Data type: Adjacency matrix
        g=draw_edges_from_adjacency_matrix(g,data_matrix)
    elif data_type=="b": #Data type: Adjacency list
        g=draw_edges_from_adjacency_list(g,data_matrix)
    else: #Data type: Incidence matrix
        g=draw_edges_from_incidence_matrix(g,data_matrix)
    return g


def display_graph(g):
    pos=nx.get_node_attributes(g,'pos')
    nx.draw(g,pos)
    plt.axis('square') # square plot provides the real circle shape of graph
    plt.show()


file_name,chosen_option=get_info_from_user()
data_matrix=read_graph_representation_from_file(file_name,chosen_option)
graph=draw_nodes(data_matrix)
graph=draw_edges(graph,data_matrix,chosen_option)
display_graph(graph)
