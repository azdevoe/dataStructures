def fibonacci(n):
    if n<=2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)


print(fibonacci(50))

