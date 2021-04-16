import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


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

def display_graph_coloured_sequences(g,node_colors_tab):
    """Function displaying graph with each sequence coloured different"""
    pos=nx.get_node_attributes(g,'pos')
    nx.draw(g,pos,node_size=10000/len(pos),node_color=node_colors_tab,with_labels=True)
    plt.axis('square') # square plot provides the real circle shape of graph
    plt.show()

def draw_graph(data_matrix,node_colors_tab=None):
  graph=draw_nodes(data_matrix)
  graph=draw_edges(graph,data_matrix)
  if node_colors_tab == None:
    display_graph(graph)
  else:
    display_graph_coloured_sequences(graph,node_colors_tab)
