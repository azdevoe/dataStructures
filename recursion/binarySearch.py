def binary(arr,target,l,r):
    mid=l+(r-l)//2
    if r<l: return -1
    if arr[mid]==target:return mid
    elif arr[mid]>target:
        return binary(arr,target,l,mid-1)
    else:
        return binary(arr,target,mid+1,r)
arr=[1,2,3,4,5,6,7,8,9,10]
print(binary(arr,11,0,len(arr)-1))


    # left=0
    # right=len(arr)-1
    # while left<=right:
    #     mid=left+(right-left)//2
    #     if arr[mid]==target:
    #         return mid
    #     if arr[mid]>target:
    #         right=mid-1
    #     else:
    #         left=mid+1
    # return -1