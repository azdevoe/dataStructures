def fib(n,memo={}):
    if n in memo:return memo[n]
    if n<3:return 1
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]

def tabFib(n):
    ta=[1]*(n)
    for i in range(2,n):
        ta[i]= ta[i-1]+ta[i-2]
        print(ta)
    return ta[n-1]

def optimizedFibTab(n):
    if n==0: return 0
    if n<3:return 1
    first=1
    second=1
    for i in  range(2,n):
        curr=first+second
        first=second
        second=curr
    return second
print(optimizedFibTab(0))