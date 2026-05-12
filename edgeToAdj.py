def edgeToAdj(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
        
# edge=[
#     ["w","x"],
#     ["x","y"],
#     ["z","y"],
#     ["z","v"],
#     ["w","v"]
# ]

edges = [
    [1, 2],
    [2, 3],
    [4, 5],
    [6, 7],
    [7, 8]
]
edgeToAdj(edges)