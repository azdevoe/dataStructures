# maxMeetingsInOneRoom: given a list of [start, end] meetings,
# return the maximum number of meetings one room can host
# (a meeting that starts exactly when another ends is allowed).
def maxMeetingsInOneRoom(meetings: list):
    count=None
    meetings.sort(key=lambda x:x[1])
    prev=None
    if meetings:
        prev=meetings[0][1]
        count=1
    for start,end in meetings:
        if start>=prev:
            count+=1
            prev=end
    return 0 if count is None else count


print(maxMeetingsInOneRoom([[1, 3], [2, 4], [3, 5]]))      # expected: 2
print(maxMeetingsInOneRoom([[1, 6], [5, 8], [7, 12]]))     # expected: 2
print(maxMeetingsInOneRoom([[1, 10], [2, 3], [4, 5]]))     # expected: 2
print(maxMeetingsInOneRoom([[5, 6], [1, 2], [3, 4]]))      # expected: 3
print(maxMeetingsInOneRoom([]))                            # expected: 0
print(maxMeetingsInOneRoom([[1, 2], [1, 2], [1, 2]]))      # expected: 1
print(maxMeetingsInOneRoom([[1, 2], [2, 10], [3, 4]]))   # expected: 2