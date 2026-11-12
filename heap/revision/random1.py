import heapq
# assignTaxis: each trip is [pickup_time, dropoff_time].
# A taxi can only drive one trip at a time, and a taxi that has
# dropped off can take a trip that starts at that same time or later.
# Taxis are numbered 1, 2, 3... in the order they are first used.
# Rule: if a taxi is free, reuse the one that freed up first.
# Otherwise bring in a new taxi with the next number.
# Return a list with the taxi number for each trip,
# in the order of the trips after sorting them by pickup time.

def assignTaxis(trips):
    trips.sort(key=lambda x:x[0])
    print(trips)
    heap=[]
    final=[]
    for start,end in trips:
        if not heap:
            heap.append((end,1))
            final.append(1)
            print(heap)
        else:
            if start<heap[0][0]:
                tt=len(heap)
                print("i am",tt)
                heapq.heappush(heap,(end,tt+1))
                final.append(tt+1)
                print(heap)
                print("it entered the secone conditon")
            else:
                tt=heapq.heappop(heap)
                print(tt)
                heapq.heappush(heap,(end,tt[1]))
                final.append(tt[1])
    return final
print(assignTaxis([[1, 2], [1, 3], [2, 4], [3, 5]]))
    
#[[1, 4], [2, 5], [6, 8]] → [1, 2, 1]
#[[1, 3], [3, 5], [5, 7]] → [1, 1, 1]
#[[1, 2], [1, 3], [2, 4], [3, 5]] → [1, 2, 1, 2]