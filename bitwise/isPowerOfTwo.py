def is_power_of_two(n: int) -> bool:
    # Return True if n is one of 1, 2, 4, 8, 16, ...
    # Use n & 1 to read the last digit and n >> 1 to drop it.
    # Do not use bin() or str().
    if n==0: return False
    while n:
        if n&1 ==1 and n!=1:
            return False
        n=n>>1
    return True


print(is_power_of_two(8))    # expect True   (1000)
print(is_power_of_two(1))    # expect True   (1)
print(is_power_of_two(16))   # expect True   (10000)
print(is_power_of_two(10))   # expect False  (1010)
print(is_power_of_two(5))    # expect False  (101)
print(is_power_of_two(6))    # expect False  (110)
print(is_power_of_two(0))    # expect False  (0 is not a power of 2)