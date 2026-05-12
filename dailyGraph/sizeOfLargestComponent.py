def edgeToGraph(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph:graph[a]=[]
        if b not in graph: graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def connectedComponent(edge):
    final = 0
    visited= set()
    count= 0
    graph = edgeToGraph(edge)
    keys = graph.keys()
    for node in keys:
        if node not in visited:
            c =scout(graph,node,visited,count)
            final=max(final,c)
    return final
def scout(graph,node,visited,count):
    stack=[node]
    while len(stack)>0:
        curr=stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        count+=1
        for neighbour in graph[curr]:
            stack.append(neighbour)
    return count

edges = [
  [0, 1],
  [1, 2],
  [3, 4],
  [5, 6],
  [6, 7],
  [7, 5]
]

print(connectedComponent(edges))