def wrapper(graph):
    visited=set()
    arr=[]
    keys =graph.keys()
    for node in keys:
        if node not in visited:
            final=topSort(graph,node,visited,arr)
    final.reverse()
    return final
def topSort(graph,src,visited,arr):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            topSort(graph,neighbour,visited,arr)
    arr.append(src)
    return arr

graph = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}
arr=[]
print(wrapper(graph))
