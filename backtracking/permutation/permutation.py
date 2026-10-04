def permutation(arr):
    result=[]
    path=[]
    visited=set()
    
    def backTrack():
        if len(path) == len(arr):
            result.append(path[:])
            return
        for i in range(len(arr)):
            if i not in visited:
                visited.add(i)
                path.append(arr[i])
                backTrack()
                path.pop()
                visited.remove(i)
    backTrack()
    return result
print(permutation([1,2,3]))
print(permutation([1,1,2]))