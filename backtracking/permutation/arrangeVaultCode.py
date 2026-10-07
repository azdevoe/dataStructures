def arrangeVaultCode(arrs, k):
    # Return every ordered arrangement of k distinct numbers from arr.
    # Order matters: [1,2] and [2,1] are different codes.
    # Each number is used at most once per code.
    # Example: arrangeVaultCode([1,2,3], 2)
    #   -> [[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]]
    path=[]
    res=[]
    visited=set()
    arr=sorted(arrs)
    
    def backtrack():
        if len(path)==k:
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

print(arrangeVaultCode([1,2,3], 2))