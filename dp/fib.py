def fib(n,mapp):
    if n in mapp:
        return mapp[n]
    if n<=2:
        return 1
    mapp[n]=fib(n-2,mapp)+fib(n-1,mapp)
    return mapp[n]

print(fib(50,{}))