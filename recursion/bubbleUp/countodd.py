def countOdd(arr):
    if len(arr)==0:
        return 0
    return 1+countOdd(arr[1:]) if arr[0]%2 != 0 else countOdd(arr[1:])
#print(countOdd([1, 2, 3, 4, 5]))

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    # 1. Base case: what happens when the string is empty?
    if len(s)==0:return s
    if s[0] in vowels:
        return ''+remove_vowels(s[1:])
    return s[0]+remove_vowels(s[1:])
    

print(remove_vowels("hello")) # Should print "hll"