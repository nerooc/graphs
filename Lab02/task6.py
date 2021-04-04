from graph_processor_temp import read_graph_file_return_Adjacency_matrix, convert_Adjacency_matrix_into_Adjacency_list

def hamilton_cycle(graph, v = 0, stack = None):
    if stack is None:
        stack = []
    
    size = len(graph)

    if v not in set(stack):
        stack.append(v)

        if len(stack) == size:
            if stack[-1] in graph[stack[0]]:
                stack.append(stack[0])
                return [x+1 for x in stack]
            else:
                stack.pop()
                return None

        for v_n in graph[v]:
            stack_copy = stack[:]
            hamilton_result = hamilton_cycle(graph, v_n, stack_copy)
            if hamilton_result is not None:
                return hamilton_result


def is_hamiltonian():
    print("Hamilton stack Finder - Please type the name of your file:")
    file_name = input()
    graph = convert_Adjacency_matrix_into_Adjacency_list(read_graph_file_return_Adjacency_matrix(file_name))

    for i in range(len(graph)):
        for j in range(len(graph[i])):
             graph[i][j] -= 1

    result_cycle = hamilton_cycle(graph)

    if result_cycle: 
        print("The graph is Hamiltonian and the cycle is:")
        print(result_cycle)
    else:
        print("There is no Hamiltonian cycle in the graph.")


if __name__ == "__main__":
    is_hamiltonian()
