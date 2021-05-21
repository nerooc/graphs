# Project 3
 
- [Task 1 - Weighted graph randomization](#task-1---weighted-graph-randomization)
- [Task 2 - Dijkstra algorithm](#task-2---dijkstra-algorithm)
- [Task 3 - Distance matrix](#task-3---distance-matrix)
- [Task 4 - Graph center](#task-4---graph-center)
- [Task 5 - Minimum spanning tree](#task-5---minimum-spanning-tree)
 
### `ALL COMMANDS FROM README SHOULD BE EXECUTED FROM THE Lab03 DIRECTORY`
 
## Task 1 - Weighted graph randomization
 
The program generates random component graph with weights and write it to 'graph.txt' file for other tasks.
 
### 1.1 How to run the program
 
`python3 task1.py [max_vertices_number]`
max_vertices_number - maximum number of vertices in graph (positive int)
 
## Task 2 - Dijkstra algorithm
 
The program allows user to find the shortest paths from the chosen vertex to all the rest inside of a graph generated in [Task 1](#task-1---weighted-graph-randomization). **[INDEXING FROM 0]**
 
### 2.1 How to run the program
 
`python3 task2.py <path to file> [start-vertex]`
 
Where:
 
- `<path to file>` is the path to the file containing graph in form of a weighted adjacency matrix,
- `[start-vertex]` defines the number of the vertex from which we will find the shortest paths to the rest of the vertices.
 
### 2.2 Testing
 
`python3 task2.py test`
 
The tests contain the function calls for:
 
- **#1 - First vertex** of a hardcoded matrix, <br/>
- **#2 - Last vertex** of a hardcoded matrix, <br/>
 
## Task 3 - Distance matrix
 
The program allows user to generate distance matrix containing distances between each pair of vertices on the graph.
 
### 3.1 How to run the program
 
`python3 task3.py <path to file>`
 
Where `<path to file>` is the path to the file containing graph in form of a weighted adjacency matrix.
 
### 3.2 Testing
 
`python3 task3.py test`
 
The tests contain the function calls for:
 
- **#1** - Generated graph of max 5 vertices, <br/>
- **#2** - Generated graph of max 30 vertices, <br/>
 
## Task 4 - Graph center
 
The program allows user to find center and minimax center of a graph. NOTE: When printing the center or minimax center, we assume graph nodes are numbered starting with value one for the first vertex.
 
### 4.1 How to run the program
 
`python3 task4.py` - this command runs program on graph given in form of adjacency matrix (file 'graph.txt' in current folder generated in task1.py) and computes its centers.
 
`python3 task4.py <path to file>` - this command runs program on any graph given in file containing adjacency matrix, especially graph generated in _task1.py_.
 
### 4.2 Testing
 
`python3 task4.py test`
 
The tests contain the function calls for:
 
- **#1** - Simple distance matrix, one center, one minimax center <br/>
- **#2** - Bigger distance matrix, one center, one minimax center <br/>
- **#3** - Distance matrix, two centers, one minimax center<br/>
- **#4** - Distance matrix, one center, two minimax centers<br/>
- **#5** - Distance matrix, two centers, two minimax centers<br/>
 
## Task 5 - Minimum spanning tree
 
The program allows user to find and display Minimal Spanning Tree of the graph given in adjacency matrix provided as an argument.
 
### 5.1 How to run the program
 
`python3 task5.py <path to file>`
 

