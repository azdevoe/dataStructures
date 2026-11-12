import heapq
def meetingRoom(arr):
    #we are supposed to count the number of meeting rooms being used
    arr.sort( key=lambda k: k[0])
    heap=[]
    for startT,endT in arr:
        if not heap:
            heap.append(endT)
        else:
            if startT<heap[0]:
                heapq.heappush(heap,endT)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,endT)
    return len(heap)

print(meetingRoom([[8,10],[9,11],[14,15]]))