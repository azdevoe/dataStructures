def subSeq(s,t):
    ori=len(s)
    i=j=0
    while j< len(t) and i < len(s):
        if s[i] == t[j]:
            i+=1
            j+=1
        else:
            i+=1
    adder=len(t)-j
    for i in range(j,adder+j):
        s+=t[i]
    return len(s)-ori

print(subSeq("cdng","coding"))
print(subSeq("abc", "cab"))
print(subSeq("xyz", "abc"))

