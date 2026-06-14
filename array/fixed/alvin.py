def sliding(arr,size):
    maximum= float("-inf")
    start=curr=0
    if not arr or size >len(arr):
        return None
    for end in range(len(arr)):
        curr+=arr[end]
        if end >= size-1:
            maximum=max(maximum,curr)
            curr=curr-arr[start]
            start+=1
    return maximum
print(sliding([4,2,1,-9,8,43],3))