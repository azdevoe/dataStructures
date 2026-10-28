def allValid(arr,k):
    res=[]
    path=[]
    def backTrack(left,right):
        if left>k or right>k: return
        if left == k and right == k:
            res.append(path[:])
            return 
        for i in range(k):
                path.append(arr[i])
                backTrack(i+1,i+1)
                path.pop()
    backTrack(0,0)
    return res

print(allValid(["(",")"],3))