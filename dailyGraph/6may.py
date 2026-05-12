from collections import deque
import heapq
def wrapper(graph):
    keys=graph.keys()
    visited=set()
    count=0
    for node in keys:
        if node not in visited:
            connected(graph,node,visited)
            count+=1
    return count
        
def connected(graph,src,visited):
    stack=[src]
    while stack:
        curr=stack.pop()
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
                
def edgeToAdj(edge):
    graph={}
    for a,b in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def wrapperForLargest(graph):
    keys=graph.keys()
    visited=set()
    count=float('-inf')
    for node in keys:
        if node not in visited:
            ii =explore(graph,node,visited)
            count=max(count,ii)
    return count
def explore(graph,src,visited):
    stack=[src]
    count=0
    while stack:
        curr=stack.pop()
        visited.add(curr)
        count+=1
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
    return count

def hasPath(graph,src,dst):
    visited=set()
    stack=[src]
    while stack:
        curr=stack.pop()
        if curr==dst:
            return True
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
    return False

def wrapperForCycleDetectionDirected(graph):
    keys=graph.keys()
    visited=set()
    path=set()
    for node in keys:
        if CycleDetectionDirected(graph,node,visited,path):
            return True
    return False
    
def CycleDetectionDirected(graph,node,visited,path):
    if node in path:return True
    if node in visited:return False
    visited.add(node)
    path.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            if CycleDetectionDirected(graph,neighbour,visited,path):
                return True
    path.remove(node)
    return False

def wrapperForCycleUndirected(graph):
    keys=graph.keys()
    visited=set()
    for node in keys:
        if undirectedC(graph,node,None,visited):
            return True
    return False
        
def undirectedC(graph,src,parent,visited):
    if src in visited and src!= parent:
        return True
    if src in visited and src == parent:
        return False
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if undirectedC(graph,neighbour,src,visited):
                return True
    return False
            
def floyd(head):
    curr=head
    hare=head
    tortoise=head
    while hare and hare.next != None:
        tortoise=tortoise.next
        hare=hare.next.next
        
        if hare == tortoise:
            break
    tortoise=curr
    while tortoise != hare:
        tortoise=tortoise.next
        hare=hare.next
    return hare

def reverseLR(head):
    if head is None or head.next is None:return head
    p=reverseLR(head.next)
    head.next.next=head
    head.next=None
    return p

def reverseLI(head):
    prev=None
    curr=head 
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev
def topSortWrapper(graph):
    keys=graph.keys()
    visited=set()
    arr=[]
    if wrapperForCycleDetectionDirected(graph):
        return "cycle exists"
    for node in keys:
        if node not  in visited:
            topoSort(graph,node,visited,arr)
    arr.reverse()
    return arr
def topoSort(graph,src,visited,arr):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            topoSort(graph,neighbour,visited,arr)
    arr.append(src)
    return arr


def khan(graph):
    queue=deque([])
    arr=[]
    indegree={node:0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour]+=1
    
    for node in indegree:
        if indegree[node] ==0:
            queue.append(node)
            arr.append(node)
    while queue:
        curr=queue.popleft()
        for neighbour in graph[curr]:
            indegree[neighbour]-=1
            if indegree[neighbour]==0:
                queue.append(neighbour)
                arr.append(neighbour)
    print(queue)
    return arr

graph = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}

def shortestPath(graph,src):
    queue=deque([(src,0)])
    visited=set()
    finel={src:0}
    visited.add(src)
    while queue:
        curr,distance=queue.popleft()
        for neighbours in graph[curr]:
            if neighbours not in visited:
                queue.append((neighbours,distance+1))
                visited.add(neighbours)
                finel[neighbours]=distance+1
    return finel

graph={
    "w":["x","y"],
    "x":["w","y"],
    "y":["x","z"],
    "z":["y","v"],
    "v":["z","w"]
}


def dijkstra(graph,src):
    arr=[]
    heapq.heappush(arr,(0,src))
    visited=set()
    visited.add(src)
    while arr:
        weight,curr=heapq.heappop(arr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                node,mass=neighbour
                heapq.heappush(arr,(mass+weight,node))
                visited.add(neighbour)
            
    print(arr)
    
def hasPath(graph,src,dst):
    queue=deque([src])
    visited=set()
    while queue:
        curr=queue.popleft()
        if curr==dst:
            return True
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return False
def hasPathD(graph,src,dst):
    stack=[src]
    visited=set()
    while stack:
        curr=stack.pop()
        visited.add(curr)
        if curr==dst:
            return True
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
    return False
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('D', 1)],
    'D': [('B', 2), ('C', 1), ('E', 1)],
    'E': [('B', 5), ('D', 1)]
}
print(dijkstra(graph,"A"))