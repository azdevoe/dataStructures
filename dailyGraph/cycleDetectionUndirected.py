def wrapper(graph):
    visited=set()
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            if dfs(graph,node,None,visited):
                return True
    return False
def dfs(graph,src,parent,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if dfs(graph,neighbour,src,visited):
                return True
        else:
            if neighbour==parent:
                return
            return True
    return False
        