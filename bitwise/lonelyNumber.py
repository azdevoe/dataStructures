def find_lonely_number(nums: list[int]) -> int:
    # Every number in nums appears exactly twice, except one number
    # that appears once. Return that lonely number.
    # Use XOR (^). Do not use a dictionary or a set.
    final=0
    for num in nums:
        final=final^num
    return final


print(find_lonely_number([4, 6, 4, 9, 6]))  # expect 9
print(find_lonely_number([2, 5, 2, 5, 7]))  # expect 7
print(find_lonely_number([8]))              # expect 8
print(find_lonely_number([1, 3, 1, 3, 10, 3, 3]))  # expect 10