def find_missing_number(nums: list[int]) -> int:
    # nums holds every number from 0 to n except one (n = len(nums)).
    # Return the missing number. Use XOR.
    final=0
    for i in range(len(nums)+1):
        final^=i
    for num in nums:
        final^=num
    return final


print(find_missing_number([0, 1, 3]))         # expect 2
print(find_missing_number([0, 2]))            # expect 1
print(find_missing_number([1, 2, 3]))         # expect 0
print(find_missing_number([0, 1, 2]))         # expect 3
print(find_missing_number([3, 0, 1, 4, 5]))   # expect 2

def simpler(nums):
    n=len(nums)
    return (n*(n+1)//2)-sum(nums)
print(simpler([0,1,2]))