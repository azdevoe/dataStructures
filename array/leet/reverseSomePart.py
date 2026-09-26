import heapq

def rev(arr,k):
    reverser(arr,0,len(arr)-1)
    reverser(arr,0,k-1)
    reverser(arr,k,len(arr)-1)
    print(arr)
def reverser(arr,l,r):
    while l<r:
        [arr[l],arr[r]]=[arr[r],arr[l]]
        l+=1
        r-=1
#print(rev([1,2,3,4,5,6,7,8],3))