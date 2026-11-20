# minJobsToRemove: given a list of jobs [start, end],
# return the fewest jobs to remove so that no two remaining
# jobs overlap. A job that starts exactly when another ends
# does NOT overlap.
def minJobsToRemove(jobs:list):
    # your code here
    if not jobs: return 0
    arr=sorted(jobs,key=lambda x:x[1])
    prev=arr[0][1]
    count=1
    print(arr)
    for start,end in arr[1:]:
        if prev<=start:
            prev=end
            count+=1
    return len(arr)-count
    

# Tests
print(minJobsToRemove([[1, 10], [2, 3], [4, 5], [6, 7]]))  # expect 1
print(minJobsToRemove([[1, 2], [2, 3], [3, 4], [1, 3]]))   # expect 1
print(minJobsToRemove([[1, 2], [1, 2], [1, 2]]))           # expect 2
print(minJobsToRemove([[1, 2], [2, 3]]))                   # expect 0
print(minJobsToRemove([]))                                 # expect 0
print(minJobsToRemove([[1, 2], [2, 5], [3, 6]]))  # expect 1, you get 0