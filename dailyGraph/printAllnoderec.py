def dfs(graph,src):
    print(src)
    for neighbour in graph[src]:
        dfs(graph,neighbour)
graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

dfs(graph, 0)
# prints: 0 1 3 2