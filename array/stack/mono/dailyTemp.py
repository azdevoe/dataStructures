def dailyTemp(arr):
    stack=[]
    result=[0]*(len(arr))
    for i in range(len(arr)):
        stack.append(i)
        while stack and arr[i]>arr[-1]:
            popped =stack.pop()
            result[popped]=i-popped
            stack.append(i)
    return result

print(dailyTemp([73,74,75,71,69,72,76,73]))
