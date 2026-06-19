from collections import defaultdict,deque
def k_distant(str,k):
    curr=''
    start=0
    final=0
    str_map={}
    for end in range(len(str)):
        curr+=str[end]
        str_map[str[end]]=str_map.get(str[end],0)+1
        while len(str_map)>k:
            curr=curr[1:]
            str_map[str[start]]-=1
            if str_map[str[start]]==0:
                del str_map[str[start]]
            start+=1
        final=max(final,end-start+1)
    return final

def maxCount(arr,k):
    start=curr=0
    count=float("-inf")
    for end in range(len(arr)):
        curr+=arr[end]
        if arr[end]==0:
            k-=1
        while k<0:
            curr-=arr[start]
            if arr[start]==0:
                k+=1
            start+=1
        count=max(count,end-start+1)
    return count


def longest_subarray_with_at_most_one_negative(arr):
    start=curr=0
    final=float("-inf")
    neg_count=1
    for end in range(len(arr)):
        curr+=arr[end]
        if arr[end]<0:
            neg_count-=1
        while neg_count<0:
            curr-=arr[start]
            if arr[start]<0:
                neg_count+=1
            start+=1
        final=max(final,end-start+1)
    return final


def length_of_smallest_subarray_that_contains_one_and_minus1(arr):
    curr=start=0
    final=float("inf")
    matches=0
    matches_dict=defaultdict(int)
    for end in range(len(arr)):
        curr+=arr[end]
        if arr[end]==1 or arr[end] == -1:
            matches_dict[arr[end]]+=1
            if matches_dict[1]>=1 and matches_dict[-1]>=1:
                matches=2
        while matches == 2:
            curr-=arr[start]
            final=min(final,end-start+1)
            if arr[start] == 1 or arr[start] == -1:
                matches_dict[arr[start]]-=1
                if matches_dict[-1] <1 or matches_dict[1]<1:
                    matches-=1
            start+=1
    return final

def first_negative(arr,size):
    start=curr=0
    final=[]
    tracker=deque([])
    for end in range(len(arr)):
        curr+=arr[end]
        if arr[end]<0:
            tracker.append(end)
        if end>=size-1:
            if not tracker:
                final.append(0)
            else:
                if tracker[0] <= end-size:
                    tracker.popleft()
                if not tracker:
                    final.append(0)
                else:
                    final.append(arr[tracker[0]])
            start+=1
    return final


def maximum_no_of_each_window(arr, size):

    final = []
    tracker = deque([])  
    for end in range(len(arr)):
        
        while tracker and arr[tracker[-1]] < arr[end]:
            tracker.pop()
            
        tracker.append(end)
        
        
        if tracker[0] <= end - size:
            tracker.popleft()
            
        if end >= size - 1:
            final.append(arr[tracker[0]])
            
    return final

def minimum_no_for_each_window(arr,size):

    final=[]
    tracker=deque([])
    for end in range(len(arr)):
        while tracker and arr[tracker[len(tracker)-1]]>arr[end]:
            tracker.pop()
        tracker.append(end)
        
        if tracker[0]<end-size+1:
            tracker.popleft()
            
        if end>=size-1:
            final.append(arr[tracker[0]])
    return final

print(minimum_no_for_each_window([9, 4, 7, 2, 6], 3))
# Output: [3, 3, 5, 5, 6, 7]