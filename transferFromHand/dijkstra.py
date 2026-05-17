import heapq
def dijkstra(graph,src):
    arr=[]
    visited=set()
    heapq.heappush(arr,(0,src))
    final={}
    final[src]=0
    while arr:
        dist,curr=heapq.heappop(arr)
        if curr in visited:continue
        visited.add(curr)
        for node,distance in graph[curr]:
            if node not in visited:
                heapq.heappush(arr,((distance+dist,node)))
                final[node]=dist+distance
    return final

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(dijkstra(graph,0))