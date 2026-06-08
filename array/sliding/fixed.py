def sliding(arr,size):
    final=float("-inf")
    curr=0
    start=0
    for i in range(len(arr)):
        curr=curr+arr[i]
        if i>size-2:
            final=max(final,curr)
            curr=curr-arr[start]
            start+=1
    return final
            
print(sliding([2, 1, 5, 1, 3, 2],3))