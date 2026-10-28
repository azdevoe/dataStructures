from collections import defaultdict
def lengthOfLongestSubstring(s: str) -> int:
    start=0
    largest=0
    sett=defaultdict(int)
    for end in range(len(s)):
        sett[s[end]]+=1
        while sett[s[end]]>1:
            sett[s[start]]-=1
            if sett[s[start]] <1:
                del sett[s[start]]
            start+=1
        largest=max(largest,len(sett))
    print(sett)
    return largest
print(lengthOfLongestSubstring("abcabcbb"))