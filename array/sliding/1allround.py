from collections import Counter
def maxSum(arr,size):
    start=curr=0
    final=float("-inf")
    for end in range(len(arr)):
        curr+=arr[end]
        if end>= size-1:
            final=max(final,curr)
            curr-=arr[start]
            start+=1
    return final


def firstNegetive(arr,size):
    curr=start=0
    final=[]
    for end in range(len(arr)):
        curr+=arr[end]
        if end>=size-1:
            for i in range(start,end+1):
                if arr[i] <0:
                    final.append(arr[i])
                else:
                    final.append(0)
            curr-=arr[start]
            start+=1
    return final
            

def no_of_occurrences(str,patt):
    start=0
    curr=''
    size=len(patt)
    dic={}
    count=0
    patt_count=Counter(patt)
    for end in range(len(str)):
        curr=curr+str[end]
        dic[str[end]]=dic.get(str[end],0)+1
        if end>=size-1:
            if dic == patt_count:
                count+=1
            curr=curr[1:]
            dic[str[start]]-=1
            if dic[str[start]]==0:
                del dic[str[start]]
            start+=1
    return count
        
#print(firstNeg([12, -1, -7, 8, -15, 30, 16, 28],3))

def longestSubArray(arr,target):
    start=curr=0
    final=float("-inf")
    sub=[]
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>target and start<end:
            curr-=arr[start]
            start+=1
        final=max(final,end-start+1)
    for i in range(start,end+1):
        sub.append(arr[i])
    return sub

def longestSubstring(str):
    start=0
    curr=''
    final=0
    mapper={}
    for end in range(len(str)):
        curr+=str[end]
        mapper[str[end]]=mapper.get(str[end],0)+1
        while mapper[str[end]]>1:
            curr=curr[1:]
            mapper[str[start]]-=1
            if mapper[str[start]]==0:
                del mapper[str[start]]
            start+=1
        final=max(final,end-start+1)
    return final

def smallest_window_that_contains_target(s,t):
    t_map = Counter(t)
    window_map = {}
    matches = 0
    start = 0
    result = None
    curr=""

    for end in range(len(s)):
        # 1. add s[end] to window_map
        curr+=s[end]
        window_map[s[end]]=window_map.get(s[end],0)+1
        # 2. if s[end] is in t_map and its count just hit the required, matches += 1
        if s[end] in t_map and window_map[s[end]]==t_map[s[end]]:
            matches+=1

        while matches == len(t_map):
            # 3. record result if this window is smaller
            if result is None or len(curr)<len(result):
                result=curr
            # 4. remove s[start] from window_map
            window_map[s[start]]-=1
            if window_map[s[start]] == 0:
                del window_map[s[start]]
            # 5. if s[start] is in t_map and its count dropped below required, matches -= 1
            if s[start] in t_map and s[start] not in window_map:
                matches-=1
            # 6. start += 1
            curr=curr[1:]
            start+=1
    return result
print(smallest_window_that_contains_target("ADOBECODEBANC","ABC"))