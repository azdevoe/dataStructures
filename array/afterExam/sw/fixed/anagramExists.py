from collections import Counter,defaultdict
def anagramExists(word,string):
    start=0
    mapp=defaultdict(int)
    strCount= Counter(string)
    if strCount == Counter(word[0:len(string)]):return True
    for end in range(len(word)):
        mapp[word[end]]+=1
        if end - start>=len(string):
            mapp[word[start]]-=1
            if mapp[word[start]] ==0:
                del mapp[word[start]]
            start+=1
            if mapp == strCount:return True
            
    return False

print(anagramExists("greyhounds",'huy'))
print(anagramExists("abcxyz","xyz"))