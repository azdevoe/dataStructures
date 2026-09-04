#this is to find the number of times a subarray sum up to the target

def subArraySumCount(arr,target,size):
    start=count=curr=0
    for end in range(len(arr)):
        curr+=arr[end]
        if curr==target and end-start+1==size:
            count+=1
        if end-start>= size:
            curr-=arr[start]
            start+=1
            if curr==target:
                count+=1
    return count

print(subArraySumCount([2,3,2,2,3,1,3,8,5,0,2,4],7,3))