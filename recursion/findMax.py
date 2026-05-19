def findMax(arr):
    def findMaxsub(arr,ind,maxe):
        if ind<0:
            return maxe
        maxe=max(maxe,arr[ind])
        return findMaxsub(arr,ind-1,maxe)
    index=len(arr)-1
    maxV=arr[index]
    answer =findMaxsub(arr,index,maxV)
    return answer


def typeOf(arr):
    if type(arr) == list:
        return "list"
    return "int"
def flatten(arr,result):
    for num in arr:
        if typeOf(num) == "list":
            flatten(num,result)
        else:
            result.append(num)
    return result

arr=[1, [2, [3, 4], 5], 6],
print(flatten(arr,[]))