def two(arr,target):
    l=0
    r=len(arr)-1
    while r>l:
        if arr[l]+arr[r]<target:
            l+=1
        elif arr[l]+arr[r]>target:
            r-=1
        else:
            return [l,r]
print(two([2, 7, 11, 15],9))