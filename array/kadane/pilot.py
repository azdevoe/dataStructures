def kadane(arr):
    best=arr[0]
    curr=0
    for num in arr:
        curr=max(curr,0)
        curr+=num
        best=max(best,curr)
    return best
print(kadane([4,-1,2,-7,3,5,-2]))
print(kadane([-5,-2,-8]))