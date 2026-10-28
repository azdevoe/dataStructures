import heapq

# mergeKUnique: merge k sorted lists into one sorted list using a heap,
# but each number appears only once in the result
# example: mergeKUnique([[1, 2, 2], [2, 3], [1, 4]]) -> [1, 2, 3, 4]
# edge case: mergeKUnique([[5, 5], [], [5]]) -> [5]
def mergeKUnique(lists):
    final,heap=[],[]
    prev=None
    for i in range(len(lists)):
        if not lists[i]:continue
        heapq.heappush(heap,(lists[i][0],i,0))
    while heap:
        num,currList,index=heapq.heappop(heap)
        if num != prev:
            final.append(num)
            prev=num
        if index+1<len(lists[currList]):
            heapq.heappush(heap,(lists[currList][index+1],currList,index+1))
    return final
print(mergeKUnique([[1, 2, 2], [2, 3], [1, 4]]))
print(mergeKUnique([[5, 5], [], [5]]))