def combination(arr,k):
    res=[]
    path=[]
    def backtrack(start):
        if k==len(path):
            res.append(path[:])
            return
        for i in range(start,len(arr)):
            path.append(arr[i])
            backtrack(i+1)
            path.pop()
    backtrack(0)
    return res

print(combination([1,2,3],2))
print(combination([1,1,2],2))