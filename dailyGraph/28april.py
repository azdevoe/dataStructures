def build_graph(edges):
    graph={}
    for [a,b] in edges:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph


def explore(graph):
    visited=set()
    keys=graph.keys()
    count=0
    largest=-10000
    for node in keys:
        if node not in visited:
            count+=1
            largest=max(largest,dfs(graph,node,visited))
    return largest
            
def dfs(graph,src,visited):
    if src in visited:return 0
    count=1
    visited.add(src)
    
    for neighbour in graph[src]:
        if neighbour not in visited:
            count+=dfs(graph,neighbour,visited)
    return count
            
def has_path(graph, src, dst):
    stack=[src]
    while len(stack)>0:
        curr=stack.pop()
        if curr == dst:
            return True
        for neighbour in graph[curr]:
            stack.append(neighbour)
    return False

def explore(graph):
    visited=set()
    path=set()
    keys=graph.keys()
    for node in keys:
            if cycle_detector(graph,node,visited,path):
                return True
    return False
def cycle_detector(graph,src,visited,path):
    if src in path:
        return True
    if src in visited:
        return False
    path.add(src)
    visited.add(src)
    for neighbour in graph[src]:
        if cycle_detector(graph,neighbour,visited,path):
            return True
    path.remove(src)
    return False

def explore(graph):
    visited=set()
    keys=graph.keys()
    for node in keys:
        if node not in visited:
            if detect_cycle(graph,node,None,visited):
                return True
    return False
def detect_cycle(graph,src,parent,visited):
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour not in visited:
            if detect_cycle(graph,neighbour,src,visited):
                return True
        else:
            if neighbour == parent:continue
            return True
    return False
        
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}
edges = [[0,1],[1,2],[2,3],[3,4]]
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['f'],
    'e': [],
    'f': []
}
graph = {
    'a': ['b'],
    'b': ['c'],
    'c': ['a'],  # cycle here
    'd': ['e'],
    'e': []
}
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1, 4],
    4: [3, 0],  # cycle: 0-2... wait, trace it yourself
}

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Build: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
#head.next.next.next.next = head.next  # points back to 2

def reverseLinked(node):
    if node==None or node.next == None:return
    p = reverseLinked(node.next)
    node.next.next = node
    node.next=None
    return p

def detectCycle(head):
    hare=head
    tortoise=head
    
    while hare and hare.next:
        hare=hare.next.next
        tortoise=tortoise.next
        if tortoise == hare:
            break
    else:
        return "no cycle"
    tortoise=head
    while tortoise != hare:
        tortoise=tortoise.next
        hare=hare.next
    return tortoise

print(reverseLinked(head))