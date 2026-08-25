def howSum(target, arr):
    if target == 0: return []
    if target<0: return []
    
    for num in arr:
        left=[target] +howSum(target-num,arr)
        if left: return left
        right =[target] + howSum(target-num,arr)
        if right: return right
        
    
print(howSum(7,[5,3,4,7]))