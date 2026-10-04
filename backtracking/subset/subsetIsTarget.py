def isTarget(arr,target):
    def backtrack(i,total):
        if i==len(arr):
            return True if total==0 else False
        a=backtrack(i+1,total-arr[i])
        b=backtrack(i+1,total)
        return a or b
    return backtrack(0,target)
    
print(isTarget([1,2],5))
print(isTarget([1,2,3],3))