def flatten(arr,result):
    if len(arr)==0:
        return result
    if type(arr[0]) == list:
        flatten(arr[0],result)
    else:
        result.append(arr[0])
    return flatten(arr[1:],result)

print(flatten([1, [2, 3], [4, [5, 6]]],[]))