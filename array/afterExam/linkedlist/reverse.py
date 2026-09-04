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

def rev(head):
    curr=head
    prev=None
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

def revRec(head):
    if head is None or head.next is None:
        return head
    p=revRec(head.next)
    head.next.next=head
    head.next=None
    return p
print(revRec(a).val)