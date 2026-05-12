def reverse(arr, index):
    if index==0:
        return [arr[0]]
    return [arr[index]]+reverse(arr,index-1)

arr=[1, 2, 3, 4, 5]
print(reverse(arr,4))
print(arr)
    