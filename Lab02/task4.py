"""
Grafy i ich zastosowania
Projekt 2, zadanie 4
Script by Tomasz Gajda
"""

import copy as cp

from lab01 import draw_graph
from lab02 import isDegreeSequence, degSeq2adjMat, generate_eulerian, euler_cycle

if __name__ == "__main__":
    print("Euler cycle - Please type the count of vertices you want:")
    n = int(input())
    graph_adj_mat = generate_eulerian(n)
    graph_adj_mat_cp = cp.deepcopy(graph_adj_mat)

    result_cycle = euler_cycle(graph_adj_mat_cp)
    print(result_cycle)
    draw_graph(graph_adj_mat)
