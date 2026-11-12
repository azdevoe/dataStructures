# minMeetingsToCancel: given a list of [start, end] meetings,
# return the fewest meetings you must cancel so that no two overlap
# (a meeting that starts exactly when another ends is allowed).
def minMeetingsToCancel(meetings:list):
    count=None
    prev=None
    meetings.sort(key=lambda x:x[1])
    if meetings:
        count=1
        prev=meetings[0][1]
    for start,end in meetings[1:]:
        if start>=prev:
            count+=1
            prev = end
    if count is None:
        count=0
    return len(meetings)-count


print(minMeetingsToCancel([[1, 2], [2, 3], [3, 4], [1, 3]]))   # expected: 1
print(minMeetingsToCancel([[1, 2], [1, 2], [1, 2]]))           # expected: 2
print(minMeetingsToCancel([[1, 2], [2, 3]]))                   # expected: 0
print(minMeetingsToCancel([[1, 10], [2, 3], [4, 5]]))          # expected: 1
print(minMeetingsToCancel([[1, 6], [5, 8], [7, 12]]))          # expected: 1
print(minMeetingsToCancel([]))                                 # expected: 0
