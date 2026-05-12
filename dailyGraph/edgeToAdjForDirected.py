def edgeToAdj(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph: graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
    return graph

def hasPath(edge,src,dst):
    stack=[src]
    graph=edgeToAdj(edge)
    while len(stack)>0:
        curr=stack.pop()
        if curr==dst:
            return True
        for neighbour in graph[curr]:
            stack.append(neighbour)
    return False
    
edges = [
  [0, 1],
  [1, 2],
  [2, 4],
  [3, 4],
  [5, 6],
]

print(hasPath(edges,0,4))