def smallestSubArray(arr,target):
    start=0
    final=float("inf")
    curr=0
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>=target:
            final = min(final,end-start+1)
            curr-=arr[start]
            start+=1
    return 0 if final == float("inf") else final
print(smallestSubArray([2,1,5,2,3,2],7))
