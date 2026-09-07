def rect(arr):
    maxArea=curr=0
    print(arr)
    arr1=right(arr)
    arr2=left(arr)
    print(arr1,arr2)
    for i in range(len(arr)):
        curr=arr[i]*(arr1[i]-arr2[i]-1)
        maxArea=max(maxArea,curr)
    return maxArea

def right(arr):
    stack=[]
    final=[len(arr)]*len(arr)
    for i in range(len(arr)):
        while stack and arr[i]<arr[stack[-1]]:
            curr=stack.pop()
            final[curr]=i
        stack.append(i)
    return final

def left(arr):
    stack=[]
    result=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[i]<arr[stack[-1]]:
            curr=stack.pop()
            result[curr]=i
        stack.append(i)
    return result

print(rect([2, 1, 5, 6, 2, 3]))