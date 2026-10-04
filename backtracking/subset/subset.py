def subset(arr):
    result=[]
    path=[]
    def backtrack(i):
        if i == len(arr):
            result.append(path[:])
            return 
        path.append(arr[i])
        backtrack(i+1)
        path.pop()
        backtrack(i+1)
    backtrack(0)
    return result

def anotherSubset(arr):
    result=[]
    path=[]
    def backtrack(i):
        if i == len(arr):
            result.append(path[:])
            return
        path.append(arr[i])
        backtrack(i+1)
        path.pop()
        backtrack(i+1)
    backtrack(0)
    return result
print(anotherSubset([1,2,3]))