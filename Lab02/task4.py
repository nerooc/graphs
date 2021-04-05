import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from graph_processor_temp import read_graph_file_return_Adjacency_matrix, convert_Adjacency_matrix_into_Adjacency_list

# def is_eulerian():
#   function checking if graph is eulerian
#   by checking if degrees are even

def euler_cycle(graph):
    cycle = []

    def euler_dfs(v):
        for u in range(len(graph)):
            if graph[v][u] > 0:
                graph[v][u] -= 1
                graph[u][v] -= 1
                euler_dfs(u)
        cycle.append(v)

    euler_dfs(0)

    return [x+1 for x in cycle]


def find_euler_cycle():
    # I know the graph should be generated - to be implemented
    print("Euler cycle finder - Please type the name of your file:")
    file_name = input()
    graph_adj_mat = read_graph_file_return_Adjacency_matrix(file_name)

    result_cycle = euler_cycle(graph_adj_mat)

    if result_cycle: 
        print("The graph is Eulerian and the cycle is:")
        print(result_cycle)

    else:
        print("There is no Eulerian cycle in the graph.")


if __name__ == "__main__":
    find_euler_cycle()
