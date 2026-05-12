class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def lca(head,a,b):
    if head ==None:
        return None
    if head.val== a or head.val == b:
        return head
    left=lca(head.left,a,b)
    right=lca(head.right,a,b)
    if left and right:
        return head
    if left:
        return left
    if right:
        return right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(lca(root, 4, 5).val)  # 2
print(lca(root, 4, 3).val)  # 1