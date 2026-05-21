#this si to return the sum of numbers greater than 5
def bigSum(arr):
    if len(arr)==0:
        return 0
    great =arr[0] if arr[0]>5 else 0
    return great+bigSum(arr[1:])
print(bigSum([3, 7, 1, 9, 2]))