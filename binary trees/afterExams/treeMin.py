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
def treeMin(root):
    if root is None: return float("inf")
    left = treeMin(root.left)
    right = treeMin(root.right)
    return min(left,right,root.val)
print(treeMin(a))