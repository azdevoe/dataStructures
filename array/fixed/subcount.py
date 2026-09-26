from collections import Counter
def subCount(arr,target,size):
    curr=start=0
    count=0
    for end in range(len(arr)):
        curr+=arr[end]
        if end>=size-1:
            if curr==target:count+=1
            curr=curr-arr[start]
            start+=1
    return count

#print(subCount([2,3,2,2,3,1,3,8,5,0,2,4],7,3))

def minOperations(nums) -> int:
    mapp=Counter(nums)
    count=0
    print(mapp)
    for num in mapp:
        print("i am num",num)
        if mapp[num]%3==0:
            count+=(mapp[num]//3)
            print(mapp[num],num,(mapp[num]//3))
            print(count)
            continue
        if mapp[num]%2==0:
            count+=(mapp[num]//2)
            print(mapp[num],num,(mapp[num]//2))
            print(count)
            continue
        return -1
    print(mapp)
    return count

print(minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))