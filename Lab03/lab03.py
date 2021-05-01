from queue import PriorityQueue # for task 2

# task 2 written by Tomasz Gajda

def get_neighbours(graph: list, v: int) -> list:
    '''Function finding all neighbours to a given vertex and returning
    them as a list

    Arguments:
		graph {list} -- graph in form of an adjacency matrix
        v {int} -- vertex for which we are looking for neighbours
	
    Returns:
		list -- list of neighbours of given vertex
	'''
    rank = len(graph)
    neighbours = []
    
    for i in range(rank):
        if graph[v][i] > 0:
            neighbours.append(i)
    
    return neighbours


def dijkstra(graph: list, v_start: int) -> tuple:
    '''Dijkstra algorithm implementation, finding costs of each path
    and predecessors of all vertices
    
    Arguments:
		graph {list} -- graph in form of an adjacency matrix
        v_start {int} -- vertex from which we start the process
	
    Returns:
		path_costs -- list of costs for each vertex in the graph
        predecessors -- predecessors of all vertices
	'''
    rank = len(graph)
    path_costs = [2**30 for _ in range(rank)]
    predecessors = [None for _ in range(rank)]
    path_costs[v_start] = 0

    Q = PriorityQueue()
    for v in range(rank):
        Q.put((path_costs[v], v))

    while not Q.empty():
        u_cost, u = Q.get()
        u_neighbours = get_neighbours(graph, u)
        
        for n in u_neighbours:
            if path_costs[n] > path_costs[u] + graph[u][n]:
                path_costs[n] = path_costs[u] + graph[u][n]
                predecessors[n] = u
                Q.put((path_costs[n], n))

    return path_costs, predecessors


def get_path(predecessors: list, v_start: int, v_end: int) -> list:
    '''Function finding shortest path from a given start vertex to a given end vertex

    Arguments:
        predecessors {list} -- predecessors of all vertices
        v_start {int} -- vertex from which we start the process
        v_end {int} -- vertex where we end the process

	Returns:
		path {list} -- shortest path in form of list of vertices
	'''
    path = []
    v_temp = v_end

    while v_temp != v_start:
        path.append(v_temp)
        v_temp = predecessors[v_temp]
    path.append(v_start)
    path.reverse()
    
    return path


def print_dijkstra(path_costs: list, predecessors: list, v_start: int):
    '''Function printing out all the shortest paths (to all different vertices) and costs

    Arguments:
        path_costs {list} -- list of costs for each vertex in the graph
        predecessors {list} -- predecessors of all vertices
        v_start {int} -- vertex from which we start the process
	'''
    rank = len(path_costs)
    print("START: s = " + str(v_start))

    for v in range(rank):
        print("d({0}) = {1} ==> {2}". format(v, path_costs[v], str(get_path(predecessors, v_start, v))))

########################################################################

# task 3 written by Tomasz Gajda

def distance_matrix(graph: list):
    '''Function printing out the distance matrix with distances between every pair of vertices

    Arguments:
        graph {list} -- graph in form of an adjacency matrix
	'''
    distance_matrix = []
    for v in range(9):
        path_costs, _ = dijkstra(graph, v)
        distance_matrix.append(path_costs)
    
    for row in distance_matrix:
        print(row)

########################################################################
