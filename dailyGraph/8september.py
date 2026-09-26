from linkedList import LinkedList, Node
from collections import deque
import heapq
head = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d=Node(5)
e=Node(6)
head.next = a
a.next = b
b.next = c
c.next=d
d.next=e
e.next=c
def cycleDetection(head):
    curr=head
    fast=head
    slow=head
    
    while fast  and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break
        
    fast=curr
    while fast != slow:
        fast=fast.next
        slow=slow.next
    return fast

#print(cycleDetection(head))
def edgeToAdj(edge):
    graph={}
    for [a,b] in edge:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
    print(graph)
    return graph
        
# def khan(edge):
#     graph=edgeToAdj(edge)
#     final=[]
#     indegree={node:0 for node in graph}
#     queue=deque([])
#     for node in graph:
#         for neighbour in graph[node]:
#             indegree[neighbour]+=1
#     for node in indegree:
#         if indegree[node] ==0:
#             queue.append(node)
#     while queue:
#         curr=queue.popleft()
#         final.append(curr)
#         for neighbour in graph[curr]:
#             indegree[neighbour]-=1
#             if indegree[neighbour]==0:
#                 queue.append(neighbour)
#     print(graph,indegree,queue)
#     return final
    
def khan(edge):
    graph=edgeToAdj(edge)
    queue=deque([])
    final=[]
    indegree={node:0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour]+=1
    for i in indegree:
        if indegree[i]==0:
            queue.append(i)
    while queue:
        curr=queue.popleft()
        final.append(curr)
        for neighbour in graph[curr]:
            indegree[neighbour]-=1
            if indegree[neighbour]==0:
                queue.append(neighbour)
    if len(final)!=len(graph):
        return "cycle detected"
    return final

#print(khan([("a","b"), ("b","a")]))
# print(khan([("b","m"),('a','b'),("b","z")]))
# print(khan([
#     (1, 2),
#     (1, 3),
#     (2, 4),
#     (3, 4),
#     (4, 5),
#     (5, 6),
#     (5, 7),
#     (6, 8),
#     (7, 8)
# ]))

def cycleDetecInUndirected(graph):
    visited=set()
    key=graph.keys()
    for node in key:
        if node not in visited:
            if cycleDetector(graph,node,visited,None):
                return True
    return False

def cycleDetector(graph,src,visited,parent):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if cycleDetector(graph,neighbour,visited,src):
                return True
        else:
            if neighbour==parent:continue
            else:
                return True
    return False

#print(cycleDetecInUndirected({"a":["b"],"b":["a"]}))
#print(cycleDetecInUndirected({"a":["b","c"], "b":["a","c"], "c":["a","b"]}))

def recursive(head):
    if head is None or head.next is None:
        return head
    p=recursive(head.next)
    head.next.next= head
    head.next=None
    return p

def reversalIt(head):
    curr=head
    prev=None
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

def topWrapper(graph):
    arr=[]
    visited=set()
    keys=graph.keys()
    print(keys)
    for node in keys:
        if node not in visited:
            final=topSort(graph,node,visited,arr)
    final.reverse()
    return final

def topSort(graph,src,visited,arr):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            topSort(graph,neighbour,visited,arr)
    arr.append(src)
    return arr

graph = {
    "socks": ["shoes"],
    "underwear": ["pants"],
    "pants": ["shoes", "belt"],
    "shoes": [],
    "belt": []
}
#print(topWrapper(graph))

def bfsShortestPath(graph,src,dst):
    queue=deque([(src,0)])
    final={}
    visited=set()
    visited.add(src)
    while queue:
        curr,distance=queue.popleft()
        final[curr]=distance
        if curr == dst:
            return final
        for node in graph[curr]:
            if node not in visited:
                queue.append((node,distance+1))
                visited.add(node)
    return None

# print(bfsShortestPath({
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "D", "E"],
#     "D": ["B", "C", "F"],
#     "E": ["C", "F"],
#     "F": ["D", "E", "G"],
#     "G": ["F"]
# },"A","G"))

def dijkstra(graph,src):
    queue = []
    paths={}
    heapq.heappush(queue,(0,src))
    visited=set()
    while queue:
        distance,curr=heapq.heappop(queue)
        if curr in visited:continue
        visited.add(curr)
        paths[curr]=distance
        for neighbour,dist in graph[curr]:
                if neighbour not in visited:
                    print(dist,distance)
                    heapq.heappush(queue,(dist+distance,neighbour))
    return paths
# print(dijkstra({
#     "A": [("B", 4), ("C", 1)],
#     "B": [("A", 4), ("D", 1)],
#     "C": [("A", 1), ("D", 5), ("E", 8)],
#     "D": [("B", 1), ("C", 5), ("E", 2), ("F", 6)],
#     "E": [("C", 8), ("D", 2), ("F", 3)],
#     "F": [("D", 6), ("E", 3)]
# },"A"))


def hasPathBfs(graph,src,dst):
    queue=deque([src])
    visited=set()
    visited.add(src)
    while queue:
        curr=queue.popleft()
        if curr == dst:
            return True
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return False

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
    "X": ["Y"],
    "Y": ["X"]
}

# print(hasPathBfs(graph,"A","D"))
# print(hasPathBfs(graph,"A","X"))

def hasPathRec(graph,src,dst,visited):
    visited.add(src)
    if src ==dst:
        return True
    for neighbour in graph[src]:
        if neighbour not in visited:
            if hasPathRec(graph,neighbour,dst,visited):
                return True
    return False

#print(hasPathRec(graph,"A","X", set()))

def connectedWrapper(graph):
    keys=graph.keys()
    visited = set()
    count=0
    for node in keys:
        if node not in visited:
            connectedCounter(graph,node,visited)
            count+=1
    return count

def connectedCounter(graph,src,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            connectedCounter(graph,neighbour,visited)
graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"],
    "F": ["G", "H"],
    "G": ["F"],
    "H": ["F"]
}
#print(connectedWrapper(graph))


def largestWrapper(graph):
    keys=graph.keys()
    visited=set()
    count=0
    subCount=0
    for node in keys:
        if node not in visited:
            count = max(count,largestCounter(graph,node,visited,subCount))
    return count

def largestCounter(graph,src,visited,count):
    count+=1
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            count=largestCounter(graph,neighbour,visited,count)
    return count


graph = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D", "E"],
    "D": ["C", "E"],
    "E": ["C", "D", "F"],
    "F": ["E"],
    "G": ["H", "I", "J"],
    "H": ["G"],
    "I": ["G"],
    "J": ["G"]
}
#print(largestWrapper(graph))

def dailytemp(arr):
    final=[]
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            curr=stack.pop()
            final.append(i-curr)
        stack.append(i)
    return final

print(dailytemp([73, 74, 75, 71, 69, 72, 76, 73]))