def compress(s):
    if s == "":return ""
    count=0
    prev=None
    final=[]
    for char in s:
        if prev == char:
            count+=1
            print(count,char)
        elif prev is None:
            count+=1
            prev=char
        else:
            final.append(prev+str(count))
            count=0
            prev=char
            count+=1
    final.append(prev+str(count))
    return "".join(final)
print(compress("aaabbc"))# → output "a3b2c1"