import random #for task 2
import time #for task 2
from lab01 import convert_Adjacency_matrix_into_Adjacency_list #for task 2
from lab01 import convert_Adjacency_list_into_Adjacency_matrix #for task 2


# task 2 by Karol Szeliga

def graph_randomization(adjacency_matrix):
    """
    :param adjacency_matrix: 
    :return: randomised adjacency_matrix
    """
    ## some explanation
    # algorithm mixes edges in graph without changing vertex degrees

    # using adjacency list it finds randomly 4 vertices (A,B,C,D) with:
    # 1. edges between A-B and C-D
    # 2. not edges between A..C and C..D
    # When vertices are found edges are mixed:
    # A-B C-D are swapped to A-C B-D

    # algorithm repeats finding and swapping several times depend on size of the graph
    
    work_on_complement = False
    if count_edges(adjacency_matrix) > int(full_graph_edges(len(adjacency_matrix))/2):
        adjacency_matrix = graph_complement(adjacency_matrix)
        work_on_complement = True

    adjacency_list = convert_Adjacency_matrix_into_Adjacency_list(adjacency_matrix)

    all_selectable_ver = list(range(len(adjacency_list)))
    for i in range(len(all_selectable_ver)):  # sort out empty and full vertices
        if len(adjacency_list[i]) == 0 or len(adjacency_list[i]) == len(adjacency_list) - 1:
            all_selectable_ver.remove(i)
    # print("all selectable vertices -> ", all_selectable_ver)

    # number of finding and swapping
    mixes_number = random.choice(range(int(len(adjacency_list) / 2), int(len(adjacency_list))))
    for i in range(mixes_number):
        if len(all_selectable_ver) < 2:
            print("[This graph cannot be randomise, return with no swap]")
            break
        edgesAllA = all_selectable_ver.copy()
        foundAll = False
        iverA, iverD, verB, verC = [0, 0, 0, 0]
        graphImposibleToRand = False
        foundA = False
        while not foundA:
            iverA = random.choice(edgesAllA)  # iterator for first 'A' vertex (iverA = i -> i+1 vertex)
            edgesAllD = all_selectable_ver.copy()
            edgesAllD.remove(iverA)
            foundA = True
            foundD = False
            while not foundD:
                iverD = random.choice(edgesAllD)  # iterator for second 'D' vertex  (iverD = i -> i+1 vertex)
                if adjacency_list[iverA].__contains__(iverD + 1):  # if D-A then find another D
                    if len(edgesAllD) <= 1:
                        foundA = False
                        foundD = True  # fake, return and try to find another A
                    else:
                        edgesAllD.remove(iverD)
                else:
                    foundD = True
                    edgesA = adjacency_list[iverA].copy()
                    foundB = False
                    while not foundB:
                        verB = random.choice(edgesA)  # vertex B
                        # B will never be D, because there is no A-D
                        edgesD = adjacency_list[iverD].copy()
                        if edgesD.__contains__(verB):
                            if len(edgesD) <= 1:
                                foundD = False
                                foundB = True  # fake, return and try to find D again
                                foundC = True  # fake, return and try to find D again
                            else:
                                edgesD.remove(verB)
                                foundB = True
                                foundC = False
                        else:
                            foundB = True
                            foundC = False
                        while not foundC:
                            verC = random.choice(edgesD)  # vertex C
                            if not adjacency_list[verC - 1].__contains__(verB):
                                foundC = True
                                foundAll = True  # if found C, then all vertices has correct edges
                            else:
                                if len(edgesD) <= 1:
                                    foundB = False
                                    foundC = True  # fake, return and try to find B and C again
                                else:
                                    edgesD.remove(verC)  # try to find another C
                        if not foundB:
                            if len(edgesA) <= 1:
                                foundD = False
                                foundB = True  # fake, return and try to find D again
                            else:
                                edgesA.remove(verB)  # try to find another B
                    if not foundD:
                        if len(edgesAllD) <= 1:
                            foundA = False
                            foundD = True  # fake, return and try to find another A
                        else:
                            edgesAllD.remove(iverD)  # try to find another D
                if not foundA:
                    if len(edgesAllA) <= 1:
                        foundA = True  # fake, this graph cannot be randomise!!!
                        graphImposibleToRand = True
                    else:
                        edgesAllA.remove(iverA)  # try to find another D

        if graphImposibleToRand:
            print("[This graph cannot be randomise, return with no swap]")
            break
        else:
            # mixing
            # print(iverA+1,"-X-", verB," ", verC,"-X-", iverD+1)
            # print(iverA+1,"-", iverD+1," ", verC,"-", verB)
            # print()
            iAB = adjacency_list[iverA].index(verB)
            adjacency_list[iverA][iAB] = iverD + 1
            iDC = adjacency_list[iverD].index(verC)
            adjacency_list[iverD][iDC] = iverA + 1

            iBA = adjacency_list[verB - 1].index(iverA + 1)
            adjacency_list[verB - 1][iBA] = verC
            iCD = adjacency_list[verC - 1].index(iverD + 1)
            adjacency_list[verC - 1][iCD] = verB

    if work_on_complement:
        return graph_complement(convert_Adjacency_list_into_Adjacency_matrix(adjacency_list))
    else:
        return convert_Adjacency_list_into_Adjacency_matrix(adjacency_list)


def count_edges(adjacency_matrix):
    count = 0
    for i in range(len(adjacency_matrix) - 1):
        for j in range(i + 1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                count += 1
    return count


def set_opposite(cell):
    if cell == 0:
        return 1
    else:
        return 0


def graph_complement(adjacency_matrix):
    complement_adjacency_matrix = [[set_opposite(cell) for cell in row] for row in adjacency_matrix]
    for i in range(len(complement_adjacency_matrix)):
        complement_adjacency_matrix[i][i] = 0
    return complement_adjacency_matrix


def full_graph_edges(length):
    return length*(length-1)/2

############################################################################################################
