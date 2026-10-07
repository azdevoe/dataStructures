def floorKthRoot(n, k):
    # n >= 0, k >= 1
    # return the largest whole number x such that x ** k <= n
    left,right=0,n+1
    while left<right:
        mid=left+(right-left)//2
        if (mid**k) < n:
            left=mid+1
        elif (mid**k)>n:
            right=mid
        else:
            return mid
    return left-1
print(floorKthRoot(64, 2))  # ->  8
print(floorKthRoot(343, 3))  #->  7
print(floorKthRoot(50, 2))  # ->  7
print(floorKthRoot(100, 3))  #->  4    (4*4*4=64 fits, 5*5*5=125 is too big)
print(floorKthRoot(0, 2)) 
print(floorKthRoot(1, 3))