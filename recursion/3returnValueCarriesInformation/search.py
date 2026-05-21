def search(arr,value):
    if len(arr)==0:return False
    if arr[0]==value:return True
    if type(arr[0]) == list:
        if search(arr[0],value):return True
    return search(arr[1:],value)
        
print(search([1, [2, [3, 4]], 5], 3))
print(search([1, [2, [3, 4]], 5], 9))
print(search([[2, 3], 5], 5) )