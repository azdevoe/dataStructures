def same(arrs):
    arr=sorted(arrs)
    res=[]
    path=[]
    visited=set()
    def backtrack():
        if len(arr)==len(path):
            res.append(path[:])
            return
        for i in range(len(arr)):
            if i not in visited:
                if i>0 and arr[i]==arr[i-1] and (i-1) not in visited:
                    continue
                path.append(arr[i])
                visited.add(i)
                backtrack()
                path.pop()
                visited.remove(i)
    backtrack()
    return res
print(same([1,1,2]))
print(same([1, 1, 2, 2]))