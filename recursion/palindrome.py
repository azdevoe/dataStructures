def palin(string):
    if len(string)<=1:
        return True
    
    if  string[0] == string[len(string)-1]:
        if palin(string[1:len(string)-1]):
            return True
    return False
    
print(palin("payap"))
