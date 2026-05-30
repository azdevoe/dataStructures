def subsets(arr, current, result):
    result.append(current[:])
    for i in range(len(arr)):
        current.append(arr[i])
        subsets(arr[i+1:],current,result)
        current.pop()
    return result

def permutation(arr,current,result):
    if len(arr) ==0:
        result.append(current[:])
    for i in range(len(arr)):
        current.append(arr[i])
        permutation(arr[:i] + arr[i+1:],current,result)
        current.pop()
    return result

print(permutation([1,2,3],[],[]))