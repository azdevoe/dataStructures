def maxVowel(arr,k):
    start=curr=final=0
    vowelMap = {"a","e","i","o","u"}
    for end in range(len(arr)):
        if arr[end] in vowelMap:
            curr+=1
        if end - start>=k:
            if arr[start] in vowelMap:
                curr-=1
            start+=1
        if end-start+1==k:
            final = max(final,curr)
    return final
print(maxVowel("abciiidef",3))