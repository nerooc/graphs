## Task 1 - Graph decoder

First task revolves around different graph representations and their connection between each other. The program allows the user to convert a graph from a file to the other forms.

The representations have to meet some requirements.

### Program should be run with command `python3 task1.py path_to_file` 

If `path_to_file` not specified, program will try to open file called *input.txt*

### Requirements for Adjacency matrix input file:

1. File should contain only rows with matrix (no enters before matrix and after).
2. Numbers should be separated with space.

Example:

```
0 1 1 <- first line
1 0 0
1 0 0 <- last line
```

### Requirements for Adjacency list input file:

1. List should be bulleted without dots.
2. File should contain only rows with matrix (no enters before matrix and after).
3. Numbers should be separaded with spaces.

Example:

```
1. 2 3 <- first line
2. 1
3. 1 <- last line
```

### Requirements for Incidence matrix input file:

1. File should contain only rows with matrix (no enters before matrix and after).
2. Numbers should be separaded with space.

Example:

```
1 1 <- first line
1 0
0 1 <- last line
```

## Task 2 - Graph drawer

Program allows the user to draw/plot a graph based on any representation. The vertices of the graph are evenly distributed around a circle.

### Program should be run with command `python3 task2.py path_to_file` 

![graph_pic](https://github.com/nerooc/graphs/blob/main/Lab01/Preview/graph_picture.png)

## Task 3 - Graph generator

### Program should be run with command `python3 task3.py [-h] -v VERTICES [-e EDGES] [-p PROBABILITY]` 

```
arguments:
  -h, --help            show this help message and exit
  -v VERTICES, --vertices VERTICES
                        Number of vertices
  -e EDGES, --edges EDGES
                        Number of edges
  -p PROBABILITY, --probability PROBABILITY
                        Probability that an edge exists between two vertices
```

Program allows user to generate random graph based on number of vertices and number of edges or probability that between two vertices there exists an edge.
