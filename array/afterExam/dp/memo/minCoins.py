def minCoins(target,arr,memo={}):
    if target in memo: 
        if memo[target]==float("inf"):
            return -1
        return memo[target]
    if target <= 0:
        return 0
    minn=float("inf")
    for num in arr:
        minn =min(minn, 1+minCoins(target-num,arr))
    memo[target]=minn
    return memo[target]
print(minCoins(4,[1,2,3]))

#this might be wrong redo later with helper function