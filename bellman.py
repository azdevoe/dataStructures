def edgeToAdj(edge):
    graph={}
    for a,b,c in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append((b,c))
    return graph

def bellMan(edge,src,dst):
    nodes=set()
    for x,y,z in edge:
        nodes.add(x)
        nodes.add(y)
    
    d={node:float("inf") for node in nodes}
    d[src]=0
    
    length=len(d)
    while length>1:
        for x,y,z in edge:
            if d[x]+z<d[y]:
                d[y]=d[x]+z
        length-=1
    
    for x,y,z in edge:
        if d[x]+z != d[y]:
            return "cycle detected"
    if dst not in d:
        return -1
    return d[dst]

edges = [[0,1,4],[0,2,1],[2,1,-3],[1,3,2]]
src = 0
dst = 3
print(bellMan(edges,0,3))