def sumPossible(arr,target):
    if target<0:return False
    if target==0:
        return True
    for num in arr:
        return sumPossible(arr,target-num)
def allPossibleSum(arr,target):
    path=[]
    res=[]
    def backtrack(start):
        if sum(path)>target: return
        if sum(path)==target:
            res.append(path[:])
            return
        for i in range(start,len(arr)):
            path.append(arr[i])
            backtrack(i)
            path.pop()
    backtrack(0)
    return res
print(sumPossible([6,2,110,19],15))