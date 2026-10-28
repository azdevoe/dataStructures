import heapq
def topK(arr,k):
    if not arr or k>len(arr):
        return None
    heap = []
    for num in arr:
        heapq.heappush(heap,num)
        if len(heap)>k:
            heapq.heappop(heap)
    return heap[0]

print(topK([5, 1, 9, 3, 7],3))