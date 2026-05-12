def mergeSort(arr,l,r):
    if r<l:return
    
    mid = l+(r-l)//2
    left=mergeSort(arr,l,mid)
    right=mergeSort(arr,mid+1,r)
    print(left,right)
arr=[3,4,2,8,6,9,1,4]
print(mergeSort(arr,0,len(arr)-1))