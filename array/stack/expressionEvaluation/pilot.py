def evaluate(s):
    stack=[]
    lastOpp="+"
    for i in range(len(s)):
        if s[i]  in "+-":
            lastOpp=s[i]
        elif s[i] in "*/":
            continue
        else:
            stack.append(int(lastOpp+s[i]))

print(evaluate("3-2"))