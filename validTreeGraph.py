def edgeToAdj(edge,n):
    graph={i:[] for i in range(n)}
    for [a,b] in edge:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def validTree(edge,n):
    visited=set()
    graph=edgeToAdj(edge,n)
    keys=graph.keys()
    count=0
    for node in keys:
        if node not in visited:
            count+=1
            if dfs(graph,node,None,visited):
                return False
    if count==1:
        return True
    else: return False
        
def dfs(graph,src,parent,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if dfs(graph,neighbour,src,visited):
                return True
        else:
            if neighbour==parent:
                continue
            return True
    return False

print(validTree([[0,1],[0,2],[0,3],[1,4]], 5))  # True
print(validTree([[0,1],[1,2],[2,3],[1,3],[1,4]], 5))  # False — cycle
print(validTree([[0,1],[0,2]], 5))  # False — disconnected