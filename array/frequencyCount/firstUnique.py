from collections import Counter
def firstUnique(s):
    newS=Counter(s)
    for st in s:
        if newS[st]==1:
            return st
    return -1