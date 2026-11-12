# mergeBusyTimes:
# You get a list of busy blocks on a calendar, each one is [start, end].
# The list is NOT sorted, and blocks can overlap.
# Touching counts as overlap, so [1,3] and [3,5] become [1,5].
# Return a new list of blocks with all overlapping ones merged.
def mergeBusyTimes(blocks):
    blocks.sort(key=lambda x:x[0])
    final=[]
    last=None
    for start,end in blocks:
        if not final:
            final.append([start,end])
            last=end
        else:
            if start<=last:
                final[-1][1] = max(last,end)
                last=max(last,end)
            else:
                final.append([start,end])
                last=end
    return final
print(mergeBusyTimes([[1,3],[2,4],[5,7],[6,8]]))
print(mergeBusyTimes([]))