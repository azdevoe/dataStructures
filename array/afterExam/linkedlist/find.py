class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
a=Node("A")
b=Node("B")
c=Node("c")
d=Node("D")

a.next=b
b.next=c
c.next=d

def finder(head,target):
    if head is None:return False
    if head.val == target:
        return True
    if finder(head.next,target):
        return True
    return False
print(finder(a,"B"))