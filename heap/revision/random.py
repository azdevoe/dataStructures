import heapq
# minimumTaxis: each trip is [pickup_time, dropoff_time].
# A taxi can only drive one trip at a time.
# A taxi that has dropped off a passenger can take a new trip
# starting at that same time or later.
# Return the smallest number of taxis needed to cover all the trips.

def minimumTaxis(trips):
    trips.sort(key = lambda x: x[0])
    print(trips)
    heap=[]
    for start,end in trips:
        if not heap:
            heap.append(end)
        else:
            if start<heap[0]:
                heapq.heappush(heap,end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,end)
    return len(heap)
print(minimumTaxis([[5, 9], [1, 6], [2, 3]]))
#[[1, 4], [2, 5], [6, 8]] → 2
#[[1, 3], [3, 5], [5, 7]] → 1
#[[5, 9], [1, 6], [2, 3]] → 2