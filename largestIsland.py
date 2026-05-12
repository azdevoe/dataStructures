def largestIsland(graph):
    visited=set()
    keys=graph.keys()
    longest=0
    for node in keys:
        longest = max(scout(graph,node,visited),longest)
    return longest

def scout(graph,src,visited):
    if src in visited:
        return 0
    size=1
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour in visited:continue
        size += scout(graph,neighbour,visited)
    return size

graph = {
    1: [2, 3],
    2: [1],
    3: [1],
    4: [5],
    5: [4],
    6: [],
    7: [8],
    8: [7, 9],
    9: [8]
}

print(largestIsland(graph))