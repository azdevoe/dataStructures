import heapq
def meetingRoom(arr):
    arr.sort(key=lambda x: x[0])
    print(arr)
    heap=[]
    for startT,endTime in arr:
        if not heap:
            heapq.heappush(heap,endTime)
        else:
            if startT<heap[0]:
                return False
            heapq.heappop(heap)
            heapq.heappush(heap,endTime)
    return True
print(meetingRoom([[0, 30], [5, 10], [15, 20]]))
print(meetingRoom([[7, 10], [2, 4]]))
print(meetingRoom([[1, 3], [4, 6], [5, 7]]))