def topo_sort(graph):
    visited=set()
    result=[]
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            dfs(graph,node,visited,result)
    result.reverse()
    return result
def dfs(graph,src,visited,result):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited,result)
    result.append(src)

graph = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
}

print(topo_sort(graph))