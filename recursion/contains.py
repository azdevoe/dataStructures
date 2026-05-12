def contains(arr, index, target):
    if index == 0:
        return arr[index]==target
    return arr[index]==target or contains(arr,index-1,target)
print(contains([1, 4, 7, 2, 9],4,7))