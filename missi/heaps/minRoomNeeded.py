import heapq

# minRoomsNeeded: given a list of meetings [start, end],
# return the smallest number of rooms so that no two
# overlapping meetings share a room.
def minRoomsNeeded(meetings:list):
    # your code here
    meetings.sort(key=lambda x: x[0])
    final=[]
    for start,end in meetings:
        if not final:
            final.append(end)
        else:
            if start<final[0]:
                heapq.heappush(final,end)
            else:
                heapq.heappop(final)
                heapq.heappush(final,end)
    return len(final)


# Tests
print(minRoomsNeeded([[0, 30], [5, 10], [15, 20]]))      # expect 2
print(minRoomsNeeded([[7, 10], [2, 4]]))                 # expect 1
print(minRoomsNeeded([[14, 15], [8, 10], [9, 11]]))      # expect 2
print(minRoomsNeeded([[1, 5], [2, 6], [3, 7], [4, 8]]))  # expect 4
print(minRoomsNeeded([]))                                # expect 0