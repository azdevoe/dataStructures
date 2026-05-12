def maximum(arr, index):
    if index<0:
        return 0
    return max(arr[index],maximum(arr,index-1))
print(maximum([3, 7, 1, 9, 2],4))