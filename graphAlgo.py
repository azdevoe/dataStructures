from collections import deque
def dfs(graph,src):
    stack=[src]
    visited=set()
    while len(stack)>0:
        curr= stack.pop()
        if curr in visited:continue
        print(curr)
        visited.add(curr)
        for neighbour in graph[curr]:
            stack.append(neighbour)
            
def bfs(graph,src):
    visited=set()
    queue=deque([src])
    while(len(queue)>0):
        curr= queue.popleft()
        if curr in visited: continue
        print(curr)
        visited.add(curr)
        for neighbour in graph[curr]:
            queue.append(neighbour)
adj={
    1: [2, 3],
    2: [4, 5],
    3: [5, 6],
    4: [7],
    5: [7, 8],
    6: [8],
    7: [9],
    8: [9, 10],
    9: [10],
    10: [],
}
bfs(adj,1)