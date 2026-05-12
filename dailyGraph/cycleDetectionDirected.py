def edgeToAdj(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph: graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
    print(graph)
    return graph



def manager(edge):
    graph=edgeToAdj(edge)
    visited=set()
    path=set()
    for node in graph:
        if node not in visited:
            if cycleDetection(graph,node,visited,path):
                return True
    return False
def cycleDetection(graph,src,visited,path):
    if src in path:
        return True
    if src in visited:
        return False
    visited.add(src)
    path.add(src)
    for neighbour in graph[src]:
            if cycleDetection(graph,neighbour,visited,path):
                return True
    path.remove(src)
    return False

edges = [
  [0, 1],
  [1, 2],
  [2, 0],  # cycle
  [3, 4],
]

print(manager(edges))