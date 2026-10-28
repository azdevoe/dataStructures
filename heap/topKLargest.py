from pilot import Heap

# topKLargest: given a list of numbers and k, return the k largest values
# using a min heap that never grows past size k.
def topKLargest(nums, k):
    myHeap=[]
    uu=Heap(myHeap)
    for i in range(len(nums)):
        if len(myHeap)<k:
            uu.push(nums[i])
        else:
            if uu.peek()>nums[i]:
                continue
            uu.pop()
            uu.push(nums[i])
    kk=sorted(myHeap,reverse=True)
    return kk
print(topKLargest([7, 9, 12, 8, 15, 3, 10],3))