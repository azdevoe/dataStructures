def combination(arr,k):
    res=[]
    path=[]
    def backTrack(start):
        if k == len(path):
            res.append(path[:])
            return
        for i in range(start,len(arr)):
            if i>start and arr[i]==arr[i-1]:continue
            path.append(arr[i])
            backTrack(i+1)
            path.pop()
    backTrack(0)
    return res

print(combination([1,1],2))