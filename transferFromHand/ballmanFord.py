def bellMan(edge,src):
    mySet=set()
    for x,y,z in edge:
        mySet.add(x)
        mySet.add(y)
    mapper={node:float("inf") for node in mySet}
    mapper[src]=0
    lenth=len(mapper)
    while lenth>1:
        for x,y,z in edge:
            if mapper[x]+z<mapper[y]:
                mapper[y]=mapper[x]+z
        lenth-=1
    return mapper

edges = [[0,1,4],[0,2,1],[2,1,-3],[1,3,2]]
src = 0
dst = 3
print(bellMan(edges,0))