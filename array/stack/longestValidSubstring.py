def longest(s):
    stack=[-1]
    valid=0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            curr=stack.pop()
            if s[curr] == "(" and s[i]==")":
                valid=max(valid,i-stack[-1])
            else:
                stack.append(i)
    return valid
print(longest(")()())()(())"))