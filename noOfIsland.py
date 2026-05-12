def manager(adj):
    listOfNodes=[]
    count=0
    visited=set()
    keys=adj.keys()
    for node in keys:
        if node not in visited:
            scout(adj,node,visited,listOfNodes)
            count+=1
    return listOfNodes

def scout(adj,node,visited,listOfNodes):
    stack=[node]
    obj=set()
    while len(stack)>0:
        curr=stack.pop()
        if curr in visited:continue
        visited.add(curr)
        obj.add(curr)
        for neighbour in adj[curr]:
            stack.append(neighbour)
    listOfNodes.append(obj)
    
directedIslands = {
  1: [2, 3],
  2: [4],
  3: [4],
  4: [5],
  5: [],

  6: [7],
  7: [8, 9],
  8: [10],
  9: [10],
  10: [],

  11: [12],
  12: [13],
  13: [],

  14: [15],
  15: [],
}

manager(directedIslands)