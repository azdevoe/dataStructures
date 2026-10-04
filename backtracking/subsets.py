def subSet(arr):
    paths=[]
    result=[]
    backTrack(0,paths,result,arr)
    return result
def backTrack(i,path,result,arr):
    if i == len(arr):
        result.append(path[:])
        return
    path.append(arr[i])
    backTrack(i+1,path,result,arr)
    path.pop()
    backTrack(i+1,path,result,arr)
    
#print(subSet([1,2]))
def newSubset(arr):
    path=[]
    result=[]
    def backTrack(i):
        if i ==len(arr):
            result.append(path[:])
            return
        path.append(arr[i])
        backTrack(i+1)
        path.pop()
        backTrack(i+1)
    backTrack(0)
    return result

print(newSubset([1,2,3]))#2^n

# benchmark script 
# fundamental 
# databases how the language works acid