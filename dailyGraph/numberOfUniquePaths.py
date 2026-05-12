def unique(graph,src,dst):
    count=0
    if src == dst:
        return 1
    for neighbour in graph[src]:
        count+=unique(graph,neighbour,dst)
    return count
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(unique(graph,0,3))