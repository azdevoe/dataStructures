#this is for longest unique substring
from collections import defaultdict
def longestUnique(arr):
    start=0
    final=0
    mapper = defaultdict(int)
    for end in range(len(arr)):
        mapper[arr[end]]+=1
        print(mapper)
        while mapper[arr[end]]>1:
            mapper[arr[start]]-=1
            start+=1
        final=max(final,end-start+1)
    return final
print(longestUnique("abcabcbb"))