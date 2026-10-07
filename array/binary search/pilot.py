def findUserById(ids, target,left,right):
    # ids is a sorted list of unique user ids (ascending)
    # return the index of target in ids, or -1 if it isn't there
    if left>=right: return -1
    mid=left+((right-left)//2)
    if ids[mid]>target: 
        return findUserById(ids,target,left,mid)
    elif ids[mid]<target:
        return findUserById(ids,target,mid+1,right)
    else: return mid
    
    
def loopBin(arr,target):
    left=0
    right=len(arr)
    while right-left>=1:
        mid=left+(right-left)//2
        if arr[mid]>target:
            right=mid
        elif arr[mid]<target:
            left=mid+1
        else:
            return mid
    return -1
id=[3, 8, 15, 22, 41, 57, 90]
print(findUserById(id, 41,0,len(id)))
print(findUserById(id, 10,0,len(id)))
print(findUserById(id, 3,0,len(id)))    # first element, expect 0
print(findUserById(id, 90,0,len(id)))