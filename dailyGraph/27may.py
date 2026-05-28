def wrapper(graph):
    visited=set()
    path=set()
    keys=graph.keys()
    for node in keys:
        if cycleDetect(graph,node,visited,path):
            return True
    return False
def cycleDetect(graph,src,visited,path):
    if src in path:return True
    if src in visited: return False
    path.add(src)
    visited.add(src)
    for neighbour in graph[src]:
        if cycleDetect(graph,neighbour,visited,path):
            return True
    path.remove(src)
    return False

def wrapperForUn(graph):
    visited=set()
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            cycleDet(graph,node,None,visited)
def  cycleDet(graph,src,parent,visited):
    visited.add(src)
    if src==parent:
        return True
    for neighbour in graph[src]:
        if neighbour not in visited:
            cycleDetect(graph,neighbour,src,visited)
    


graph1 = {1: [2], 2: [3], 3: [1]}

# no cycle
graph2 = {1: [2, 3], 2: [], 3: []}

print(wrapper(graph2))