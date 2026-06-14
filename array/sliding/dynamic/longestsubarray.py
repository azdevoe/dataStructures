def longestSub(arr,target):
    curr=start=0
    count=0
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>target and start<end:
            curr-=arr[start]
            start+=1
        if curr==target:
            count=max(count,end-start+1)
    return count
print(longestSub([4,3,3,2,1,5,2,3,5,10,1],10))