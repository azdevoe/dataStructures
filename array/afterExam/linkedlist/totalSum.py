class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
a=Node(2)
b=Node(4)
c=Node(6)
d=Node(8)

a.next=b
b.next=c
c.next=d

def totalSum(head):
    if head is None: return 0
    return head.val+totalSum(head.next)
print(totalSum(a))