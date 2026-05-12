from collections import deque

def khan(graph):
    indegree = {node: 0 for node in graph}
    queue = deque()
    result = []
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1
    for a in indegree:
        if indegree[a] == 0:
            queue.append(a)
    while queue:
        curr = queue.popleft()
        result.append(curr)
        for neighbour in graph[curr]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    return result


graph = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}
arr=[]
print(khan(graph))
