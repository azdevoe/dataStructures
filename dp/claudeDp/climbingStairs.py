def climbingStairs(n,memo):
    if n<0:return 0
    if n == 0:return 1
    if n in memo: return memo[n]
    left=climbingStairs(n-1,memo)
    right=climbingStairs(n-2,memo)
    memo[n]=left+right
    return memo[n]

def climbing3(n,memo):
    if n<0:return 0
    if n == 0: return 1
    if n in memo: return memo[n]
    un=climbing3(n-1,memo)
    deux=climbing3(n-2,memo)
    trois=climbing3(n-3,memo)
    memo[n]=un+deux+trois
    return memo[n]
print(climbing3(50,{}))