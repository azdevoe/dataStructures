def array_sum(arr,storage):
    if len(arr)==0:
        return storage
    storage+=arr[0]
    return array_sum(arr[1:],storage)
    

def reverse_string(s, storage=""):
    if len(s)==0:
        return storage
    storage =s[0]+storage
    return reverse_string(s[1:],storage)


def factorial(n, current_product=1):
    if n==1:
        return current_product
    current_product=current_product*n
    return factorial(n-1,current_product)

print(factorial(5)) # Should print 120