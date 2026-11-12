# insertIntervalLinear: given a sorted list of non-overlapping intervals
# and one new interval, return the new sorted list with the new interval
# inserted and merged. Must go through the list once, O(n).
def insertIntervalLinear(intervals, new):
    final=[]
    merged=False
    # if not intervals: final.append(new)
    for start, end in intervals:
        if end<new[0]:
            final.append([start,end])
        elif new[1]<start:
            if not merged:
                final.append(new)
            final.append([start,end])
            merged=True
        else:
            [new[0],new[1]]=[min(start,new[0]),max(end,new[1])]
    if not merged:
        final.append(new)
    return final


print(insertIntervalLinear([[1,3],[5,6],[7,9],[12,14]], [6,8]))
# expected: [[1,3],[5,9],[12,14]]

print(insertIntervalLinear([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# expected: [[1,2],[3,10],[12,16]]

print(insertIntervalLinear([], [2,5]))
# expected: [[2,5]]

print(insertIntervalLinear([[1,2],[3,4]], [6,7]))
# expected: [[1,2],[3,4],[6,7]]

print(insertIntervalLinear([[5,6]], [1,2]))
# expected: [[1,2],[5,6]]

print(insertIntervalLinear([[1,2],[6,7],[9,10]], [4,5]))
# expected: [[1,2],[4,5],[6,7],[9,10]]