from collections import deque
def shortestPath(graph,src,dst):
    queue=deque([(src,0)])
    final={}
    visited=set()
    parent={src:None}
    visited.add(src)
    path=[]
    while queue:
        curr,dist=queue.popleft()
        final[curr]=dist
        if curr==dst:
            node=dst
            print(parent)
            while node != None:
                path.append(node)
                node=parent[node]
            path.reverse()
            return path
        for neighbour in graph[curr]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,dist+1))
                if neighbour not  in parent: #new path added
                    parent[neighbour]=curr
    return -1
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
print(shortestPath(graph,"A","E"))