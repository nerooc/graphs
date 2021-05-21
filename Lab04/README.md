# Project 4

## Task 1 - Generating random graphs and displaying their forms

The program allows user to:
- generate random graph 
- print other forms (adjacency list, incidence matrix, visual version) of a graph given in specified input file

In both cases user can supress output by using a flag. In second case it would lead to printing only visual version of a graph and in first case it would lead additionaly to saving the file to `InputFiles/task1_output.txt`. 

### How to run the program

`python3 task1.py number_of_vertices probability [-n]`  
In this case, without using a `-n` flag, user will be shown all of the forms of randomly generated graph, graph will be displayed and saved to `InputFiles/task1_output.txt` for future use.
When `-n` flag is used, the same thing will happen except for showing other forms of the graph in the console. 

`python3 task1.py path_to_file [-n]`
In this case, without using a `-n` flag, user will be shown all of the forms of the graph generated from file specified by `path_to_file` and graph will be displayed to user.
When `-n` flag is used, the same thing will happen except for showing other forms of the graph in the console. 



## Task 2 - Strongly Connected Components

The program allows the user to find strongly connected components in digraph using Kosaraju algorithm and coloring up to 13 different components.

Example:

![task2_example.png](./Preview/task2_example.png)

**More info to be added soon**
