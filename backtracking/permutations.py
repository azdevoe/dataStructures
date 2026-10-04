def permutations(arr):
    result=[]
    path=[]
    
    def backtrack():
        if len(path)==len(arr):
            result.append(path[:])
            return
        for j in range(len(arr)):
            if arr[j] not in path:
                path.append(arr[j])
                backtrack()
                path.pop()
    
    backtrack()
    return result

print(permutations([1,2,3]))


def permu(arr):
    result=[]
    path=[]
    def backTrack():
        if len(path)==len(arr):
            result.append(path[:])
            return
        for i in range(len(arr)):
            if arr[i] not in path:
                path.append(arr[i])
                backTrack()
                path.pop()
    backTrack()
    return result
print(permu([5,6,7]))