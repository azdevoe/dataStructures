def productSub(arr,size):
    final=float("-inf")
    curr=1
    start=0
    for end in range(len(arr)):
        curr*=arr[end]
        if end>=size-1:
            final=max(final,curr)
            if arr[start]==0:
                curr=1
                for i in range(start+1,end+1):
                    curr*=arr[i]
            else:
                curr=curr//arr[start]
            start+=1
    return final

print(productSub([0,4,1,6,-3,3,-5,2,26],4))
