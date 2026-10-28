import heapq

def topLargest(arr,k):
    if not arr or k>len(arr) or k<1: return None
    myHeap=[]
    for num in arr:
        if len(myHeap)<k:
            heapq.heappush(myHeap,num)
        else:
            print(myHeap)
            if num>myHeap[0]:
                heapq.heappop(myHeap)
                heapq.heappush(myHeap,num)
    return myHeap[0]

print(topLargest([], 3))
print(topLargest([40, 90], 3))