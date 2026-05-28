#      3
#     / \
#    9  20
#       / \
#      15  7

def has_path_sum(node, target_sum):
    if node is None:
        return False
    target_sum=target_sum-node.val
    if node.left is None and node.right is None:
        if target_sum == 0:return True
        return False
    left = has_path_sum(node.left,target_sum)
    if left:return True
    right=has_path_sum(node.right,target_sum)
    if right:return True
    return False



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
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

def fetch_node(node, target):
    if node is None:return None
    if node.val == target: return node
    left=fetch_node(node.left,target)
    if left:
        return left
    right=fetch_node(node.right,target)
    if right:
        return right
    return None
print(fetch_node(root,15))