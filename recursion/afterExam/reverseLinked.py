class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
head =Node(1)
sec=Node(2)
thi=Node(3)
fort=Node(4)
fif=Node(5)
head.next=sec
sec.next=thi
thi.next=fort
fort.next=fif
def rev(head):
    if head is None or head.next is None:return head
    p=rev(head.next)
    head.next.next=head
    head.next=None
    return p
ne=rev(head)
while ne is not None:
    print(ne.val)
    ne=ne.next