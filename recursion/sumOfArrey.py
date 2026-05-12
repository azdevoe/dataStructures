def sumOfArray(arr,index):
    if len(arr)==0:
        return arr
    if index<=0:
        return arr[0]
    return arr[index]+sumOfArray(arr,index-1)
print(sumOfArray([1, 2, 3, 4, 5],4))