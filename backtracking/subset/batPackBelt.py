def packBatBelt(gadgets):
    # Return every possible subset of gadgets Batman could carry,
    # including carrying nothing and carrying everything.
    # Example: packBatBelt([1,2,3])
    #   -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    res=[]
    path=[]
    def backtrack(i):
        if i == len(gadgets):
            res.append(path[:])
            return
        path.append(gadgets[i])
        backtrack(i+1)
        path.pop()
        backtrack(i+1)
    backtrack(0)
    return res

print(packBatBelt([1,2,3]))