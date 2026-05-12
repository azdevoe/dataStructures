def stringRecursion(string):
    if len(string)<=1:
        return string
    return stringRecursion(string[1:])+string[0]

print(stringRecursion("biro"))