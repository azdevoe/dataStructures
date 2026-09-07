def dailyTemp(arr):
    stack=[]
    result=[0]*len(arr)
    for i in range(len(arr)):
        while stack and arr[i]>arr[stack[-1]]:
            curr=stack.pop()
            result[curr]=i-curr
        stack.append(i)
    return result
print(dailyTemp([73,74,75,71,69,72,76,73]))
