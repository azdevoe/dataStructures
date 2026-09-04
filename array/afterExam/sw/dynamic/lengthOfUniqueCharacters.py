#this finds the length of the longest substring that contains only unique characters
from collections import defaultdict
def longUnique(word):
    start=longest=0
    mapper=defaultdict(int)
    for end in range(len(word)):
        mapper[word[end]]+=1
        while mapper[word[end]]>1:
            mapper[word[start]]-=1
            if mapper[word[start]] == 0:
                del mapper[word[start]]
            start+=1
        longest=max(longest,len(mapper))
    return longest

print(longUnique("abcabcdqbb"))