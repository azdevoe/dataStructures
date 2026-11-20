def mergeIntervals(arr:list):
    arr.sort(key=lambda x:x[0])
    final=[]
    last = None
    if arr:
        final.append(arr[0])
    for start,end in arr[1:]:
        last=final[-1][1]
        if start<=last:
            final[-1][1]=max(end,last)
            last=end
        else:
            final.append([start,end])
    
    return final
        
arr=[[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeIntervals(arr))