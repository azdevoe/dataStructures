# mergeMeetings: each meeting is [start, end].
# Meetings that overlap or touch become one bigger meeting.
# Return the merged list, sorted by start time.

def mergeMeetings(meetings):
    meetings.sort(key=lambda x:x[0])
    last=None
    final=[]
    for start,end in meetings:
        if not final:
            final.append([start,end])
            last=end
            print(last)
        else:
            print(end,last)
            if start<=last:
                final[-1][1]=max(end,last)
                last=max(end,last)
            else:
                final.append([start,end])
                last=end
    return final
#print(mergeMeetings([[5, 6], [1, 2]]))
print(mergeMeetings([[1, 3], [2, 6], [5, 7]]))

#[[1, 3], [2, 6], [8, 10]] → [[1, 6], [8, 10]]
#[[1, 3], [3, 5]] → [[1, 5]]
#[[1, 10], [2, 3]] → [[1, 10]]
#[[5, 6], [1, 2]] → [[1, 2], [5, 6]]