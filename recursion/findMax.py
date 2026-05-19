def findMax(arr):
    def findMaxsub(arr,ind,maxe):
        if ind<0:
            return maxe
        maxe=max(maxe,arr[ind])
        return findMaxsub(arr,ind-1,maxe)
    index=len(arr)-1
    maxV=arr[index]
    answer =findMaxsub(arr,index,maxV)
    return answer

arr=[3, 7, 2, 9, 1]
print(findMax(arr))