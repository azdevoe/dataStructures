def maxMeetingsOneRoom(meetings: list[list[int]]) -> int:
    # meetings is a list of [start, end] requests for ONE meeting room, in any order.
    # Return the largest number of meetings the room can host with no overlap.
    # A meeting that starts exactly when another ends is allowed (no overlap).
    if not meetings: return 0
    arr=sorted(meetings,key=lambda x:x[1])
    final=[arr[0][:]]
    for start, end in arr[1:]:
        prev=final[-1][1]
        if prev<=start:
            final.append([start,end])
    return len(final)
            
    


print(maxMeetingsOneRoom([[1,3],[2,4],[3,5]]))        # expect 2
print(maxMeetingsOneRoom([[1,10],[2,3],[4,5],[6,7]])) # expect 3
print(maxMeetingsOneRoom([[1,2],[2,3],[3,4]]))        # expect 3
print(maxMeetingsOneRoom([[1,4],[2,3]]))              # expect 1
print(maxMeetingsOneRoom([[5,6]]))                    # expect 1
print(maxMeetingsOneRoom([]))                         # expect 0