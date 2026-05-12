def hasPath(graph,src,dst,visited):
    visited.add(src)
    if src == dst:
        return True
    print(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if hasPath(graph,neighbour,dst,visited):
                return True
    return False
graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

print(hasPath(graph, 0, 3,set())) # True
print(hasPath(graph, 2, 3,set()))  # False