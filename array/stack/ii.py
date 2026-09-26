import heapq
def removeOccurrences(s: str, part: str) -> str:
    stack=[]
    leng=len(part)
    for char in s:
        stack.append(char)
        if len(stack)>leng-1 and "".join(stack[len(stack)-leng:]) == part:
            for _ in range(leng):
                stack.pop()
    return "".join(stack)

json1='{"name":"Alex","age":"25","city":"New York"}'
json2='{"name":"Alex","age":"30","city":"Denvar","nonya":"nonya"}'
def tinyHelper(s):
    inner = s.strip('{}')
    pairs=inner.split(",")
    final={}
    for pair in pairs:
        key,val =pair.split(":")
        key=key.strip('"')
        val=val.strip('"')
        final[key]=val
    return final

def ana(json1,json2):
    j1=tinyHelper(json1)
    j2=tinyHelper(json2)
    final=[]
    for key in j1:
        if key in j2 and j2[key] != j1[key]:
            final.append(key)
    return sorted(final)
#print(ana(json1,json2))

uu='{"bio":"loves cake, hates rain"}'
u=uu.strip("{}")

print(u)