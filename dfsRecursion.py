def recur(graph,src,visited):
    print(src)
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour in visited:continue
        recur(graph,neighbour,visited)

# def hasPathRecur(graph,src,dst):
#     if src == dst: return True
#     for neighbour in graph[src]:
#         if hasPathRecur(graph,neighbour,dst) == True:
#             return True
#     return False
dd={
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}  
print(recur(dd,"a",visited=set()))