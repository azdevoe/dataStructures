def searchInsertPosition(ids, target):
    # ids is sorted ascending, unique values
    # return the index where target is, or where it would be inserted to keep ids sorted
    left,right=0,len(ids)
    while left<right:
        mid=left+(right-left)//2
        if ids[mid]<target:
            left=mid+1
        else:
            right=mid
    return right
print(searchInsertPosition([1, 3, 6, 8], 6))        # expect 2
print(searchInsertPosition([1, 3, 6, 8], 5))        # expect 2
print(searchInsertPosition([1, 3, 6, 8], 0))        # expect 0
print(searchInsertPosition([1, 3, 6, 8], 100))      # expect 4
print(searchInsertPosition([1, 2, 2, 2, 3], 2))     # expect 1