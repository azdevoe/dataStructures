from collections import deque
def bfs(graph,src,dst):
    queue=deque([(src,0)])
    visited=set()
    path=[]
    vis={src:None}
    while queue:
        curr,distance=queue.popleft()
        if curr==dst:
            print(vis)
            node=dst
            while node != None:
                path.append(node)
                node=vis[node]
                path.reverse()
            return path
        for neighbour in graph[curr]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,distance+1))
                if neighbour not in path:
                    vis[neighbour]=curr
    return -1

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
print(bfs(graph,"A","E"))