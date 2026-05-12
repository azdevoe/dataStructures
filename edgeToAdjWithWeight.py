import heapq
def edgeToAdj(edge):
    graph={}
    for a,b,c in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph

def dijkstra(edge,src,dst):
    graph=edgeToAdj(edge)
    arr=[]
    visited=set()
    heapq.heappush(arr,(0,src))
    final={}
    final[src]=0
    
    while arr:
        mass,curr=heapq.heappop(arr)
        if curr in visited:continue
        visited.add(curr)
        if curr==dst:
            return mass
        for neighbour in graph[curr]:
            node,weight=neighbour
            if node not in visited:
                heapq.heappush(arr,(mass+weight,node))
                final[node]=mass+weight
    print(final)
    return -1
edges = [[0,1,4],[0,2,1],[2,1,2],[1,3,1],[2,3,5]]
print(dijkstra(edges,0,3))