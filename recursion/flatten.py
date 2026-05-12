def flatten(arr,index):
    if index<=0:
        if type(arr[index])!=list:
            return [arr[index]]
        else:
            return flatten(arr[index],len(arr[index])-1)
    if type(arr[index])!=list:
        return [arr[index]]+flatten(arr,index-1)
    else:
        return flatten(arr[index],len(arr[index])-1)+flatten(arr,index-1)
print(flatten([1, [2, 3], 7],2))