def insertInterval(arr:list,new:list):
    final=[]
    merged=False
    for start,end in arr:
        if end<new[0]:
            final.append([start,end])
        elif new[1]<start:
            if not merged:
                final.append(new)
                merged=True
            final.append([start,end])
        else:
            new[0]=min(new[0],start)
            new[1]=max(new[1],end)
    if not merged:
        final.append(new)
    return final
            
print(insertInterval([[1, 3], [6, 9]], [2, 5]))
print(insertInterval([[3, 5], [8, 10]], [1, 2]))