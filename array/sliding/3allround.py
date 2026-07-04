from collections import defaultdict,deque
def characterReplacement(s, k):
    start=0
    final=0
    curr=""
    s_map=defaultdict(int)
    for end in range(len(s)):
        curr+=s[end]
        s_map[s[end]]+=1
        windowlength=end-start+1
        maxcount=max(s_map.values())
        cost=windowlength-maxcount
        while cost>k:
            curr=curr[1:]
            s_map[s[start]]-=1
            if s_map[s[start]]==0:
                del s_map[s[start]]
            start+=1
            
            window_length = end - start + 1
            max_count = max(s_map.values()) if s_map else 0
            cost = window_length - max_count
        final=max(final,end-start+1)
    return final

def longest_substring_without_repeating_character(s):
    start=0
    final=0
    s_count=defaultdict(int)
    for end in range(len(s)):
        s_count[s[end]]+=1
        while s_count[s[end]]>1:
            s_count[s[start]]-=1
            if s_count[s[start]]==0:
                del s_count[s[start]]
            start+=1
        final=max(final,end-start+1)
    return final

def max_consecutive_ones(arr,k):
    start=0
    final=0
    for end in range(len(arr)):
        if arr[end] ==0:
            k-=1
        while k<0:
            if arr[start]==0:
                k+=1
            start+=1
        final=max(final,end-start+1)
    return final

def k_distint_character(s,k):
    start=0
    final=0
    s_map=defaultdict(int)
    for end in range(len(s)):
        s_map[s[end]]+=1
        while len(s_map) >k:
            s_map[s[start]]-=1
            if s_map[s[start]]==0:
                del s_map[s[start]]
            start+=1
        final=max(final,end-start+1)
    return final

def minimal_size_subarray(arr,target):
    curr=0
    final=float("inf")
    start=0
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>=target:
            final=min(final,end-start+1)
            curr-=arr[start]
            start+=1
    return final if final != float("inf") else 0

def maximum_of_each_window(arr,size):
    queue=deque([])
    final=[]
    for end in range(len(arr)):
        while queue and arr[queue[-1]]<arr[end]:
            queue.pop()
        queue.append(end)
        if end>=size-1:
            if queue[0]<end-size+1:
                queue.popleft()
            final.append(arr[queue[0]])
    return final

def minimum_of_each_window(arr,size):
    start=0
    final=[]
    queue=deque([])
    for end in range(len(arr)):
        while queue and arr[queue[-1]]>arr[end]:
            queue.pop()
        queue.append(end)
        if end>=size-1:
            if queue[0]<end-size+1:
                queue.popleft()
            
            final.append(arr[queue[0]])
            start+=1
    return final

def subarray_with_at_most_one_negative(arr):
    start=0
    final=0
    check=1
    for end in range(len(arr)):
        if arr[end]<0:
            check-=1
        while check<0:
            if arr[start]<0:
                check+=1
            start+=1
        final=max(final,end-start+1)
    return final

def smallest_subarray_with_negative_one_and_one(arr):
    start=0
    final=float("inf")
    one_condition=0
    neg_one = 0
    for end in range(len(arr)):
        if arr[end] == 1:
            one_condition+=1
        if arr[end]==-1:
            neg_one+=1
        while neg_one and one_condition:
            final=min(final,end-start+1)
            if arr[start] == 1:
                one_condition-=1
            if arr[start]==-1:
                neg_one-=1
            start+=1
    return final if final != float("inf") else-1
print(smallest_subarray_with_negative_one_and_one([1,1,-1]))
