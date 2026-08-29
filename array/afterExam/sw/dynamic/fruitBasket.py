from collections import defaultdict
def fruit(arr):
    start=0
    maxLength=float("-inf")
    store= defaultdict(int)
    for end in range(len(arr)):
        store[arr[end]]+=1
        while len(store) >2:
            store[arr[start]]-=1
            if store[arr[start]]==0:
                del store[arr[start]]
            start+=1
        maxLength = max(maxLength,end-start+1)
    return 0 if maxLength == float("-inf") else maxLength
print(fruit([1, 2, 1, 2, 3, 3, 4]))