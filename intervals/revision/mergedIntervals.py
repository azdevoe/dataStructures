# mergeIntervals: merge all overlapping intervals into fewer intervals
# example: mergeIntervals([[1,3],[2,6],[8,10]]) -> [[1,6],[8,10]]
# edge case: mergeIntervals([[1,4],[4,5]]) -> [[1,5]]  (touching counts as overlapping)
def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    final=[]
    prev=None
    for start,end in intervals:
        if prev is None:
            final.append([start,end])
            prev=end
        else:
            if start<=prev:
                if end > prev:
                    final[-1][1]=end
            else:
                final.append([start,end])
        prev=max(prev,end)
    return final
print(mergeIntervals([[1,3],[2,6],[8,10]]))
print(mergeIntervals([[1,4],[4,5]]))
print(mergeIntervals([[1,10],[2,3]]))        # should be [[1,10]]
print(mergeIntervals([[1,2],[5,8],[6,7]]))   # should be [[1,2],[5,8]]
print(mergeIntervals([[1,10],[2,3],[4,5]]))   # should be [[1,10]]
print(mergeIntervals([[-3,0],[0,2]]))