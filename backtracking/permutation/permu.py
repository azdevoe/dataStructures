def permu(arr):
    res=[]
    path=[]
    visited=set()
    def backtrack():
        if len(path)==len(arr):
            res.append(path[:])
            return
        for i in range(len(arr)):
            if i not in visited:
                path.append(arr[i])
                visited.add(i)
                backtrack()
                path.pop()
                visited.remove(i)
    backtrack()
    return res

print(permu([1,2,3]))