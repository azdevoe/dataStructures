from collections import deque
def wrapper(graph):
    keys=graph.keys()
    visited=set()
    count=0
    for node in keys:
        if node not in visited:
            dfs(graph,node,visited)
            count+=1
    return count
def dfs(graph,src,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
            
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}

edges = [[0,1],[1,2],[2,3],[3,4]]
n = 5

def edgeToAdj(edge,n):
    graph={i:[] for i in range(n)}
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def wrapperForLargest(graph):
    keys=graph.keys()
    visited=set()
    count=0
    for node in keys:
        if node not in visited:
            count = max(largestComp(graph,node,visited),count)
    return count
def largestComp(graph,src,visited):
    if src in visited:return 0
    visited.add(src)
    count=1
    for neighbour in graph[src]:
        if neighbour not in visited:
            count+=largestComp(graph,neighbour,visited)
    return count
            
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: [],
}
graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: [5],
    5: [4],
    6: [7, 8],
    7: [6],
    8: [6],
}


def hasPath(graph,src,dst,visited):
    if src == dst:return True
    print(src)
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if hasPath(graph,neighbour,dst,visited):
                return True
    return False

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': [],
    'e': []
}

def cycleWrapper(graph):
    visited=set()
    path=set()
    keys=graph.keys()
    for node in keys:
        if hasCycle(graph,node,visited,path):
            return True
    return False
def hasCycle(graph,src,visited,path):
    if src in path:return True
    if src in visited:return False
    visited.add(src)
    path.add(src)
    for neighbour in graph[src]:
        if hasCycle(graph,neighbour,visited,path):
            return True
    return False

graph = {
    'a': ['b'],
    'b': ['c'],
    'c': ['a'],
    'd': ['e'],
    'e': []
}

def cycleWrapperUndir(graph):
    visited=set()
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            if cycleUnDir(graph,node,None,visited):
                return True
    return False
def cycleUnDir(graph,src,parent,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if cycleUnDir(graph,neighbour,src,visited):
                return True
        else:
            if neighbour == parent:continue
            else:return True
    return False

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1, 4],
    4: [3, 2],
    2: [0, 4]
}

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# build a linked list with a cycle
head = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
head.next = a
a.next = b
b.next = c
#c.next = a  # cycle back to a

def floyd(head):
    curr=head
    tortoise=curr
    hare=curr
    while hare and hare.next:
        tortoise=tortoise.next
        hare=hare.next.next
        if hare == tortoise:
            break
    hare=curr
    
    return False
        
def floyd(head):
    curr=head
    tortoise=curr
    hare=curr
    while hare and hare.next:
        tortoise=tortoise.next
        hare=hare.next.next
        if hare == tortoise:
            break
    tortoise=curr
    while tortoise!=hare:
        tortoise=tortoise.next
        hare=hare.next
        
    nextval=hare
    while hare.next != nextval:
        hare=hare.next
    hare.next = None
    return head
        
def reverseIte(head):
    prev=None
    curr = head
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev.val

def recursive(head):
    if head.next is None or head.next is None:
        return head
    tail=recursive(head.next)
    head.next.next=head
    return tail
    



def topSortWrapper(graph):
    visited=set()
    keys=graph.keys()
    final=[]
    for node in keys:
        if node not in visited:
            topSort(graph,node,visited,final)
    final.reverse()
    return final
def topSort(graph,src,visited,final):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            topSort(graph,neighbour,visited,final)
    final.append(src)
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}


def khan(graph):
    final=[]
    indegree={node:0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour]+=1
    queue=deque([])
    for node in indegree:
        if indegree[node]==0:
            queue.append(node)
    while queue:
        curr=queue.popleft()
        final.append(curr)
        for neighbour in graph[curr]:
            indegree[neighbour]-=1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    return final

def bellmanFord(edges,src):
    allVal=set()
    for x,y,z in edges:
        allVal.add(x)
        allVal.add(y)
    dist={node:float("inf") for node in allVal}
    dist[src]=0
    length=len(dist)
    for i in range(length):
        for a,b,z in edges:
            if dist[a]+z<dist[b]:
                dist[b]=dist[a]+z
    return dist
    print(len(dist))
edges = [
    ('a', 'b', 4),
    ('a', 'c', 2),
    ('c', 'b', 1),
    ('b', 'd', 5),
    ('c', 'd', 8),
]
source = 'a'
nodes = ['a', 'b', 'c', 'd']


def matrixWrapper(matrix):
    visited=set()
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] ==1:
                if (i,j) not in visited:
                    matrixDfs(matrix,i,j,visited)
                    count+=1
    return count
def matrixDfs(matrix,row,col,visited):
    stack=[(row,col)]
    while stack:
        row,col = stack.pop()
        visited.add((row,col))
        neighbour=[(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        for ro,co in neighbour:
            if tinyhelper(matrix,ro,co,visited):
                stack.append((ro,co))

def tinyhelper(matrix,row,col,visited):
    if not (row>=0 and row<len(matrix) and col>=0 and col<len(matrix[row])):
        return False
    if matrix[row][col] == 0:
        return False
    if (row,col) in visited:
        return False
    return True

matrix = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]
print(matrixWrapper(matrix))
