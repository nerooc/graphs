import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from task1 import read_graph_file_return_Adjacency_matrix


def compute_node_coordinates(number_of_nodes,radius):
    coordinates=[(np.sin(np.pi*2*i/number_of_nodes)*radius, np.cos(np.pi*2*i/number_of_nodes)*radius) for i in range(number_of_nodes)]
    return coordinates


def get_info_from_user():
    print("Welcome to graph builder. Please type the name of your file:")
    file_name=input()
    return (file_name)


def draw_nodes(data_matrix):
    g=nx.Graph()
    node_value=1 
    number_of_nodes=len(data_matrix)
    coordinates=compute_node_coordinates(number_of_nodes,number_of_nodes*1.0)
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


def draw_edges(g,data_matrix):
    g=draw_edges_from_adjacency_matrix(g,data_matrix)
    return g


def display_graph(g):
    pos=nx.get_node_attributes(g,'pos')
    nx.draw(g,pos,node_size=10000/len(pos),with_labels=True)
    plt.axis('square') # square plot provides the real circle shape of graph
    plt.show()


if __name__ == "__main__":
    file_name=get_info_from_user()
    data_matrix=read_graph_file_return_Adjacency_matrix(file_name) #using the function from task 1
    graph=draw_nodes(data_matrix)
    graph=draw_edges(graph,data_matrix)
    display_graph(graph)
