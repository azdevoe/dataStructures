def postfix(input):
    stack=[]
    ops={"+","-","/","*"}
    inp=0
    for char in input:
        if char not in ops:
            stack.append(char)
        else:
            if stack:
                in1=stack.pop()
                if stack:
                    in2=stack.pop()
                    inp =tinyHelp(in1,char,in2)
                    stack.append(inp)
    return inp

def tinyHelp(in11,char,in22):
    in1=int(in11)
    in2=int(in22)
    if char == "+":
        inp = in2 + in1
    elif char == "-":
        inp = in2 - in1
    elif char == "*":
        inp = in2 * in1
    elif char == "/":
        inp = int(in2 / in1)
    return inp


print(postfix("21+3*"))
print(postfix(["1","2","+","3","*","4","-"]))