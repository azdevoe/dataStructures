from collections import deque 
def shortestPath(graph,src,dst):
    visited=set()
    queue= deque([[src,0]])
    while len(queue)>0:
        [curr,distance] = queue.popleft()
        visited.add(curr)
        if curr == dst:
            return distance
        for neighbour in graph[src]:
            if neighbour  not in visited:
                queue.append([neighbour,distance+1])
    return -1
graph={
    "w":["x","y"],
    "x":["w","y"],
    "y":["x","z"],
    "z":["Y","v"],
    "v":["z","w"]
}
print(shortestPath(graph,"w","z"))