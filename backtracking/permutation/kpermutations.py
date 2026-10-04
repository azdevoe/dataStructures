# kPermutations(arr, k)
#
# WHAT IT DOES:
#   Returns every ARRANGEMENT of exactly k elements chosen from arr.
#   Order matters: [1,2] and [2,1] are different results.
#   Example: arr=[1,2,3], k=2 -> 6 lists:
#            [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
#
# SHAPE:
#   Same as full permutations (path + visited of INDEXES + loop over arr).
#   The ONLY change: base case is len(path) == k, not len(arr).
#
# RULES TO REMEMBER:
#   - Base case saves path[:] and always returns.
#   - Whoever adds to path/visited removes them after the call.
#   - visited stores indexes, not values (values break on duplicates).
#   - k == n gives plain permutations (n! lists).
#
# COUNT:  n x (n-1) x ... (k terms) = n! / (n-k)!
# TIME:   about O(n * n!/(n-k)!)
# SPACE:  O(k)  (recursion depth k, path holds k)
#
# REAL-WORLD: top-3 podium orderings out of 10 runners.


def kPermutations(arr,k):
    res=[]
    path=[]
    visited=set()
    def backtrack():
        if len(path)==k:
            res.append(path[:])
            return 
        for i in range(len(arr)):
            if i not in visited:
                path.append(arr[i])
                visited.add(i)
                backtrack()
                path.pop()
                visited.remove(i)
    backtrack()
    return res
print(kPermutations([1,2,3],2))
print(kPermutations([1,2,3], 3))
print(kPermutations([1,2,3,4], 2))