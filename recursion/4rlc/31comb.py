def subset(arr,k,current,final):
    if len(current)==k:
        final.append(current[:])
    for i in range(len(arr)):
        current.append(arr[i])
        subset(arr[i+1:],k,current,final)
        current.pop()
    return final

def permutation(arr,current,final):
    if len(current) ==3:
        final.append(current[:])
    for i in range(len(arr)):
        current.append(arr[i])
        permutation(arr[i+1:]+arr[:i],current,final)
        current.pop()
    return final


def phoneBook(digits,current,final):
    phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }
    if len(digits) ==0:
        final.append(current[:])
        return
    for let in phone[digits[0]]:
        current.append(let)
        phoneBook(digits[1:],current,final)
        current.pop()
    return final
print(phoneBook("23", [], []))

        