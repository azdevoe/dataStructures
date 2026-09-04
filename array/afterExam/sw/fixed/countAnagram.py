from collections import Counter,defaultdict
def countAnagram(word,string):
    stringCount=Counter(string)
    count=start=0
    if stringCount == Counter(word[0:len(string)]): count+=1
    globalMap = defaultdict(int)
    for end in range(len(word)):
        globalMap[word[end]]+=1
        if end-start>= len(string):
            globalMap[word[start]]-=1
            if globalMap[word[start]]==0:
                del globalMap[word[start]]
            start+=1
            if globalMap==stringCount:count+=1
    return count

print(countAnagram("gattactat","att"))