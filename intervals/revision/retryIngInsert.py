def retrying(arr,newArr):
    arr.append(newArr)
    arr.sort(key=lambda x: x[0])
    final=[]
    final.append(arr[0])
    for start,end in arr[1:]:
        prev=final[-1][1]
        if start<=prev:
            final[-1][1]=max(prev,end)
        else:
            final.append([start,end])
    return final
print(retrying([[1,3],[6,9]], [2,5]))
print(retrying([[1,2],[3,4]], [0,10]))