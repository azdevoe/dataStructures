def decBi(dec,string):
    if dec==0:
        return string
    return decBi(dec//2,str(dec%2)+string)

print(decBi(25,""))

