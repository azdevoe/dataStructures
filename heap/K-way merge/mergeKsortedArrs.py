import heapq

# mergeKSortedLists: merge k sorted lists into one sorted list using a heap
# example: mergeKSortedLists([[1, 4], [2, 5], [3, 6]]) -> [1, 2, 3, 4, 5, 6]
# edge case to handle: mergeKSortedLists([[1, 2], [], [3]]) -> [1, 2, 3]
def mergeKSortedLists(lists):
    heap=[]
    final=[]
    for i in range(len(lists)):
        if not lists[i] : continue
        heapq.heappush(heap,(lists[i][0],i,0))
    while heap:
        num,listNumber,ind = heapq.heappop(heap)
        final.append(num)
        if ind+1 < len(lists[listNumber]):
            heapq.heappush(heap,(lists[listNumber][ind+1],listNumber,ind+1))
        
    return final

print(mergeKSortedLists([[1, 4], [2, 5], [3, 6]]))
print(mergeKSortedLists([[1, 2], [], [3]]))