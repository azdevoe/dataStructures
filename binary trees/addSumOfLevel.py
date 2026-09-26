from collections import deque
from bst import Node
import heapq
a=Node(5)
b=Node(6)
c=Node(7)
a.left=b
a.right=c
c.right=Node(22)
b.right=Node(77)


def bfs(root):
    queue=deque([root])
    while queue:
        curr=queue.popleft()
        print(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
#print(bfs(a))


def addSum(root,k):
    queue=deque([])
    final=[]
    queue.append((root))
    while queue:
        levelsum=0
        for i in range(len(queue)):
            curr=queue.popleft()
            levelsum+=curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        heapq.heappush(final,levelsum)
    if len(final)<k: return -1
    return final[len(final)-k]

#print(addSum(a,1))
