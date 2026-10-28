def pushZerosToEnd(arr):
    # nums is a list of integers
    # move every 0 to the END of the list
    # keep the other numbers in their original order
    # do it IN PLACE: change nums itself, do not make a new list
    # return nothing
    def swap(l,r):
        [arr[l],arr[r]]=[arr[r],arr[l]]
    left=0
    while left<len(arr):
        right=left+1
        if arr[left] != 0:
            left+=1
            continue
        while right<len(arr):
            if arr[right]!=0:break
            right+=1
        if right<len(arr):
            swap(left,right)
            left+=1
        else:break
arr=[0, 1, 0, 3, 12]
print(pushZerosToEnd(arr))
print(arr)