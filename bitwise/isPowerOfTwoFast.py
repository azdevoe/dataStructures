def is_power_of_two_fast(n: int) -> bool:
    # Return True if n is one of 1, 2, 4, 8, 16, ...
    # Use n & (n - 1). No loop. Watch out for n = 0.
    if n==0:return False
    return n&(n-1)==0


print(is_power_of_two_fast(8))    # expect True
print(is_power_of_two_fast(1))    # expect True
print(is_power_of_two_fast(16))   # expect True
print(is_power_of_two_fast(6))    # expect False
print(is_power_of_two_fast(5))    # expect False
print(is_power_of_two_fast(0))    # expect False