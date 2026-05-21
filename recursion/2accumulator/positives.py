def positives(arr,storage):
    if len(arr)==0:
        return storage
    if arr[0]>0:
        storage.append(arr[0])
    return positives(arr[1:],storage)
print(positives([3, -1, 4, -2, 5],[]))