class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Singly:
    def __init__(self):
        self.head=None
    def add(self,val):
        newNode=Node(val)
        curr=self.head
        if not curr:
            self.head=newNode
            return
        while curr.next:
            curr=curr.next
        curr.next=newNode
    def display(self):
        curr=self.head
        while curr:
            print(curr.val)
            curr=curr.next
    def floyd(self):
        curr=self.head
        if not curr:
            return
        hare=curr
        tortoise=curr
        while hare and hare.next:
            hare=hare.next.next
            tortoise=tortoise.next
            if hare==tortoise:
                break
        else:
            return "no cycle"
        tortoise=self.head
        while tortoise != hare:
            tortoise=tortoise.next
            hare=hare.next
        return hare.val
        
v1 = Singly()
v1.add(1)
v1.add(2)
v1.add(3)
v1.add(4)
v1.add(5)

# manually create a cycle: 5 points back to 3
v1.head.next.next.next.next.next = v1.head.next.next  # 5 -> 3

print(v1.floyd())  # True

v2 = Singly()
v2.add(1)
v2.add(2)
v2.add(3)
print(v2.floyd())  # False