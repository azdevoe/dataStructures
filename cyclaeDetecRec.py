def cycleDetection(graph,src,visited,path):
    if src in visited:
        return False
    if src in path:
        return True
    visited.add(src)
    path.add(src)
    for neighbour in graph[src]:
        if cycleDetection(graph, neighbour,visited,path):
            return True
    path.remove(src)
    return False