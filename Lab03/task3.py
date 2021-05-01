"""
Grafy i ich zastosowania
Projekt 3, zadanie 3
Script by Tomasz Gajda
"""

from lab03 import distance_matrix

if __name__ == "__main__": 
    #graph will be generated after task 1 will be finished :)

    graph = [[0,  3,  0,  2,  0,  0,  0,  0,  4],   
            [3,  0,  0,  0,  0,  0,  0,  4,  0],
            [0,  0,  0,  6,  0,  1,  0,  2,  0],
            [2,  0,  6,  0,  1,  0,  0,  0,  0],
            [0,  0,  0,  1,  0,  0,  0,  0,  8],
            [0,  0,  1,  0,  0,  0,  8,  0,  0],
            [0,  0,  0,  0,  0,  8,  0,  0,  0],
            [0,  4,  2,  0,  0,  0,  0,  0,  0],
            [4,  0,  0,  0,  8,  0,  0,  0,  0]]

    distance_matrix(graph)
