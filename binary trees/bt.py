class Bt:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Logic:
    def __init__(self):
        self.head=None
    def add(self,val):
        newNode=Bt(val)
        if self.head==None:
            self.head=newNode
            return
        curr=self.head
        
        if newNode.val>curr.val:
            while curr.right:
                curr=curr.right
            curr.right=newNode
            return
        if newNode.val<curr.val:
            while curr.left:
                curr=curr.left
            curr.left=newNode
    def dfs(self):
        curr=self.head
        stack=[curr]
        while stack:
            curr=stack.pop()
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            
        
v1=Logic()
v1.add(8)
v1.add(6)
v1.add(4)
v1.add(9)
v1.dfs()