def stringPerm(s):
    arr=list(s)
    res=[]
    path=[]
    visited=set()
    def backtrack():
        if len(path)==len(arr):
            res.append("".join(path))
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
print(stringPerm("abc"))