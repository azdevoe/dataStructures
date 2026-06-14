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
            
            
            
            
            
            
def sliding(arr,size):
    curr=start=0
    final=float("-inf")
    for end in range(len(arr)):
        curr+=arr[end]
        if end > size-2:
            final = max(final,curr)
            curr=curr-arr[start]
            start+=1
    return final

def slidingMean(arr,size):
    final=[]
    curr=start=0
    for end in range(len(arr)):
        curr+=arr[end]
        if end>=size-1:
            final.append(curr/size)
            curr=curr-arr[start]
            start+=1
    return final

def minimumSum(arr,size):
    final=float("inf")
    curr=start=0
    for end in range(len(arr)):
        curr+=arr[end]
        if end>=size-1:
            final=min(final,curr)
            curr = curr-arr[start]
            start+=1
    return final
print(minimumSum([3, 5, 2, 1, 4, 6],2))