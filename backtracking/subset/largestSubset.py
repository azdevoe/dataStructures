#Given arr and target, return the size of the largest subset
# whose sum is ≤ target. For [1,2,3,4] and target 5,
# the answer is 2 ([1,4] or [2,3]).

def largestSubset(arr,target):
    best=0
    path=[]
    def backtrack(i):
        nonlocal best
        if i == len(arr):
            if sum(path) <= target:
                print(path)
                best=max(best,len(path))
            return
        path.append(arr[i])
        backtrack(i+1)
        path.pop()
        backtrack(i+1)
    backtrack(0)
    return best

def primeLargestSubset(arr,target):
    best=0
    def backtrack(i,total,count):
        nonlocal best
        if i == len(arr):
            if total<=target:
                best=max(best,count)
            return
        backtrack(i+1,total+arr[i],count+1)
        backtrack(i+1,total,count)
    backtrack(0,0,0)
    return best
print(primeLargestSubset([1,2,3,4],5))
print(primeLargestSubset([1,2,3,4], 100))