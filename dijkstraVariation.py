import heapq
def edgeToAdj(edge):
    graph={}
    for a,b,c in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph
def wrapper(edge):
    graph=edgeToAdj(edge)
    visited=set()
    dd=None
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            dd= dijkstra(graph,node,dst,visited)
    return dd

def dijkstra(graph,src,dst,visited):
    queue=[]
    heapq.heappush(queue,(0,src))
    while queue:
        weight,curr=heapq.heappop(queue)
        visited.add(curr)
        if curr == dst:
            return weight
        for neighbour in graph[curr]:
            node,mass=neighbour
            if node not in visited:
                heapq.heappush(queue,(mass+weight,node))
    return -1

edges = [[0,1,2],[1,2,4],[0,3,1],[3,4,3]]
src = 0
dst = 5
graph=edgeToAdj(edges)
#print(dijkstra(graph,src,dst,set()))

def dijkstra2(edge,src):
    graph=edgeToAdj(edge)
    visited=set()
    final={}
    queue=[]
    heapq.heappush(queue,(0,src))
    while queue:
        weight,curr=heapq.heappop(queue)
        if curr in visited:continue
        visited.add(curr)
        final[curr]=weight
        for neighbour in graph[curr]:
            node,mass=neighbour
            if node not in visited:
                heapq.heappush(queue,(mass+weight,node))
    return final

edges = [[0,1,1],[0,2,4],[1,2,2],[1,3,5],[2,3,1]]
src = 0
#print(dijkstra2(edges,src))

def dijkstra3(edge,src,dst):
    graph=edgeToAdj(edge)
    print(graph)
    queue=[]
    heapq.heappush(queue,(0,src))
    visited=set()
    parent={src:None}
    final=[]
    while queue:
        weight,curr=heapq.heappop(queue)
        if curr in visited: continue
        visited.add(curr)
        if curr ==dst:
            while parent[dst] is not None:
                final.append(dst)
                dst=parent[dst]
            final.append(dst)
            final.reverse()
            return final
        for neighbour in graph[curr]:
            node,mass=neighbour
            if node not in visited:
                heapq.heappush(queue,(mass+weight,node))
                parent[node]=curr
    return -1

edges = [[0,1,1],[0,2,4],[1,2,2],[1,3,5],[2,3,1]]
src = 0
dst = 3
print(dijkstra3(edges,src,dst))