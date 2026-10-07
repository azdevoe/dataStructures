def pickTwoTeammates(arrs, k):
    # Return every way to pick k numbers from arr.
    # Order doesn't matter: [1,2] and [2,1] count as the same pick.
    # Example: pickTwoTeammates([1,2,3,4], 2)
    #   -> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    arr=sorted(arrs)
    path=[]
    res=[]
    def backtrack(start):
        if len(path)==k:
            res.append(path[:])
            return
        for i in range(start,len(arr)):
            if i > start and arr[i]==arr[i-1]: continue
            path.append(arr[i])
            backtrack(i+1)
            path.pop()
    backtrack(0)
    return res

print(pickTwoTeammates([1,2,3,4], 2))