def manager(graph):
    visited=set()
    path=set()
    keys = graph.keys()
    for node in keys:
        if cycleDetec(graph,node,visited,path):
            return True
    return False
def cycleDetec(graph,src,visited,path):
    if src in path:
        return True
    if src in visited:
        return False
    path.add(src)
    visited.add(src)
    
    for neighbour in graph[src]:
        if cycleDetec(graph,neighbour,visited,path):
            return True
    path.remove(src)
    return False
