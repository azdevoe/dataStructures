class Node:
    def __init__(self,val):
        self.val = val
        self.left=None
        self.right=None

# a=Node("a")
# b=Node("b")
# c=Node("c")
# d=Node("d")
# e=Node("e")
# f=Node("f")

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(-6)

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

def dfs(node):
    stack=[node]
    while stack:
        curr=stack.pop()
        print(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

def dfsR(node,result):
    if node is None:
        return []
    result.append(node.val)
    dfsR(node.left,result)
    dfsR(node.right,result)
    return result
    
#print(dfsR(a,[]))

def hasTarget(node,target):
    if node is None:return False
    if node.val == target:
        return True
    left = hasTarget(node.left,target)
    if left:return True
    right=hasTarget(node.right,target)
    if right:return True
    return False

#print(hasTarget(a,"f"))

def treeSum(node):
    if node is None:return 0
    return node.val+treeSum(node.left)+treeSum(node.right)

#print(treeSum(a))

def smallest(node,smalles):
    if node is None:return smalles
    if node.val<smalles:
        smalles=node.val
    left=smallest(node.left,smalles)
    right=smallest(node.right,smalles)
    return min(left,right)

def maxPathSum(node):
    if node is None:return 0
    if node.left is None and node.right is None:
        return node.val
    left=node.val+maxPathSum(node.left)
    right=node.val+maxPathSum(node.right)
    return max(left,right)
# print(maxPathSum(a))

def slidingWindow(arr,size):
    final=current=sum(arr[:size])
    for i in range(size,len(arr)):
        final=max(final,current)
        while i<len(arr):
            current=current-arr[i-size+1]+arr[i]
    return final
print(slidingWindow([1,4,1,10,25,3,5,0,26],4))