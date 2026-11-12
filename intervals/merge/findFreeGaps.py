# findFreeGaps:
# You get a list of busy blocks on a calendar, each one is [start, end].
# The list is NOT sorted, and blocks can overlap or touch.
# Return the free gaps BETWEEN busy blocks, as [start, end] pairs.
# Ignore time before the first block and after the last one.
def findFreeGaps(blocks):
    blocks.sort(key = lambda x : x[0])
    checker=[]
    final=[]
    for start,end in blocks:
        if not checker:
            checker.append([start,end])
        else:
            if start<=checker[0][1]:
                checker[0]=[min(checker[0][0],start),max(end,checker[0][1])]
            else:
                final.append([checker[0][1],start])
                checker[0]=[start,end]
    return final
                
print(findFreeGaps([[1,10],[2,4],[6,8]]))