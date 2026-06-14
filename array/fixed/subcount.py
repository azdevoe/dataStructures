def subCount(arr,target,size):
    curr=start=0
    count=0
    for end in range(len(arr)):
        curr+=arr[end]
        if end>=size-1:
            if curr==target:count+=1
            curr=curr-arr[start]
            start+=1
    return count

print(subCount([2,3,2,2,3,1,3,8,5,0,2,4],7,3))