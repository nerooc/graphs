# Project 2
- [Task 1 - Degree Sequence](#task-1---degree-sequence)
- [Task 2 - Graph randomization](#task-2---graph-randomization)
- [Task 3 - Graph components](#task-3---graph-components)
- [Task 4 - Eulerian cycle](#task-4---eulerian-cycle)
- [Task 5 - *k*-regular Graph Generator](#task-5---k-regular-graph-generator)
- [Task 6 - Hamiltonian Cycle](#task-6---hamiltonian-cycle)

### `ALL COMMANDS FROM README SHOULD BE EXECUTED FROM THE Lab02 DIRECTORY`

## Task 1 - Degree Sequence

The program allows user to check whether given sequence is a degree sequence (representing graph).

## Task 2 - Graph randomization

The program allows user to randomise graph without changing vertices degrees.

## Task 3 - Graph components

The program allows user to find all components in given degree sequence representing graph.

## Task 4 - Eulerian cycle

The program allows user to find and display Eulerian cycle in a randomly generated Eulerian graph.

### 4.1 How to run the program

`python3 task4.py [number-of-vertices]`

Where `number-of-vertices` defines graph's size and should be a number within the range of **[3, 16]**. (Or more, depending on the hardware)
 
### 4.2 Testing
`python3 task4.py test`

The tests contain the function calls for:
- **#1 - minimal (3)** number of vertices in the range, <br/>
- **#2 - maximal (16)** number of vertices in the range, <br/>
- **#3 - hardcoded matrix:**

```
0 1 1 1 1 0 1 1
1 0 1 1 1 1 0 1
1 1 0 1 0 1 0 0
1 1 1 0 0 0 1 0
1 1 0 0 0 0 0 0
0 1 1 0 0 0 0 0
1 0 0 1 0 0 0 0
1 1 0 0 0 0 0 0
```

## Task 5 - *k*-regular Graph Generator

The program allows user to generate random *k*-regular graph.

## Task 6 - Hamiltonian Cycle

The program allows user to check if a graph from a file is Hamiltonian and if it is, the program finds and displays the Hamiltonian cycle.

### 6.1 How to run the program

`python3 task6.py InputFiles/[file-name]`

Where `file-name` is the name of the file containing graph in any of supported representations (AM, IM, AL, IL). <br/>
The format of the file is strictly described in [Project 1 README](https://github.com/nerooc/graphs/tree/main/Lab01#requirements-for-adjacency-matrix-input-file). <br/>

**WHEN ADDING A NEW TEST INPUT FILE, PLEASE REMEMBER ABOUT PLACING IT IN InputFiles DIRECTORY**

### 6.2 Testing
`python3 task6.py test`

The tests contain the function calls for:
- **#1** - Hamiltonian graph in form of AM
```
0 1 0 1 1 0 0 0
1 0 1 0 1 1 0 0
0 1 0 1 0 0 1 0
1 0 1 0 0 1 1 0
1 1 0 0 0 0 0 1
0 1 0 1 0 0 0 1
0 0 1 1 0 0 0 1
0 0 0 0 1 1 1 0
```

- **#2** - Non-hamiltonian graph in form of AM
```
0 1 0 0 1 1 0 0 0 0 0 0
1 0 1 0 0 1 0 0 0 0 0 0
0 1 0 1 1 0 0 0 0 0 0 1
0 0 1 0 0 0 0 1 1 0 1 0
1 0 1 0 0 0 1 0 1 0 0 0
1 1 0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 1 0 1 0 0 0 0
0 0 0 1 0 0 1 0 1 0 0 1
0 0 0 1 1 0 0 1 0 1 0 0
0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 1 0 0 0 0
```

### More info **to be added soon**.
