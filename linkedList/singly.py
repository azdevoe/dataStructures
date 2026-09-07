class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, val):
        newNode = Node(val)
        curr=self.head
        if not curr:
            self.head=newNode
            return
        while curr.next is not None:
            curr=curr.next
        curr.next=newNode

    def display(self):
        curr=self.head
        arr=[]
        while curr:
            print(curr.val)
            arr.append(curr.val)
            curr=curr.next
        return arr
    
    def remove(self):
        curr=self.head
        while curr.next.next is not None:
            curr=curr.next
        fileToDel = curr.next
        curr.next=None
        return fileToDel
    
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        p=self.reverse(head.next)
        head.next.next=head
        head.next=None
        return p
v1=LinkedList()
v1.add(1)
v1.add(2)
v1.remove()
v1.add(3)
v1.reverse(v1)
print(v1.display())