def maxSubarraySum(nums):
    # return the biggest sum of any non-empty subarray of nums
    if not nums: return 0
    largest=nums[0]
    curr=0
    for num in nums:
        curr=max(curr,0)
        curr+=num
        largest=max(largest,curr)
    return largest

print(maxSubarraySum([2, -1, 3, -4, 5]))
print(maxSubarraySum([-3, -1, -2]))