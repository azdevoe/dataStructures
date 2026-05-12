def hasPath(graph,src,dst,visited):
    if src == dst:
        return True
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if hasPath(graph,neighbour,dst,visited):
                return True
    return False
    
graph = {
    1: [2, 3],
    2: [1],
    3: [1],
    4: [5],
    5: [4],
    6: [],
    7: [8],
    8: [7, 9],
    9: [8]
}
print(hasPath(graph,1,3,set()))