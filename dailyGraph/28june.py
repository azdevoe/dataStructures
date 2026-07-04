def connectedComp(graph):
    keys=graph.keys()
    visited=set()
    count=0
    for node in keys:
        if node not in visited:
            dfs(graph,node,visited)
            count+=1
    return count
def dfs(graph,src,visited):
    stack=[src]
    while stack:
        curr=stack.pop()
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
graph = {
  0: [1, 2],
  1: [0],
  2: [0],
  3: [4],
  4: [3],
  5: []
}

def edgeToAdj(edge):
    graph={}
    for a,b in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph
edges = [[0,1], [0,2], [3,4]]  # (undirected)


def largestSizeWrapper(graph):
    visited=set()
    keys=graph.keys()
    count =0
    for node in keys:
        if node not in visited:
            count =max(count,largestComp(graph,node,visited))
    return count
def largestComp(graph,src,visited):
    stack=[src]
    final=0
    count=0
    while stack:
        curr=stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        count+=1
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
    final=max(count,final)
    return final

graph={0:[1,2], 1:[0], 2:[0], 3:[4], 4:[3], 5:[]}

print(largestSizeWrapper(graph))