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
