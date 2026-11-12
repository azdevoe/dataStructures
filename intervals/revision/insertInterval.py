# insertInterval: insert one new interval into a list of intervals, merging any overlaps
# example: insertInterval([[1,3],[6,9]], [2,5]) -> [[1,5],[6,9]]
# edge case: insertInterval([[1,2],[3,4]], [0,10]) -> [[0,10]]  (new one swallows everything)
def insertInterval(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key= lambda x:x[0])
    final=[]
    final.append(intervals[0])
    for start,end in intervals[1:]:
        prev=final[-1][1]
        if start<=prev:
            final[-1][1]=max(prev,end)
        else:
            final.append([start,end])
    return final

print(insertInterval([[1,3],[6,9]], [2,5]))
print(insertInterval([[1,2],[3,4]], [0,10]))