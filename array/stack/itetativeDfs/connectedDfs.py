def wrapper(graph):
    visited=set()
    keys=graph.keys()
    count=0
    for node in keys:
        if node not in visited:
            dfs(graph,node,visited)
            count+=1
    return count
def dfs(graph,src,visited):
    stack=[src]
    while stack:
        curr=stack.pop()
        if curr in visited: continue
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
    
graph={0: [1], 1: [0], 2: [3], 3: [2], 4: []}
print(wrapper(graph))