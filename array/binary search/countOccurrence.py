def countOccurrences(ids, target):
    # ids is sorted ascending and may contain duplicates
    # return how many times target appears in ids (0 if absent)
    first = firstIndex(ids, target)
    second=lastIndex(ids,target)
    # 1) if first is -1, return what?
    return 0 if first == -1 else second-first+1
    # 2) otherwise, get last and return the count
def firstIndex(arr,target):
    answer,left,right=-1,0,len(arr)
    while left<right:
        mid=left+(right-left)//2
        if arr[mid]<target:
            left=mid+1
        elif arr[mid]>target:
            right=mid
        else:
            answer=mid
            right=mid
    return answer

def lastIndex(arr,target):
    answer,left,right=-1,0,len(arr)
    while left<right:
        mid=left+(right-left)//2
        if arr[mid]<target:
            left=mid+1
        elif arr[mid]>target:
            right=mid
        else:
            answer=mid
            left=mid+1
    return answer

print(countOccurrences([1, 2, 2, 2, 3], 2))   # expect 3
print(countOccurrences([1, 2, 2, 2, 3], 5))   # expect 0
print(countOccurrences([1, 2, 3], 2))         # expect 1