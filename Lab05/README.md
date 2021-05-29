# Project 5

## Task 1 - Generating random flow net

The program allows user to :
- generate random flow net
- display result graph 
- display and save its adjacency matrix to the txt file (`InputFiles/task1_output.txt`).

### 1.1 How to run the program

`python3 task1.py [-h] -l LAYERS [-vn VERTICES_NUMBERS [VERTICES_NUMBERS ...]]`

where:
- `LAYERS` is required integer argument representing number of middle layers (without first layer - source, and the last one - sink) of a flow net
- `VERTICES_NUMBERS` is optional list argument containing numbers of vertices corresponding to number of vertices in each of middle layers. Unless provided, program will randomly generate number of vertices in each of middle layers.

### 1.2 Example

Using command : `python3 task1.py -l 3 -vn 3 2 3` will create image shown below:
![task1_example](Preview/task1.png)

and following output:
```
----ADJACENCY MATRIX OF YOUR FLOW NET:----

0  1  10 10 0  0  0  0  1  0
0  0  0  0  0  1  0  0  0  1
0  0  0  0  9  0  0  0  0  0
0  0  0  0  5  0  0  4  0  2
0  0  0  0  0  0  0  3  0  0
0  0  0  0  0  0  5  0  4  0
0  0  0  0  0  0  0  0  0  3
0  0  0  0  0  10 0  0  0  4
0  0  0  0  0  0  5  0  0  5
0  0  0  0  0  0  0  0  0  0
```

It is worth notice that the middle layers are those without the first (source - represented by the vertex 1) and the last (sink - represented by the vertex 10) one.
