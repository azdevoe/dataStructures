# insertMeeting: busy is a list of [start, end] blocks that is ALREADY
# sorted and has no overlaps. new_block is one new [start, end].
# Insert it, merge anything it overlaps (touching counts),
# and return the new list. Do NOT sort.

def insertMeeting(busy, new_block):
    final=[]
    placed=False
    if not busy:
        final.append(new_block)
        placed=True
    for start,end in busy:
        if not placed and start>new_block[0]:
            final.append(new_block)
            placed=True
        final.append([start,end])
    if not placed:
        final.append(new_block)
        placed=True
    return merger(final)


def merger(blocks):
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
print(insertMeeting([[1,2],[5,6]], [7,8]))
#[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] → [[1,2],[3,10],[12,16]]
#[[1,3],[6,9]], [2,5] → [[1,5],[6,9]]
#[], [5,7] → [[5,7]]
#[[1,2],[5,6]], [3,4] → [[1,2],[3,4],[5,6]]
#[[1,2],[5,6]], [7,8] → [[1,2],[5,6],[7,8]]