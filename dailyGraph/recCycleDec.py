def edgeToGraph(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
    return graph

def manager(edge):
    visited=set()
    path=set()
    graph=edgeToGraph(edge)
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            if cycle(graph,node,visited,path):
                return True
    return False
def cycle(graph,node,visited,path):
    if node in path:
        return True
    if node in visited:
        return False
    visited.add(node)
    path.add(node)
    for neighbour in graph[node]:
        if cycle(graph,neighbour,visited,path):
            return True
    path.remove(node)
    return False

edges = [
  [0, 1],
  [1, 2],
  [2, 0],  # cycle
  [3, 4],
]
print(manager(edges))