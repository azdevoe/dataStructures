def allPaths(graph, src, dst, path=[]):
    if src == dst:
        return [path + [dst]]
    result = []
    for neighbour in graph[src]:
        result += allPaths(graph, neighbour, dst, path + [src])
    return result

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [],
    4: []
}

print(allPaths(graph, 0, 4))