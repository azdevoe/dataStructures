def minRemov(s):
    stack=[]
    setter=set()
    count=0
    sett={"(":")","[":"]","{":"}"}
    for i in range(len(s)):
        if s[i] in sett:
            print(s[i])
            stack.append(i)
        else:
            if s[i].isalpha():
                continue
            if not stack:
                count+=1
                setter.add(i)
            else:
                stack.pop()
    while stack:
        count+=1
        setter.add(stack[-1])
        stack.pop()
    print(setter)
    arr=[]
    for i in range(len(s)):
        if i in setter:
            continue
        arr.append(s[i])
    return "".join(arr)
print(minRemov("a)b(c)d"))
print(minRemov("(a(b(c)d"))