def countEven(arr):
    count=0
    def tinyHelper(arr,index,count):
        if index<0:
            return count
        if arr[index]%2==0:
            count+=1
        return tinyHelper(arr,index-1,count)
    answer =tinyHelper(arr,len(arr)-1,count)
    return answer

print(countEven([1, 2, 3, 4, 6]))
print(countEven([1, 3, 5]))