def longestConsecutiveRun(nums):
    if not nums: return 0
    arr=sorted(nums)
    best=1
    curr=1
    for i in range(1,len(nums)):
        if arr[i-1]==arr[i]-1:
            curr+=1
            best=max(best,curr)
        elif arr[i-1]==arr[i]:
            continue
        else:
            curr=1
    return best

print(longestConsecutiveRun([100, 4, 200, 1, 3, 2]))
print(longestConsecutiveRun([1, 2, 2, 3, 10]))
print(longestConsecutiveRun([5]))
print(longestConsecutiveRun([7, 7, 7]))