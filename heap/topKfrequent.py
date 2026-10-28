from collections import Counter
def countNum(arr,k):
    mapp = Counter(arr)
    print(mapp)
    
print(countNum([1,1,1,2,2,3],2))