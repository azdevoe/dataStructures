def decimalSquareRoot(n):
    # n >= 0
    # return the square root of n, correct to 6 decimal places
    left, right = 0, n+1
    # your loop here
    while right-left>0.0000001:
        mid=left+(right-left)/2
        if mid**2<n:
            left=mid
        elif mid**2>n:
            right=mid
        else:
            return mid
    return mid

print(round(decimalSquareRoot(50), 6))   # expect 7.071068
print(round(decimalSquareRoot(2), 6))    # expect 1.414214
print(decimalSquareRoot(1))
print(round(decimalSquareRoot(0), 6))      # expect 0.0
print(round(decimalSquareRoot(0.25), 6))   # expect 0.5