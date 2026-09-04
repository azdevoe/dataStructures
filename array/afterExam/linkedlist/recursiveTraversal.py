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

def recursive(head):
    if head is None: return
    print(head.val)
    recursive(head.next)

def returnRecurse(head):
    if head is None: return []
    return [head.val] + returnRecurse(head.next)

print(returnRecurse(a))