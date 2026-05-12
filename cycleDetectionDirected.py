def wrapper(graph):
    visited=set()
    keys = graph.keys()
    for node in keys:
        if node not in visited:
            if dfs(graph,node,None,visited):
                return True
    return False
def dfs(graph,curr,parent,visited):
    visited.add(curr)
    for neighbour in graph[curr]:
        if neighbour not in visited:
            if dfs(graph,neighbour,curr,visited):
                return True
        else:
            if neighbour==parent:
                return
            return True
    return False

print(wrapper(graph = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 2]  # 4 connects back to 2 — cycle
}))