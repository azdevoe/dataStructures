# insertBooking:
# You get a list of booked blocks, each [start, end].
# The list is already sorted by start, and no blocks overlap.
# You also get one new booking.
# Add it to the list, merging it with any blocks it overlaps or touches.
# Return the new list, still sorted.
def insertBooking(blocks, new_block):
    final=[]
    rf=[]
    for i in range(len(blocks)):
        if new_block[0]<=blocks[i][1]:
            final[-1]=[blocks[i][0],max(new_block[1],blocks[i][1])]
        else:
            final.append([blocks[i][0],blocks[i][1]])
    return final

print(insertBooking([[1,2],[3,5],[6,7],[8,10]],[4,8]))
            
            
#blocks=[[1,2],[3,5],[6,7],[8,10]], new=[4,8] -> [[1,2],[3,10]]