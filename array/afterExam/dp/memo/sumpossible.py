def sumPossible(target,arr,memo={}):
    if target in memo: return memo[target]
    if target<0: return False
    if target == 0: return True
    for num in arr:
        memo[target]=  sumPossible(target-num,arr,memo)
    return memo[target]

print(sumPossible(271,[10,0,265,24]))