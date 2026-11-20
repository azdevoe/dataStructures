def count_set_bits(n: int) -> int:
    # Count how many 1s are in the binary form of n (n >= 0).
    # Use n & 1 to read the last digit, and n >> 1 to drop it.
    # Do not use bin() or str().
    count=0
    while n:
        numb=n&1
        if numb ==1:
            count+=1
        n=n>>1
    return count

110
print(count_set_bits(6))    # expect 2  (6 is 110)
print(count_set_bits(13))   # expect 3  (13 is 1101)
print(count_set_bits(0))    # expect 0
print(count_set_bits(7))    # expect 3  (7 is 111)
print(count_set_bits(8))    # expect 1  (8 is 1000)