def bellman(edge,src,dst):
    allNode=set()
    for x,y,z in edge:
        allNode.add(x)
        allNode.add(y)
    d={node:float("inf") for node in allNode}
    d[src]=0
    length=len(d)
    while length>1:
        for x,y,z in edge:
            if d[x]+z<d[y]:
                d[y]=d[x]+z
        length-=1
    
    for x, y, z in edge:
        if d[x] + z < d[y]:
            return "negative cycle detected"
    if dst not in d:
        return -1
    return d[dst]

edges = [[0,1,4],[0,2,1],[2,1,-3],[1,3,2]]
edges = [[0,1,1],[1,2,-3],[2,1,1]]
src = 0

print(bellman(edges,src,2))