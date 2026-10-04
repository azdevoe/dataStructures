def countSubsets(arr, target):
    path=[]
    count=0
    def backtrack(i):
        nonlocal count
        if i == len(arr) :
            if sum(path)==target:
                count+=1
            return
        path.append(arr[i])
        backtrack(i+1)
        path.pop()
        backtrack(i+1)
    backtrack(0)
    return count

def countSubset(arr,target):
    path=[]
    finalcount=0
    def backtrack(i):
        if i ==len(arr):
            if sum(path)==target:
                return 1
            return 0
        path.append(arr[i])
        a=backtrack(i+1)
        path.pop()
        b=backtrack(i+1)
        return a+b
    finalcount+=backtrack(0)
    return finalcount


def countSubset(arr, target):
    def backtrack(i, total):
        if i == len(arr):
            return 1 if total == 0 else 0
        a = backtrack(i+1, total - arr[i])   # take
        b = backtrack(i+1, total)            # skip
        return a + b
    return backtrack(0, target)
print(countSubset([1,2],3))
print(countSubset([1,2,3],3))