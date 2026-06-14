from collections import Counter
def notUnique(str,anagram):
    curr=""
    start=0
    currDict={}
    size=len(anagram)
    anagramDict= Counter(anagram)
    count=0
    for end in range(len(str)):
        curr=curr+str[end]
        currDict[str[end]]=currDict.get(str[end],0)+1
        if end>=size-1:
            if currDict==anagramDict:
                count+=1
            curr=curr[1:]
            currDict[str[start]]-=1
            if currDict[str[start]] == 0:
                del currDict[str[start]]
            start+=1
    return count
            
print(notUnique("aabbaaa","aba"))