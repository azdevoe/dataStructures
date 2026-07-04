def thresum(nums,target):
    arr=sorted(nums)
    final=[]
    for i in range(len(arr)):
        if i>0 and arr[i]==arr[i-1]:continue
        left=i+1
        right=len(arr)-1
        while left<right:
            if arr[left]+arr[right]<target-arr[i]:
                left+=1
            elif arr[left]+arr[right]>target-arr[i]:
                right-=1
            else:
                final.append([arr[i],arr[left],arr[right]])
                left+=1
                right-=1
                while left<right and arr[left] == arr[left-1]:
                    left+=1
                while left<right and arr[right] == arr[right+1]:
                    right-=1
    return final

print(thresum([-1, 0, 1, 2, -1, -4],0))
print(thresum([-2, 0, 0, 2, 2],0))