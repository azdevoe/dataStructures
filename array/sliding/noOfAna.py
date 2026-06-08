from collections import Counter
def noOfAna(string,pattern):
    start=0
    curr=""
    arr_pattern=Counter(pattern)
    final={}
    final[pattern]=[]
    for end in range(len(string)):
        curr=curr+string[end]
        if Counter(curr) == arr_pattern:
            final[pattern].append(curr)
        if end<= len(pattern)-1:
            curr=curr-string[start]
            start+=1
    return final

print(noOfAna("forxxorfxdofr","for"))