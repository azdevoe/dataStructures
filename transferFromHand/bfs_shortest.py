from collections import deque
def bfs(graph,src):
    queue=deque([])
    visited=set()
    queue.append((src,0))
    final={}
    final[src]=0
    visited.add(src)
    while queue:
        curr,dist=queue.popleft()
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append((neighbour,dist+1))
                final[neighbour]=dist+1
                visited.add(neighbour)
    return final

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
print(bfs(graph,"A"))