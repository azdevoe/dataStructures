def counteven(arr):
    if len(arr) ==0:
        return 0
    first = 1 if arr[0]%2==0 else 0
    return first+counteven(arr[1:])

print(counteven([1, 2, 3, 4, 6]))
print(counteven([1, 3, 5]))