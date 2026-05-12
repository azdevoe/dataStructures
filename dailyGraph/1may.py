from collections import deque
def connectedComponent(graph):
    keys=graph.keys()
    visited=set()
    count=0
    for node in keys:
        if node not in visited:
            count+=1
            dfs(graph,node,visited)
    return count
def dfs(graph,src,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
                dfs(graph,neighbour,visited)
                
def edgeToAdj(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph
    
def largest(edge):
    graph=edgeToAdj(edge)
    count=0
    print(graph)
    keys=graph.keys()
    visited=set()
    for node in keys:
        if node not in visited:
            test =dfss(graph,node,visited)
        count=max(count,test)
    return count
    
def dfss(graph,src,visited):
    queue=deque([src])
    count=0
    while queue:
        curr=queue.popleft()
        visited.add(curr)
        count+=1
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append(neighbour)
    return count

def haspath(graph,src,dst):
    stack=[src]
    visited=set()
    while stack:
        curr=stack.pop()
        if curr ==dst:
            return True
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
    return False
edges = [
  [0, 1],
  [1, 2],
  [3, 4],
  [5, 6],
  [6, 7],
  [7, 5]
]

def cycleDecDir(graph,src,visited,path):
    if src in path:return True
    if src in visited: return False
    path.add(src)
    visited.add(src)
    for neighbour in graph[src]:
        if cycleDecDir(graph,neighbour,visited,path):
            return True
    path.remove(src)
    return False

def cycleDecUndir(graph,src,parent,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if cycleDecUndir(graph,neighbour,src,visited):
                return True
        else:
            if neighbour ==parent:continue
            return True
    return False

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def floyd(node):
    curr=node
    hare=curr
    tortoise=curr
    while hare and hare.next:
        hare=hare.next.next
        tortoise=tortoise.next
        
        if hare==tortoise:
            break
    else:
        return "no cycle"
    tortoise=curr
    while tortoise != hare:
        tortoise=tortoise.next
        hare=hare.next
    return hare

def reverseL(head):
    prev=None
    curr=head
    while curr:
        next=curr.next
        curr.next=prev
        prev = curr
        curr = next
    return prev

def reverseR(head):
    if head==None or head.next==None:return head
    p=reverseR(head.next)
    head.next.next=head
    head.next=None
    return p
    
def topWrapper(graph):
    keys=graph.keys()
    result=[]
    visited=set()
    for node in keys:
        topSort(graph,node,visited,result)
    result.reverse()
    return result
def topSort(graph,src,visited,result):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            topSort(graph,neighbour,visited,result)
    result.append(src)
    
    
def khan(graph):
    indegree={node:0 for node in graph}
    final=[]
    queue =deque([])
    for node in graph:
        for neighbours in graph[node]:
            indegree[neighbours]+=1
    for node in indegree:
        if indegree[node]==0:
            queue.append(node)
    while queue:
        curr=queue.popleft()
        final.append(curr)
        for neighbour in graph[curr]:
            indegree[neighbour]-=1
            if indegree[neighbour]==0:
                queue.append(neighbour)
    return final
    
def edgeToAdjK(packages):
    graph={}
    for [a,b] in packages:
        if a not in graph:graph[a]=[]
        if b not in graph: graph[b]=[]
        graph[b].append(a)
    return graph
def wrapper(edge):
    graph=edgeToAdjK(edge)
    keys = graph.keys()
    visited=set()
    path=set()
    for node in keys:
        if cycleDetect(graph,node,visited,path):
            return True
    return False
        
def cycleDetect(graph,src,visited,path):
    if src in path:
        return True
    if src in visited:return False
    path.add(src)
    visited.add(src)
    for neighbour in graph[src]:
        if cycleDetect(graph,neighbour,visited,path):
            return True
    path.remove(src)
    return False
def install_order(packages):
    if wrapper(packages):
        return "circular dependency detected"
    queue=deque([])
    final=[]
    graph=edgeToAdjK(packages)
    indegree={node:0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour]+=1
    for node in indegree:
        if indegree[node]==0:
            queue.append(node)
    while queue:
        curr=queue.popleft()
        final.append(curr)
        for neighbour in graph[curr]:
            indegree[neighbour]-=1
            if indegree[neighbour] ==0:
                queue.append(neighbour)
    return final

packages = [
    ("app", "auth"),
    ("app", "database"),
    ("auth", "crypto"),
    ("database", "crypto"),
    ("crypto", "utils"),
]

print(install_order(packages))