# maxConcurrentRequests: given a list of requests [start, end],
# return the biggest number of requests running at the same time.
# A request that starts exactly when another ends does NOT overlap it.
def maxConcurrentRequests(requests):
    # your code here
    final=[]
    count=0
    result=0
    for start,end in requests:
        final.append((start,1))
        final.append((end,-1))
    final.sort()
    print(final)
    for newStart,newEnd in final:
        count+=newEnd
        result=max(result,count)
    return result

# Tests
print(maxConcurrentRequests([[5, 8], [1, 5]]))   # expect 1, you get 2
print(maxConcurrentRequests([[1, 5], [2, 6], [4, 8], [9, 10]]))          # expect 3
print(maxConcurrentRequests([[1, 5], [5, 8]]))                           # expect 1
print(maxConcurrentRequests([[1, 3], [2, 4]]))                           # expect 2
print(maxConcurrentRequests([[1, 3], [2, 4], [10, 12], [11, 13], [11, 12]]))  # expect 3
print(maxConcurrentRequests([[1, 2], [2, 3], [3, 4]]))                   # expect 1
print(maxConcurrentRequests([]))                                         # expect 0