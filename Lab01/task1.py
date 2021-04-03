from task2 import draw_nodes
from task2 import draw_edges
from task2 import display_graph
# functions
#######################################
# output could be Adjacency matrix or file_data + info which representatnion it is.
# Info as:
# 'a' -> Adjacency matrix
# 'b' -> Adjacency list
# 'c' -> Incidence matrix
def read_graph_file_return_Adjacency_matrix(file_name, return_input_info = False):
  try:
    with open(file_name, "r") as f:
      file_data = [[int(num) for num in line.split()] for line in f]

      #decode which repressentation is in input
      #########
      itIsList = False
      for row in file_data:
        for i in row:
          if i not in [0,1]:
            itIsList = True
            f.seek(0)
            file_data2 = [[int(num) for num in remove_first(line.split())] for line in f] #first int is number of vertex, must be removed
            if return_input_info:
              return (file_data,'b')
            else:
              return convert_Adjacency_list_into_Adjacency_matrix(file_data2)

      if len(file_data) == len(file_data[0]):
        isSymmetric = True # only a suspicion so far
      else:
        if return_input_info:
          return (file_data,'c')
        else:
          return convert_Incidence_matrix_into_Adjacency_matrix(file_data)
      
      for i in range(len(file_data)-1): 
        for j in range(i+1, len(file_data)):
          if file_data[i][j] != file_data[j][i]:
            isSymmetric = False
            if return_input_info:
              return (file_data,'c')
            else:
              return convert_Incidence_matrix_into_Adjacency_matrix(file_data)

      diagonalOnlyZero = True
      for i in range(len(file_data)):
        if file_data[i][i] !=0:
          diagonalOnlyZero = False
          if return_input_info:
            return (file_data,'c')
          else:
            return convert_Incidence_matrix_into_Adjacency_matrix(file_data)

      isTwoOneInCol = True
      count = 0
      for i in range(len(file_data)): 
        for j in range(len(file_data)):
          if file_data[j][i] == 1:
            count+= 1
        if count != 2:
          isTwoOneInCol = False
          if return_input_info:
            return (file_data,'a')
          else:
            return file_data
        else:
          count = 0

      if all([not itIsList, isSymmetric, diagonalOnlyZero, isTwoOneInCol]):
        print("Your matrix could be redner as Adjacency matrix or Incidence matrix!\nType 'a' if you mean Adjacency matrix and 'b' if you mean Incidence matrix:")
        while True:
          chosen_option=input()
          if chosen_option in ["a","b"]:
              break
          else:
              print("Mistyped! Choose again.\nType 'a' if you mean Adjacency matrix and 'b' if you mean Incidence matrix:")
        if chosen_option == 'a':
          if return_input_info:
            return (file_data,'a')
          else:
            return file_data
        else:
          if return_input_info:
            return (file_data,'c')
          else:
            return convert_Incidence_matrix_into_Adjacency_matrix(file_data)
      ###########
  except FileNotFoundError:
    print("Sorry, there is no file called '"+file_name+"'")
    return []

def remove_first(_list): #used in read_graph
  _list.pop(0)
  return _list

def convert_Adjacency_matrix_into_Adjacency_list(data_matrix):
  for row in data_matrix: #loop through a matrix if there is '1' somethere, print with which vertex
    adj_list = [[set_num(i,row[i]) for i in range(len(row))] for row in data_matrix]
    for _list in adj_list:
      for i in range(len(_list)):
        if -1 in _list:
          _list.remove(-1)
    return adj_list

def set_num(i,num): #used in convert_Adjacency_matrix_into_Adjacency_list
  if num != 0:
    return i+1
  else:
    return -1

def convert_Adjacency_matrix_into_Incidence_matrix(data_matrix):
  #count number of edges
  count = 0
  for i in range(len(data_matrix)-1): 
    for j in range(i+1, len(data_matrix)):
      if data_matrix[i][j] != 0:
        count+=1

  #make incidence matrix
  incidence_matrix =[[0 for x in range(count)] for y in range(len(data_matrix))]
  curr_edge = 0
  for i in range(len(data_matrix)-1):
    for j in range(i+1, len(data_matrix)):
      if data_matrix[i][j] != 0:
        incidence_matrix[i][curr_edge] = 1
        incidence_matrix[j][curr_edge] = 1
        curr_edge+=1
  
  return incidence_matrix

def convert_Adjacency_list_into_Adjacency_matrix(data_matrix):
  adjacency_matrix = [[0 for x in range(len(data_matrix))] for y in range(len(data_matrix))]
  for i in range(len(data_matrix)):
    for j in data_matrix[i]:
      adjacency_matrix[i][j-1] = 1
  return adjacency_matrix

def convert_Incidence_matrix_into_Adjacency_matrix(data_matrix):
  adjacency_matrix = [[0 for x in range(len(data_matrix))] for y in range(len(data_matrix))]

  w = -1
  h = -1
  for j in range(len(data_matrix[0])):
    for i in range(len(data_matrix)):
      if data_matrix[i][j] != 0:
        if w == -1:
          w = i
        else:
          h = i
    adjacency_matrix[w][h] = 1
    adjacency_matrix[h][w] = 1
    w = -1
    h = -1
  return adjacency_matrix

def convert_Incidence_matrix_into_Adjacency_list(data_matrix):
  temp_adj_matrix = convert_Incidence_matrix_into_Adjacency_matrix(data_matrix)
  return convert_Adjacency_matrix_into_Adjacency_list(temp_adj_matrix)

def convert_Adjacency_list_into_Incidence_matrix(data_matrix):
  temp_adj_matrix = convert_Adjacency_list_into_Adjacency_matrix(data_matrix)
  return convert_Adjacency_matrix_into_Incidence_matrix(temp_adj_matrix)

#######################################
# main
if __name__ == "__main__":
  print("Welcome to graph reader.\nType the name of your input file:")
  file_name=input()
  data_matrix, chosen_option = read_graph_file_return_Adjacency_matrix(file_name,True)

  if chosen_option == "a":
    # input was Adjacency matrix
    print()
    adj_list = convert_Adjacency_matrix_into_Adjacency_list(data_matrix)
    print("Adjacency matrix -> Adjacency list:")
    for i in range(len(adj_list)):
      print(i+1,end=". ")
      for j in range(len(adj_list[i])):
        print(adj_list[i][j],end=" ")
      print()

    print()
    print("Adjacency matrix -> Incidence matrix:")
    incidence_matrix = convert_Adjacency_matrix_into_Incidence_matrix(data_matrix)
    print(*incidence_matrix, sep="\n")
    #draw graph from task 2
    graph=draw_nodes(data_matrix)
    graph=draw_edges(graph,data_matrix)
    display_graph(graph)
    #######################################

  elif chosen_option == "b":
    # input was Adjacency list
    adjacency_matrix = convert_Adjacency_list_into_Adjacency_matrix(data_matrix)
    print()
    print("Adjacency list -> Adjacency matrix:")
    print(*adjacency_matrix,sep="\n")

    incidence_matrix = convert_Adjacency_list_into_Incidence_matrix(data_matrix)
    print()
    print("Adjacency list -> Incidence matrix:")
    print(*incidence_matrix,sep="\n")
    #draw graph from task 2
    graph=draw_nodes(adjacency_matrix)
    graph=draw_edges(graph,adjacency_matrix)
    display_graph(graph)
    #######################################

  elif chosen_option == "c":  
    # input was Incidence matrix
    adjacency_matrix = convert_Incidence_matrix_into_Adjacency_matrix(data_matrix)
    print("Incidence matrix -> Adjacency matrix:")
    print(*adjacency_matrix, sep="\n")

    adj_list = convert_Incidence_matrix_into_Adjacency_list(data_matrix)
    print()
    print("Incidence matrix -> Adjacency list:")
    for i in range(len(adj_list)):
      print(i+1,end=". ")
      for j in range(len(adj_list[i])):
        print(adj_list[i][j],end=" ")
      print()
    #draw graph from task 2
    graph=draw_nodes(adjacency_matrix)
    graph=draw_edges(graph,adjacency_matrix)
    display_graph(graph)
    #######################################

