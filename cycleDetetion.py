def cycleDetectionRec(graph, src, visited, path):
    if src in path:
        return True
    if src in visited:
        return False
    
    visited.add(src)
    path.add(src)
    
    for neighbour in graph[src]:
        if cycleDetectionRec(graph, neighbour, visited, path):
            return True
    
    path.remove(src)    # done with src, remove it from current path
    return False

# has cycle
graph1 = {1: [2], 2: [3], 3: [1]}

# no cycle
graph2 = {1: [2, 3], 2: [], 3: []}

print(cycleDetectionRec(graph2, 1, set(), set()))