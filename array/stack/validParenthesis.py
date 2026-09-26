def validParenthesis(s):
    stack=[-1]
    sett={"(":")","[":"]","{":"}"}
    count=0
    for i in range(len(s)):
        if s[i] in sett:
            stack.append(i)
        else:
            curr =stack.pop()
            if curr<=-1:
                stack.append(i)
            else:
                if not stack:
                    stack.append(i)
                else:
                    count=max(count,i-stack[-1])
    return count
print(validParenthesis(")()())()(())"))