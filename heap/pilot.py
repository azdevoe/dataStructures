class Heap:
    def __init__(self,arr):
        self.arr=arr
        self.heapify()
        # heapIndexHelpers: given an index i in a 0-indexed array heap,
    # return the left child index, right child index, and parent index.
    def getLeftChild(self,i):
        return i*2+1

    def getRightChild(self,i):
        return i*2+2

    def getParent(self,i):
        return (i-1)//2
    
    # siftUpMinHeap: after a new value was appended at the end of arr,
    # move it up until every parent is <= its children.
    def swap(self,left,right):
        arr=self.arr
        [arr[left],arr[right]]=[arr[right],arr[left]]
    def siftUpMinHeap(self):
        i=len(self.arr)-1
        arr=self.arr
        while i>0 and arr[i]<arr[self.getParent(i)]:
            self.swap(i,self.getParent(i))
            i=self.getParent(i)
    def push(self,value):
        self.arr.append(value)
        self.siftUpMinHeap()
    # siftDownMinHeap: after the root was replaced by the old last element,
    # move it down, swapping with the smaller child, until the min heap rule holds.
    def siftDownMinHeap(self,i=0,size=None):
        arr = self.arr
        if size is None:
            size=len(arr)
        while True:
            left = self.getLeftChild(i)
            if left >= size:              # stop 1: no children
                break
            smallest = left
            right = self.getRightChild(i)
            if right < size and arr[right] < arr[left]:
                smallest = right              # right child exists AND is smaller
            if arr[i] <= arr[smallest]:       # stop 2: the rule already holds
                break
            self.swap(i, smallest)            # swap INDEXES, not values
            i = smallest                      # keep tracking where the value is now
    # popMinHeap: remove and return the smallest value, then restore the min heap rule.
    def pop(self):
        arr=self.arr
        if not arr: return "empty tree"
        if len(arr)==1: return arr.pop()
        self.swap(0,len(arr)-1)
        yy= arr.pop()
        self.siftDownMinHeap()
        return yy
    
    def heapify(self):
        final=len(self.arr)-1
        lastParent=self.getParent(final)
        while lastParent>=0:
            self.siftDownMinHeap(lastParent)
            lastParent-=1
    def peek(self):
        return self.arr[0]
    def heapSort(self):
        size=len(self.arr)
        while size>0:
            self.swap(0,size-1)
            size-=1
            self.siftDownMinHeap(0,size)
            
arr=[10,8,6,0, 4, 1, 9, 5, 2]
h1=Heap(arr)
h1.pop()
h1.heapSort()
print(arr)