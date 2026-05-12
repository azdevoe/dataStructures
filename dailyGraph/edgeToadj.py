def edge(edge):
    adj={}
    for [a,b] in edge:
        if a not in adj:adj[a]=[]
        if b not in adj:adj[b]=[]
        adj[a].append(b)
        adj[b].append(a)
    return adj

def connect(edgeL):
    visited=set()
    count=0
    graph=edge(edgeL)
    keys = graph.keys()
    for node in keys:
        if node not in visited:
            scout(graph,node,visited)
            count+=1
    return count

def scout(graph,node,visited):
    stack=[node]
    while len(stack)>0:
        curr=stack.pop()
        if curr in visited: continue
        visited.add(curr)
        for neighbour in graph[curr]:
            stack.append(neighbour)

edges = [
  [0, 1],
  [1, 2],
  [3, 4],
  [5, 6],
  [6, 7],
  [7, 5]
]

print(connect(edges))

#8.4.26