def pow(x,n):
    if n ==0:
        return 1
    return pow(x,n-1)*x


def palindrome(word):
    if len(word)==0:return False
    if len(word)==1:return True
    if word[0] != word[len(word)-1]:return False
    return palindrome(word[1:len(word)-1])

def euclid(a,b):
    if b==0:
        return a
    mod=a%b
    temp=b
    a=temp
    r=mod
    return euclid(a,r)

def permutation(string):
    if len(string)==1:
        return [string]
    result=[]
    for i in range(len(string)):
        first=string[i]
        rest= string[:i]+string[i+1:]
        for prem in permutation(rest):
            result.append(first+prem)
    return result
print(permutation("abcd"))