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

def treeIncludes(root,target):
    if root is None:return False
    if root.val == target:
        return True
    left = treeIncludes(root.left,target)
    if left: return True
    right = treeIncludes(root.right,target)
    if right: return True
    return False

print(treeIncludes(a,-6))