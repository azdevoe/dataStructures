def fibonacci(n:int,memo={}):
    if n in memo:return memo[n]
    if n <2:
        return n
    memo[n]=fibonacci(n-1)+fibonacci(n-2)
    return memo[n]

print(fibonacci(50))