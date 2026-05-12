class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def countNode(head):
    if head ==None:
        return 0
    return countNode(head.left)+countNode(head.right)+1

def height(head):
    if head == None:
        return 0
    return max(1+height(head.left),1+height(head.right))

def symetric(left,right):
    if left == None and right==None:
        return True
    if (left==None and right!=None ) or (left!=None and right==None):
        return False
    if left.val != right.val:
        return False
    return symetric(left.left,right.right)and symetric(left.right,right.left)

def allPaths(head,currentPath):
    if head==None:
        return []
    newPath=currentPath+[head.val]
    if head.left==None and head.right==None:
        return [newPath]
    return allPaths(head.left,newPath)+allPaths(head.right,newPath)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(5)
root.right.right = Node(4)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(5)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(allPaths(root,[]))