def container_with_most_water(arr):
    left=0
    right=len(arr)-1
    final=0
    while left<right:
        area=min(arr[left],arr[right])*(right-left)
        final=max(final,area)
        print(left,right,arr[left],arr[right],final)
        if arr[left]<=arr[right]:
            left+=1
        elif arr[right]<arr[left]:
            right-=1
    return final



def isPalindrome( s: str) -> bool:
    if len(s) == 0:
        return False
    print(s)
    new_string="".join(c for c in s if c.isalnum())
    left=0
    right=len(new_string)-1
    while left<=right:
        if new_string[left].lower()!=new_string[right].lower():
            return False
        else:
            left+=1
            right-=1
    return True
print(isPalindrome("Was it a car or a cat I saw?"))
