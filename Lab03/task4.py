from lab03 import *
import sys

### matrices for testing purposes
matrix=[ #normal case - matrix, one centre, one minimax centre
[0, 6, 11, 8, 3, 7, 5],
[6, 0, 12, 2, 4, 8, 1],
[11, 12, 0, 13, 8, 4, 13],
[8, 2, 13, 0, 6, 9, 3],
[3, 4, 8, 6, 0, 4, 5],
[7, 8, 4, 9, 4, 0, 9],
[ 5, 1, 13, 3, 5, 9, 0]
]

matrix_2=[ #normal case - bigger matrix, one centre, one minimax centre
[0,3,2,5,7,10,8,9,12,13,14,17],
[3,0,5,2,4,7,5,6,9,10,11,14],
[2,5,0,7,6,9,7,8,11,12,13,16],
[5,2,7,0,4,7,3,6,9,8,11,13],
[7,4,6,4,0,3,1,2,5,6,7,10],
[10,7,9,7,3,0,4,1,2,6,4,7],
[8,5,7,3,1,4,0,3,6,5,8,10],
[9,6,8,6,2,1,3,0,3,5,5,8],
[12,9,11,9,5,2,6,3,0,8,2,5],
[13,10,12,8,6,6,5,5,8,0,8,5],
[14,11,13,11,7,4,8,5,2,8,0,3],
[17,14,16,13,10,7,10,8,5,5,3,0]]

matrix_two_centers=[#edge case - two centers
[0, 6, 11, 8, 3, 7, 5], 
[6, 0, 12, 2, 4, 8, 1],
[11, 12, 0, 13, 8, 4, 7],
[8, 2, 13, 0, 6, 9, 3],
[3, 4, 8, 6, 0, 4, 5], 
[7, 8, 4, 9, 4, 0, 9],
[ 5, 1, 7, 3, 5, 9, 0]
]

matrix_two_minimax_centers=[ #edge case - two minimax centers
[0, 6, 11, 8, 3, 7, 5],
[6, 0, 12, 2, 4, 8, 1],
[11, 12, 0, 13, 9, 4, 13],
[8, 2, 13, 0, 6, 9, 3],
[3, 4, 9, 6, 0, 4, 5],
[7, 8, 4, 9, 4, 0, 9],
[ 5, 1, 13, 3, 5, 9, 0]
]

matrix_both_twice_centers=[#edge case - two minimax centers and two centers
    [0, 1, 3, 2, 3],
[1, 0, 3, 3, 2],
[3, 3, 0, 5, 1],
[2, 3, 5, 0, 5]
]

if __name__ == "__main__": 
    if len(sys.argv)==2:
        if sys.argv[1]=='test':
            print("-----TEST MODE - TEST 1 - Simple case - small matrix, one center, one minimax center-----\n")
            print("Performing test for distance matrix:\n")
            print_centers_function(matrix)
            print("\n-----TEST 2- Simple case - bigger matrix----\n")
            print("Performing test for distance matrix:\n")
            print_centers_function(matrix_2)
            print("\n-----TEST 3- Edge case - graph with 2 centers----\n")
            print("Performing test for distance matrix:\n")
            print_centers_function(matrix_two_centers)
            print("\n-----TEST 4- Edge case - graph with 2 centers----\n")
            print("Performing test for distance matrix:\n")
            print_centers_function(matrix_two_minimax_centers)
            print("\n-----TEST 5- Edge case - graph with 2 centers and two minimax centers----\n")
            print("Performing test for distance matrix:\n")
            print_centers_function(matrix_both_twice_centers)
        else:
            print("The only valid second arg is 'test'")
    ############## MAIN
    elif len(sys.argv)==1:
        graph=generate_random_graph(10)
        graph = add_int_weights(graph)
        print("For provided input (matrix below):\n\n")
        pretty_print(graph)
        print("\n\nComputed distance matrix: \n\n")
        distance_matrix_=distance_matrix(graph)
        print_centers_function(distance_matrix_)
    else:
        print("You must provide 1 or 2 arguments.")
