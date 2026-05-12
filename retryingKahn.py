from collections import deque
def kahn(graph):
    queue=deque([])
    final=[]
    indegree={node:0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour]+=1
    for node in indegree:
        if indegree[node]==0:
            queue.appendleft(node)
    while len(queue)>0:
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
    1: [],
    0: []
}
arr=[]
print(kahn(graph))
