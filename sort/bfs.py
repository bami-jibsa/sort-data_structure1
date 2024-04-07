graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    X, O = [], []
    X.append(start_node)

    while X:
        node = X[0]
        del X[0]

        if node not in O:
            O.append(node)
            X.extend(graph[node])
    return O


print(bfs(graph, 'A'))
