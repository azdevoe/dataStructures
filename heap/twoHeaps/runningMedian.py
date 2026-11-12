import heapq
# runningMedians: numbers arrive one at a time (e.g. response times).
# Return a LIST holding the median after EACH number arrived.
def runningMedians(arr):
    final=[0]*len(arr)
    maxHeap,minHeap=[],[]
    count=0
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
        
        if len(maxHeap)>len(minHeap):
            final[count]=-maxHeap[0]
        else:
            final[count]=((-maxHeap[0])+minHeap[0])/2
        count+=1
    return final


print(runningMedians([1,2,3]))
print(runningMedians([5, 2, 8, 1, 9]))
print(runningMedians([]))
print(runningMedians([4]))