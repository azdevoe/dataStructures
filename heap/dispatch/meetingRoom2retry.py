import heapq
def meetingRoom(arr):
    arr.sort(key=lambda x:x[0])
    heap=[]
    for start,end in arr:
        if heap and start>=heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap,end)
    return len(heap)

print(meetingRoom([[8,10],[9,11],[14,15]]))



