# Project 3
  - [Task 1 - Weighted graph randomization](#task-1---weighted-graph-randomization)
  - [Task 2 - Dijkstra algorithm](#task-2---dijkstra-algorithm)
  - [Task 3 - Distance matrix](#task-3---distance-matrix)
  - [Task 4 - Graph center](#task-4---graph-center)
  - [Task 5 - Minimum spanning tree](#task-5---minimum-spanning-tree)

### `ALL COMMANDS FROM README SHOULD BE EXECUTED FROM THE Lab03 DIRECTORY`

## Task 1 - Weighted graph randomization

## Task 2 - Dijkstra algorithm
The program allows user to generate weighted graph (with [Task 1](#task-1---weighted-graph-randomization)) and find the shortest paths from the chosen vertex to all the rest.

### 2.1 How to run the program

`python3 task2.py [start-vertex]`

Where `start-vertex` defines the number of the vertex for which we will find the shortest paths to the rest of the vertices.
 
### 2.2 Testing
`python3 task2.py test`

The tests contain the function calls for:
- **#1 - First vertex** of a hardcoded matrix, <br/>
- **#2 - Last vertex** of a hardcoded matrix, <br/>
## Task 3 - Distance matrix
The program allows user to generate distance matrix containing distances between each pair of vertices on the graph.

### 3.1 How to run the program

`python3 task3.py [max-vertex-num]`

Where `max-vertex-num` defines the max number (**int**) of vertices that the generated graph (for which we will create the distance matrix) should have. 

### 3.2 Testing
`python3 task2.py test`

The tests contain the function calls for:
- **#1** - Generated graph of max 5 vertices, <br/>
- **#2** - Generated graph of max 30 vertices, <br/>

## Task 4 - Graph center
The program allows user to find center and minimax center of a graph.

### 4.1 How to run the program

`python3 task4.py` - this command runs program on randomly generated graph and computes its centers.

`python3 task4.py <path to file>` - this command runs program on any graph given in file containing adjacency matrix, especially graph generated in *task1.py*.


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
