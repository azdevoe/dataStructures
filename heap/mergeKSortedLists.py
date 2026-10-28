import heapq

def mergeKSortedLists(lists):
    # Takes a list of sorted lists, returns one sorted list with all the values
    heapp=[]
    final=[]
    for i in range(len(lists)):
        if not lists[i]: continue
        heapq.heappush(heapp,(lists[i][0],i,0))
    
    while heapp:
        node,currArr,pointer=heapq.heappop(heapp)
        final.append(node)
        if pointer<len(lists[currArr])-1:
            heapq.heappush(heapp,(lists[currArr][pointer+1],currArr,pointer+1))
    return final

print(mergeKSortedLists([[1, 4, 9],[2, 3, 8],[5, 6, 7]]))
print(mergeKSortedLists([[1, 2], [], [3]]))