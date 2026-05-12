class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Singly:
    def __init__(self):
        self.head=None
    def add(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next = newNode
    def display(self):
        if self.head==None:
            return
        curr=self.head
        while curr:
            print(curr.val)
            curr=curr.next
    def detectCycle(self):
        curr=self.head
        fast=curr
        slow=curr
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False
    

        
        
v1 = Singly()
v1.add(1)
v1.add(2)
v1.add(3)
v1.add(4)
v1.add(5)

# manually create a cycle: 5 points back to 3
v1.head.next.next.next.next.next = v1.head.next.next  # 5 -> 3

print(v1.detectCycle())  # True

v2 = Singly()
v2.add(1)
v2.add(2)
v2.add(3)
print(v2.detectCycle())  # False