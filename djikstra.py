import heapq
def dijkstra(graph,src):
    arr=[]
    visited=set()
    final={}
    heapq.heappush(arr,(0,src))
    while arr:
        cost,curr=heapq.heappop(arr)
        print(curr,cost)
        if curr in visited:continue
        visited.add(curr)
        final[curr]=cost
        for neighbour in graph[curr]:
            node,NeighbourWeight=neighbour
            if node not in visited:
                heapq.heappush(arr,(NeighbourWeight+cost,node))
                print(node,NeighbourWeight)
    return final



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('D', 1)],
    'D': [('B', 2), ('C', 1), ('E', 1)],
    'E': [('B', 5), ('D', 1)]
}
print(dijkstra(graph,"A"))