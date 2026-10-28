import heapq
def kSmallest(arr,k):
    if not arr or  k > len(arr) or k<1:
        return None
    heap=[]
    for num in arr:
        heapq.heappush(heap,-num)
        if len(heap)>k:
            heapq.heappop(heap)
    return -heap[0]
print(kSmallest([5, 1, 9, 3, 7], 2))