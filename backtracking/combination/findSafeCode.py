def findSafeCode(k, target):
    # Return every set of k DIFFERENT digits from 1 to 9 that add up to target.
    # Order doesn't matter: [1,2,4] and [4,2,1] are the same set.
    # Each digit can be used at most once.
    # Example: findSafeCode(3, 7)
    #   -> [[1,2,4]]
    path=[]
    res=[]
    def backTrack(start,total):
        if len(path)==k:
            if total==target:
                res.append(path[:])
            return
        for i in range(start,10):
            path.append(i)
            backTrack(i+1,total+i)
            path.pop()
    backTrack(1,0)
    return res

print(findSafeCode(3, 7))