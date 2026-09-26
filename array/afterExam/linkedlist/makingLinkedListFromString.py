import sys
sys.path.insert(0, r"C:\Users\showict\Desktop\graph")

from dailyGraph.linkedList import Node
def doubleIt(head):
    yy=""
    while head:
        yy+=str(head.val)
        head=head.next
    numyy=int(yy)
    mulnumyy=2*numyy
    strmulnumyy=str(mulnumyy)
    
    prev=None
    head=None

    for ch in strmulnumyy:
        node = Node(int(ch))
        if prev is None:
            head=node
        else:
            prev.next = node
        prev=node
    return head

a=Node(9)
b=Node(9)
c=Node(9)
print(doubleIt(a.val))