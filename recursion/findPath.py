class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def findPath(head,target):
    if head == None:
        return []
    if head.val == target:
        return [head.val]
    left = findPath(head.left, target)
    if left: 
        return [head.val] + left

    right = findPath(head.right, target)
    if right:  
        return [head.val] + right

    return []

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(findPath(root, 5))