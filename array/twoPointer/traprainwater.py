def trappingRainWater(arr):
    maxLeft=[0]*len(arr)
    maxRight=[0]*len(arr)
    maxLeft[0]=arr[0]
    maxRight[-1]=arr[-1]
    final=0
    for i in range(1,len(arr)):
        maxLeft[i]=max(arr[i],maxLeft[i-1])
    for j in range(len(arr)-2,-1,-1):
        maxRight[j] = max(arr[j],maxRight[j+1])
    
    for i in range(len(arr)):
        final+=(min(maxLeft[i],maxRight[i])-arr[i])
    return final

print(trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))
