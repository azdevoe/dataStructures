class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
a=Node("A")
b=Node("B")
c=Node("C")
d=Node("D")

a.next=b
b.next=c
c.next=d

def find(head,idx):
    return helper(head,idx,0)
def helper(head,idx,pidx):
    if head is None: return "out of range"
    if idx == pidx: return head.val
    return helper(head.next,idx,pidx+1)
print(find(a,2))