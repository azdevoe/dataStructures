import heapq

# kthSmallestInSortedLists: return the k-th smallest number across all the
# sorted lists, without building the full merged list
# example: kthSmallestInSortedLists([[1, 4], [2, 5], [3, 6]], 4) -> 4
# (merged order is 1,2,3,4,5,6 so the 4th is 4)
# edge case: kthSmallestInSortedLists([[1, 2], [], [3]], 3) -> 3
def kthSmallestInSortedLists(lists, k):
    total=0
    for i in range(len(lists)):
        total+=len(lists[i])
    if k<1 or k>total:
        return None
    final=[]
    ik=0
    heap=[]
    for i in range(len(lists)):
        if not lists[i]: continue
        heapq.heappush(heap,(lists[i][0],i,0))
    while ik<k:
        num,currArr,index=heapq.heappop(heap)
        ik+=1
        final.append(num)
        if index+1 < len(lists[currArr]):
            heapq.heappush(heap,(lists[currArr][index+1],currArr,index+1))
    print(final)
    return final[-1]

print(kthSmallestInSortedLists([[1, 4], [2, 5], [3, 6]], 4))
print(kthSmallestInSortedLists([[1, 2], [], [3]], 3))