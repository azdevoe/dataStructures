def combinationSum(arr,target):
    path=[]
    res=[]
    def backtrack(start):
        if sum(path)>target:return
        if sum(path)==target:
            res.append(path[:])
            return
        for i in range(start,len(arr)):
            path.append(arr[i])
            backtrack(i)
            path.pop()
    backtrack(0)
    return res
print(combinationSum([2,3],6))