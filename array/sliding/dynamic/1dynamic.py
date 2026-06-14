def dynamic(arr):
    start=curr=0
    final=set()
    track=0
    for end in range(len(arr)):
        curr+=arr[end]
        final.add(arr[end])
        track+=1
        
        while end-start+1 != len(final):
            curr=curr-arr[start]
            final.remove(arr[start])
            start+=1
            track-=1
    return track

print(dynamic([1, 2, 3, 1, 2, 3, 4]))