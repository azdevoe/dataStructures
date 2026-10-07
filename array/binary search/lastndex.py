def lastIndex(ids, target):
    # ids is sorted ascending and may contain duplicates
    # return the index of the LAST occurrence of target, or -1 if absent
    left,right=0,len(ids)
    answer=-1
    while left<right:
        mid=left+(right-left)//2
        if ids[mid]<target:
            left=mid+1
        elif ids[mid]>target:
            right=mid
        else:
            answer=mid
            left=mid+1
    return answer

lastIndex([1, 2, 2, 2, 3], 2)    #3
lastIndex([1, 2, 2, 2, 3], 5)   # -1
lastIndex([2, 2, 2, 2, 2], 2)  #  4