def hasPath(graph,src,dst,visited):
    visited.add(src)
    if src == dst:
        return True
    for neighbour in graph[src]:
        if neighbour not in visited:
            if hasPath(graph,neighbour,dst,visited):
                return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

print(hasPath(graph, 'A', 'E',set()))
print(hasPath(graph, 'A', 'D',set()))
print(hasPath(graph, 'B', 'E',set()))