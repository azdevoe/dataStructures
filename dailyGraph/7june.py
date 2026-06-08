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
c.next = a  # cycle back to a

def floyd(head):
    curr=head
print(cycleWrapperUndir(graph))
