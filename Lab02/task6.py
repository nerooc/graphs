import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from graph_processor_temp import read_graph_file_return_Adjacency_matrix, convert_Adjacency_matrix_into_Adjacency_list

def draw_hamilton(g_am, cycle):
    g = nx.Graph()
    node_value = 1 
    labels = {}
    number_of_nodes = len(g_am)
    coordinates=[(np.sin(np.pi * 2 * i / number_of_nodes) * number_of_nodes, np.cos(np.pi * 2 * i / number_of_nodes) * number_of_nodes) for i in range(number_of_nodes)]

    for i in g_am:
        node_label = str(node_value) + "(" + str(cycle.index(node_value) + 1) +")"
        labels[node_value] = node_label
        g.add_node(node_value, pos = coordinates[node_value - 1])
        node_value += 1 

    for i in range(len(g_am)):
        for j in range(i + 1 , len(g_am)):
            if(g_am[i][j] == 1):
                g.add_edge(i + 1, j + 1)

    pos = nx.get_node_attributes(g,'pos')
    nx.draw(g, pos, node_size = 10000/len(pos), with_labels = False)
    nx.draw_networkx_labels(g, pos, labels)
    plt.axis('square')
    plt.show()

def hamilton_cycle(graph, v = 0, stack = None):
    if stack is None:
        stack = []
    
    size = len(graph)

    if v not in set(stack):
        stack.append(v)

        if len(stack) == size:
            if stack[-1] in graph[stack[0]]:
                stack.append(stack[0])
                return [x+1 for x in stack]
            else:
                stack.pop()
                return None

        for v_n in graph[v]:
            stack_copy = stack[:]
            hamilton_result = hamilton_cycle(graph, v_n, stack_copy)
            if hamilton_result is not None:
                return hamilton_result


def is_hamiltonian():
    print("Hamilton cycle finder - Please type the name of your file:")
    file_name = input()
    graph_adj_mat = read_graph_file_return_Adjacency_matrix(file_name)
    graph = convert_Adjacency_matrix_into_Adjacency_list(graph_adj_mat)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
             graph[i][j] -= 1

    result_cycle = hamilton_cycle(graph)

    if result_cycle: 
        print("The graph is Hamiltonian and the cycle is:")
        print(result_cycle)
        draw_hamilton(graph_adj_mat, result_cycle)

    else:
        print("There is no Hamiltonian cycle in the graph.")


if __name__ == "__main__":
    is_hamiltonian()
