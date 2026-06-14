def substring(str,anagram):
    visited=set()
    start=0
    curr=""
    anagramSet=set(anagram)
    size=len(anagram)
    for end in range(len(str)):
        curr=curr+str[end]
        visited.add(str[end])
        if end>=size-1:
            if visited == anagramSet:
                return True
            curr=curr[1:]
            visited.remove(str[start])
            start+=1
    return False
print(substring("greyhounds","xyz"))