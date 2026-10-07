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

def optimizedCombinationSum(arr,target):
    path=[]
    res=[]
    arr.sort()
    def backtrack(start,total):
        if total>target:return
        if target==total:
            res.append(path[:])
            return
        for i in range(start,len(arr)):
            if i>start and arr[i]==arr[i-1]: continue
            path.append(arr[i])
            backtrack(i+1,total+arr[i])
            path.pop()
    backtrack(0,0)
    return res
print(optimizedCombinationSum([2,3],6))
print(optimizedCombinationSum([1,1,2],3))