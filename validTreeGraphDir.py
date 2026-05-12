def edgeToAdj(edge,n):
    graph={i:[] for i in range(n)}
    for [a,b] in edge:
        graph[a].append(b)
    return graph
def explore(edge,n):
    graph=edgeToAdj(edge,n)
    path=set()
    visited=set()
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            if dfs(graph,node,visited,path):
                return True
    return False
def dfs(graph,src,visited,path):
    if src in path:
        return True
    if src in visited:
        return False
    
    visited.add(src)
    path.add(src)
    
    for neighbour in graph[src]:
        if dfs(graph,neighbour,visited,path):
            return True
    path.remove(src)
    return False

print(explore([[0,1],[1,2],[2,3],[3,1]], 4))  # True — cycle
print(explore([[0,1],[1,2],[2,3]], 4))  # False — no cycle