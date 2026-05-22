def arraysum(arr):
    if len(arr)==0:
        return 0
    return arr[0]+arraysum(arr[1:])

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example tree: 
#      3
#     / \
#    9  20
#       / \
#      15  7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

def depthCount(head):
    if head is None:return 0
    left =1+depthCount(head.left)
    right =1+depthCount(head.right)
    return max(left,right)

def mode(arr,target):
    if len(arr)==0:return 0
    if arr[0]==target:return 1+mode(arr[1:],target)
    else:
        return mode(arr[1:],target)


def findMax(arr):
    if len(arr) ==0:
        return float("-inf")
    return max(arr[0],findMax(arr[1:]))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#      3
#     / \
#    9  20
#       / \
#      15  7
#
# Leaves are 9, 15, and 7. Expected output: 31.
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

def addLeaf(head):
    if head is None:
        return 0
    if head.left is None and head.right is None:
        return head.val
    left = addLeaf(head.left)
    right=addLeaf(head.right)
    return left+right

