def dfs(graph,src,visited):
    print(src)
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: [0]  # points back to 0 — cycle
}

dfs(graph, 0, set())
