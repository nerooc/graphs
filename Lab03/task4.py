from lab03 import *

#this file is total mess, needs to discuss input type of data, but on distance matrices algorithm from lab03 works perfectly.

matrix=[
[0, 6, 11, 8, 3, 7, 5],
[6, 0, 12, 2, 4, 8, 1],
[11, 12, 0, 13, 8, 4, 13],
[8, 2, 13, 0, 6, 9, 3],
[3, 4, 8, 6, 0, 4, 5],
[7, 8, 4, 9, 4, 0, 9],
[ 5, 1, 13, 3, 5, 9, 0]
]

matrix_2=[[0,3,2,5,7,10,8,9,12,13,14,17],
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

if __name__ == "__main__": 
    print("Centrum = "
        +str(get_graph_centre_from_distance_matrix(matrix_2)[0])
        +" (Suma odległości = "+
        str(get_graph_centre_from_distance_matrix(matrix_2)[1])+").")

    print("Centrum minimax = ",end="")
    print(get_minimax_centre_from_distance_matrix(matrix_2)[0],end="")
    print(" (odległość od najdalszego: ",end="")
    print(get_minimax_centre_from_distance_matrix(matrix_2)[1],end="")
    print(")")
