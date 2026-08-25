def canSum(target,arr,mapp):
    if target in mapp: return mapp[target]
    if target ==0: return True
    if target <0: return False
    for i in range(len(arr)):
        yy = canSum(target - arr[i],arr,mapp)
        mapp[target] = yy
        if yy: return True
    return False

print(canSum(300,[14,7],{}))