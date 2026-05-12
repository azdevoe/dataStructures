from collections import deque
def khan(graph):
    queue=deque([])
    final=[]
    indegree={i:0 for i in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour]+=1
    for nodes in indegree:
        if indegree[nodes] == 0:
            queue.append(nodes)
    while queue:
        curr=queue.popleft()
        final.append(curr)
        for neighbour in graph[curr]:
            indegree[neighbour]-=1
            if indegree[neighbour]==0:
                queue.append(neighbour)
    return final
    
graph = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
}
print(khan(graph))