def longestWindow(arr,target):
    start=curr=0
    maxLength=0
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>target:
            curr-=arr[start]
            start+=1
        maxLength=max(maxLength,end-start+1)
    return -1 if maxLength==0 else maxLength

print(longestWindow([4,3,3,2,1,5,2,3,5,10,1],10))