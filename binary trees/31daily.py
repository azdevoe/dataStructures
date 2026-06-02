class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def search(head,dst):
    if head is None:
        return False
    if dst == head.val:
        return True
    if dst<=head.val:
        return  search(head.left,dst)
    else:
        return search(head.right,dst)

def insert(head,val):
    if head is None:
        head=Node(val)
        return head
    if val<=head.val:
        head.left = insert(head.left,val)
        return head
    else:
        head.right =insert(head.right,val)
        return head
    
ll = insert(None, 7)
ll = insert(ll, 5)
ll = insert(ll, 9)
ll = insert(ll, 6)
ll = insert(ll, 4)

def inorder(head):
    if head is None:return []
    left =inorder(head.left)
    right=inorder(head.right)
    return left+[head.val]+right

def preorder(head):
    if head is None:return []
    return [head.val]+preorder(head.left)+preorder(head.right)

def postOrder(head):
    if head is None:return []
    return postOrder(head.left)+postOrder(head.right)+[head.val]
#print(postOrder(ll))

def height(head):
    if head is None: return -1
    left = 1+height(head.left)
    right = 1+height(head.right)
    return max(left,right)
# print(height(ll))

def lca(head,left,right):
    if head is None: return None
    if left<head.val and right < head.val:
        return lca(head.left,left,right)
    if left>head.val and right> head.val:
        return lca(head.right,left,right)
    return head.val

# print(lca(ll,6,4))

def validTree(node,minRange,maxRange):
    if node is None:
        return True
    if node.val<minRange or node.val>maxRange:
        return False
    left = validTree(node.left,minRange,node.val)
    right=validTree(node.right,node.val,maxRange)
    if left and right:
        return True
    return False

# valid BST
ll = insert(None, 7)
ll = insert(ll, 5)
ll = insert(ll, 9)
ll = insert(ll, 6)
ll = insert(ll, 4)
# print(validTree(ll, float('-inf'), float('inf')))  # True

# invalid BST - manually break it
ll.right.left = Node(3)  # put 3 in right subtree of 7 - invalid
# print(validTree(ll, float('-inf'), float('inf')))  # False

def newHeight(root):
    if root is None:
        return -1
    left=1+newHeight(root.left)
    right=1+newHeight(root.right)
    return max(left,right)
def balanced(root):
    if root is None:
        return True
    left=newHeight(root.left)
    right=newHeight(root.right)
    if abs(left-right)  >1:
        return False
    return  balanced(root.left) and balanced(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)
root.left.left.left = Node(1)
root.left.left.left.left = Node(0)

# print(balanced(root))


def lowestValue(root,smallest):
    if root is None:
        return float("-inf")
    if root.val<smallest:
        smallest=root.val
    left=lowestValue(root.left,smallest)
    right=lowestValue(root.right,smallest)
    return min(left,right)

def kitInorder(root):
    if root is None:
        return []
    return kitInorder(root.left) + [root.val]+ kitInorder(root.right)
def kthsmallest(root,k):
    if root is None:
        return float("inf")
    values =kitInorder(root)
    return values[k-1]

root = Node(7)
root.left = Node(5)
root.right = Node(9)
root.left.left = Node(4)
root.left.right = Node(6)

print(kthsmallest(root, 1))  # 4
print(kthsmallest(root, 2))  # 5
print(kthsmallest(root, 3))  # 6