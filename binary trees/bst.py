class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Tree:
    def __init__(self):
        self.root=None
        

    def add(self,val):
        newNode=Node(val)
        head=self.root
        if not head:
            head=newNode
            return
        
