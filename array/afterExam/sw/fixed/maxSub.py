def maxSub(arr,size):#this is to find the maximum subarray of an array
    start= 0
    final = 0
    curr=0
    for end in range(len(arr)):
        curr+=arr[end]
        if end-start>=size:
            curr-=arr[start]
            start+=1
        final = max(final,curr)
    return final

def maxAvg(arr,k):#this si to find the maximum subarray average
    start = 0
    final=float("-inf")
    curr=0
    for end in range(len(arr)):
        curr+=arr[end]
        curr = curr
        if end-start>=k:
            curr-=arr[start]
            start+=1
        if end-start+1 == k:
            final = max(final,curr)
        
    return final/k

print(maxAvg([4, 2, 1, 7, 8, 1, 2, 8, 1, 0],4))
print(maxAvg([-5, -2, -8],2))