def decToBin(num):
    return decHelper(num,"")
def decHelper(num:int,acc:str):
    if num == 0: return acc
    ayy=str(num%2)
    return decHelper(num/2,acc+ayy)
print(decToBin(2))