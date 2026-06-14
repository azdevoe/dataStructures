def dynamic(arr,target):
    start=curr=0
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>target and start<end:
            curr=curr-arr[start]
            start+=1
        if curr==target:return True
    return False
print(dynamic([3,1,4,9,2,1,7,5],10))
print(dynamic([3,1,4,9,2,1,7,5], 100))
print(dynamic([3,1,4,9,2,1,7,5], 6))
print(dynamic([3,1,2,4,9,2,1,7,5], 6))
print(dynamic([1, 4], 4))