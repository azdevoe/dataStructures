def longestUnique(str):
    start=0
    curr=''
    final=0
    dic={}
    #Fc1@Students
    for end in range(len(str)):
        curr=curr+str[end]
        dic[str[end]]=dic.get(str[end],0)+1
        while dic[str[end]] >1:
            curr=curr[1:]
            dic[str[start]]-=1
            if dic[str[start]]<1:
                del dic[str[start]]
            start+=1
        final=max(final,end-start+1)
    return final
print(longestUnique("abcabcqbb"))
print(longestUnique("abcd"))