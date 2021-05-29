import networkx as nx
import numpy as np
import copy as cp

import matplotlib.pyplot as plt
import random

import math

from lab02 import pretty_print

#task1 written by Piotr Matiaszewski and Bartosz Rogowski

def generate_zeroed_adjacency_matrix(num_of_vertices):
    """Function generating empty adjacency matrix for a graph with {num_of_vertices} vertices.

    Arguments:
        num_of_vertices {int} - number of vertices in net (graph)
    
    Returns:
        adjacency_mat {list} - list of lists. It represents adjacency matrix of a empty graph (with no edges)
    """
    adjacency_mat=[[0 for _ in range(num_of_vertices)]  for _ in range(num_of_vertices)]
    return adjacency_mat

def fill_adjacency_matrix(matrix,edges):
    """Function filling adjacency matrix of graph (in this case of a net)
    
    Arguments:
        matrix: empty adjacency matrix (with no edges)
        edges {list} - list containing tuples: (edge_start,edge_end,{'weight':edge_weight})
    
    Returns:
        matrix: adjacency matrix of a net with edges determined by {edges}
    
    """
    for edge in edges:
        edge_start=edge[0]
        edge_end=edge[1]
        weight=edge[2]['weight']
        matrix[edge_start-1][edge_end-1]=weight
    return matrix


def rand_vertices(N:int):
    """
    Function is assigning position to each vertex generated in every layer of the net. The number of vertices in layer may differ: (2,N), where N is equal to number of "middle" layers
    
    Arguments:
        N {int} - number of "middle" layers

    Returns:
        pos {dict} --- {number_of_vertex:[position_x,position_y]}  
        vertices_in_layers {list} --- list of lists, inner lists refer to every layer of net, inner lists contain numbers of vertices in particular layer
    """

    #N is equal to number of layers between source and sink so final number of layers is equal N+2:
    N=N+2
    num_of_vertices_in_layer=[0 for i in range(N)]
    #source and sink have only one vertex:
    num_of_vertices_in_layer[0]=num_of_vertices_in_layer[-1]=1 

    for i in range(1,N-1): #we rand the number of vertices in layers between
        num_of_vertices_in_layer[i]=random.randint(2, N-2)
    pos={}
    vertices_in_layers=[[] for _ in range(N)]
    index=1

    for i in range(N): #for every layer
        for j in range(num_of_vertices_in_layer[i]): #for every vertex in layer
            pos[index]=np.array([ 1.5*i , -j*2+num_of_vertices_in_layer[i]])
            vertices_in_layers[i].append(index)
            index+=1
    return pos,vertices_in_layers


def add_random_minimal_edges_from_source_to_sink(list_of_layers:list):
    """
    Function is randomly generating minimal number of edges needed to connect every vertex to source and sink 
    
    Arguments:
        list_of_layers {list} - list of lists, inner lists refer to every layer of net, inner lists contain numbers of vertices in particular layer

    Returns:
        generated_edges {list} - list of lists, inner lists refer to edges' start and final vertices
    """
    number_of_vertices=len(list_of_layers)
    vertices=[i for i in range(1,number_of_vertices+1)]
    vertices_except_source=vertices[1:]
    generated_edges=[]

    for i in range(len(list_of_layers)-1):
        if len(list_of_layers[i])==1: #source edges to next layer
            for j in list_of_layers[i+1]:
                generated_edges.append([list_of_layers[i][0],j])
        if len(list_of_layers[i+1])==1: #edges to sink
            for j in list_of_layers[i]:
                generated_edges.append([j,list_of_layers[i+1][0]])

        else:
            next_layer_vertices=list_of_layers[i+1]
            this_layer_vertices=list_of_layers[i]
            case=len(next_layer_vertices)-len(this_layer_vertices)

            if case==0:
                list_of_next_layer_cpy=list_of_layers[i+1][:]
                for j in this_layer_vertices:
                    chosen_vertex=random.choice(list_of_next_layer_cpy)
                    list_of_next_layer_cpy.remove(chosen_vertex)
                    generated_edges.append([j,chosen_vertex])

            if case>0 and i!=0:
                list_of_next_layer_cpy=list_of_layers[i+1][:]
                list_of_this_layer_cpy=list_of_layers[i][:]
                for j in next_layer_vertices:
                    if list_of_this_layer_cpy==[]:
                        list_of_this_layer_cpy=list_of_layers[i][:]
                    chosen_vertex=random.choice(list_of_this_layer_cpy)
                    list_of_this_layer_cpy.remove(chosen_vertex)
                    generated_edges.append([chosen_vertex,j])

            if case<0 and i!=len(list_of_layers)-1:
                list_of_next_layer_cpy=list_of_layers[i+1][:]
                list_of_this_layer_cpy=list_of_layers[i][:]
                for j in this_layer_vertices:
                    if list_of_next_layer_cpy==[]:
                        list_of_next_layer_cpy=list_of_layers[i+1][:] 
                    chosen_vertex=random.choice(list_of_next_layer_cpy)
                    list_of_next_layer_cpy.remove(chosen_vertex)
                    generated_edges.append([j,chosen_vertex])

    return generated_edges

def create_possible_edges_list(list_of_vertices: list):
    """
    Function is randomly generating all possible edges for net with n vertices, where n equals length of list_of_vertices
    
    Arguments:
        list_of_vertices {list} - list of all vertices' numbers

    Returns:
        all_possible_edges {list} - list of lists, where every inner list refer to possible edge that can occur in net
    """
    all_possible_edges=[]
    first_vertex=list_of_vertices[0]
    last_vertes=list_of_vertices[-1]
    middle_vertices=list_of_vertices[1:-1]
    #edges from source to all vertices and all vertices to sink
    for i in middle_vertices:
        all_possible_edges.append([first_vertex,i])
        all_possible_edges.append([i,last_vertes])
    #edges from middle layers' vertices to middle layers' vertices
    for i in range(2,len(middle_vertices)+2):
        for j in range(i,len(middle_vertices)+2):
            if i!=j:
                all_possible_edges.append([i,j])
                all_possible_edges.append([j,i])
    return all_possible_edges

def add_2N_random_edges(already_existing_edges,vertices:list,num_of_layers:int):
    """
    Function is randomly generating 2*num_of_layers edges by choosing them from all possible edges that can occur in net (generated by another function).
    NOTE: already_existing_edges are passed as an argument to prevent adding them/their reverses again to the net.
    
    Arguments:
        already_existing_edges {list} -- list of lists, inner lists contain starting and final vertices of every edge
        vertices {list} - list containing all vertices' numbers
        num_of_layers {int} - number of middle layers (between source and sink) in net

    Returns:
        generated_edges {list} - list of lists, inner lists refer to edges' start and final vertices
    """
    all_possible_edges=create_possible_edges_list(vertices)
    possible_edges=[i for i in all_possible_edges if (i[::-1] not in already_existing_edges) and (i not in already_existing_edges)]
    generated_edges=[]
    for i in range(num_of_layers*2):
        generated_edge=random.choice(possible_edges)
        generated_edges.append(generated_edge)
        possible_edges.remove(generated_edge)
        if generated_edge[::-1] in possible_edges: #sink/source edges cornercase
            possible_edges.remove(generated_edge[::-1])
    return generated_edges
