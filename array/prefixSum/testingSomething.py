
# def rotate( nums: list[int], k: int) -> None:

#     final=[0]*len(nums)
#     j=0
#     for i in range(len(nums)-k, len(nums)):
#         final[j]=nums[i]
#         j+=1
#     print("this is j ",j)
#     for i in range(len(nums)-k):
#         print(i)
#         final[j]=nums[i]
#         j+=1

#     return final

def reverser(arr,left,right):
    while left<right:
        [arr[left],arr[right]]=[arr[right],arr[left]]
        left+=1
        right-=1
        
def rotate(arr,k):
    reverser(arr,0,len(arr)-1)
    reverser(arr,0,k-1)
    reverser(arr,k,len(arr)-1)


arr=[5,4,3,2,1]
print(rotate(arr,3))
print(arr)