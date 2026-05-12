def edgeToAdj(edge,n):
    graph={i:[] for i in range(n)}
    for [a,b] in edge:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    return graph
def manager(edge,n):
    graph=edgeToAdj(edge,n)
    visited=set()
    keys=graph.keys()
    count=0
    for node in keys:
        if node not in visited:
            dfs(graph,node,visited)
            count+=1
    return count

def dfs(graph,src,visited):
    stack=[src]
    while len(stack)>0:
        curr= stack.pop()
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
                
edges = [
  [0, 1],
  [1, 2],
  [3, 4],
  [5, 6],
  [6, 7],
  [7, 5]
]

print(manager(edges,10))