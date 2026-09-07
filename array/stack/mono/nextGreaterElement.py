# we have 2 arrays we pick an element in array1 and find an element greater than it in array2
#nums1 = [4,1,2], nums2 = [1,3,4,2] if we pick 4 in nums1 then there will be no element after it that is bigger than 4
#so we return -1; picking 1 in nums1, 3 is greater in nums2 so we return 3
#the final answer is [-1,3,-1]

def nextGreater(nums1,nums2):
    mapp=tinyHelper(nums2)
    final=[0]*len(nums1)
    for i in range(len(nums1)):
        if nums1[i] in mapp:
            final[i]=mapp[nums1[i]]
        else:
            final[i]=-1
    return final
def tinyHelper(nums2):
    mapp={}
    stack=[]
    for i in range(len(nums2)):
        while stack and nums2[i]>nums2[stack[-1]]:
            curr=stack.pop()
            mapp[nums2[curr]]=nums2[i]
        stack.append(i)
    return mapp

print(nextGreater([4,1,2],[1,3,4,2]))