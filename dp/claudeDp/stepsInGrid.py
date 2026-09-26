def steps(m,n,memo):
    if m<1 or n<1:return 0
    if m==1 and n==1:
        return 1
    if (m,n) in memo: return memo[(m,n)]
    left=steps(m,n-1,memo)
    down=steps(m-1,n,memo)
    memo[(m,n)]=left+down
    return memo[(m,n)]

print(steps(4,7,{}))