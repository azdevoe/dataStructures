from collections import deque
def edgeToAdj(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph
def shortestPath(edge,src,dst):
    graph=edgeToAdj(edge)
    queue=deque([(src,0)])
    visited=set()
    visited.add(src)
    while queue:
        curr,dist=queue.popleft()
        if curr==dst:
            return dist
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append((neighbour,dist+1))
                visited.add(neighbour)
    return -1

edges = [[0,1],[0,2],[1,3],[2,3],[3,4]]
src = 0
dst = 4
print(shortestPath(edges,src,dst))