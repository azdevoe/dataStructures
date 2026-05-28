def subsets(arr, current, result):
    result.append(current[:])
    for i in range(len(arr)):
        current.append(arr[i])
        subsets(arr[i+1:],current,result)
        current.pop()
    return result

print(subsets([1,2,3],[],[]))