import heapq

# mergeKDescending: merge k lists that are sorted from biggest to smallest
# into one list sorted from biggest to smallest, using a heap
# example: mergeKDescending([[6, 3], [5, 2], [4, 1]]) -> [6, 5, 4, 3, 2, 1]
# edge case: mergeKDescending([[9, 4], [], [7]]) -> [9, 7, 4]
def mergeKDescending(lists):
    heap=[]
    final=[]
    for i in range(len(lists)):
        if not lists[i]:continue
        heapq.heappush(heap,(-lists[i][0],i,0))
    while heap:
        num,currList,index = heapq.heappop(heap)
        final.append(-num)
        if index+1<len(lists[currList]):
            heapq.heappush(heap,(-lists[currList][index+1],currList,index+1))
    return final

print(mergeKDescending([[6, 3], [5, 2], [4, 1]]))