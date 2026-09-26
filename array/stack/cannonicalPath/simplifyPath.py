def simplifyPath(path):
    arr=path.split("/")
    stack=[]
    for str in arr:
        if str == "": continue
        if str == ".": continue
        if str == "..":
            if not stack: continue
            stack.pop()
        else:
            stack.append(str)
    return "/"+"/".join(stack)
path = "/a/../../b/c//./d/"

print(simplifyPath(path))
print(simplifyPath("/../a/b/../c/./..//d//e///f"))