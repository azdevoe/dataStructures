def manager(graph):
    visited=set()
    count=0
    key= graph.keys()
    for node in key:
        if node not in visited:
            count+=1
            noIsland(graph,node,visited)
    return count
def noIsland(graph,src,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour in visited:continue
        noIsland(graph,neighbour,visited)
        
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
print(manager(graph))