import heapq
def edgeToAdj(edge):
    graph={}
    for x,y,z in edge:
        if x not in graph:graph[x]=[]
        if y not in graph:graph[y]=[]
        graph[x].append((y,z))
        graph[y].append((x,z))
    return graph
def a(edge,src,dst,heuristic):
    visited=set()
    graph=edgeToAdj(edge)
    arr=[]
    heapq.heappush(arr,(0,0,src))
    while arr:
        est,real,curr=heapq.heappop(arr)        
        if curr in visited:continue
        if curr == dst:
            return real
        visited.add(curr)
        print(est,real,curr)
        for node,distance in graph[curr]:
            if node not in visited:
                heapq.heappush(arr,(distance+heuristic[node]+real,real+distance,node))
    return -1
edges = [[0,1,2],[0,2,4],[1,3,5],[2,3,1],[3,4,3]]

# estimated distance from each node to dst (node 4)
heuristic = {
    0: 6,
    1: 4,
    2: 3,
    3: 2,
    4: 0
}

src = 0
dst = 4

print(a(edges,src,dst,heuristic))