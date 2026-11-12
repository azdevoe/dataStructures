# trackLiveMedian: numbers arrive one at a time (e.g. response times).
# Return the median after the LAST number, using two heaps.
import heapq
def trackLiveMedian(arr):
    if len(arr)<=0:
        return None
    if len(arr)==1:
        return arr[0]
    maxHeap=[]
    minHeap=[]
    for num in arr:
        if not maxHeap:
            heapq.heappush(maxHeap,-num)
        else:
            if num<=-maxHeap[0]:
                heapq.heappush(maxHeap,-num)
            else:
                heapq.heappush(minHeap,num)
        if len(maxHeap)-len(minHeap)>1:
            top=maxHeap[0]
            heapq.heappop(maxHeap)
            heapq.heappush(minHeap,-top)
        if len(minHeap)>len(maxHeap):
            top=minHeap[0]
            heapq.heappop(minHeap)
            heapq.heappush(maxHeap,-top)
    print(maxHeap,minHeap)
    if len(maxHeap)>len(minHeap):
        return -maxHeap[0]
    return ((-maxHeap[0])+minHeap[0])/2
print(trackLiveMedian([5, 2, 8, 1, 9]))
print(trackLiveMedian([5, 2, 8, 1]))