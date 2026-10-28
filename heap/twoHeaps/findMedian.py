# trackLiveMedian: numbers arrive one at a time (e.g. response times).
# After each number, return the current median.
# Use two heaps: lower half (max-heap) and upper half (min-heap).
import heapq
def trackLiveMedian(arr):
    maxHeap=[]
    minHeap=[]
    for num in arr:
        if not maxHeap:
            heapq.heappush(maxHeap,-num)
        else:
            if num >= -maxHeap[0]:
                heapq.heappush(minHeap,num)
            else:
                heapq.heappush(maxHeap,-num)
        print(maxHeap,minHeap)
        
        
        if len(maxHeap)-len(minHeap)>1:
            curr=heapq.heappop(maxHeap)
            heapq.heappush(minHeap,-curr)
            print(maxHeap,minHeap)
        if len(minHeap)>len(maxHeap):
            curr=heapq.heappop(minHeap)
            heapq.heappush(maxHeap,-curr)
            print(maxHeap,minHeap)
    print(maxHeap,minHeap)
    if len(maxHeap)-len(minHeap)==1:
        return -maxHeap[0]
    return ((-maxHeap[0])+minHeap[0])/2
print(trackLiveMedian([5, 2, 8, 1, 9]))