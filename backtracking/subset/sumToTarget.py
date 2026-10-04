def sumToCount(arr,target):
    result=[]
    path=[]
    def backtrack(i):
        if i==len(arr):
            if sum(path)==target:
                result.append(path[:])
            return
        path.append(arr[i])
        backtrack(i+1)
        path.pop()
        backtrack(i+1)
    backtrack(0)
    return result

print(sumToCount([1,2,3,4],4))