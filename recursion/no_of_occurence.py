def no(arr,index,tagret):
    if len(arr)<1:
        return 0
    if index<0:
        return 0
    if arr[index] == tagret:
        return 1+    no(arr,index-1,tagret)
    return no(arr,index-1,tagret)
print(no([1, 3, 3, 5, 3],4,3))