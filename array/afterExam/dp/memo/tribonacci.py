def trib(n,memo={}):
    if n in memo:return memo[n]
    if n<2:return 0
    if n == 2: return 1
    memo[n]= trib(n-1)+trib(n-2)+trib(n-3)
    return memo[n]
print(trib(100))