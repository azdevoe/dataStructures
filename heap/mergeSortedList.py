# mergeSortedScores: merges two already-sorted lists into one sorted list in O(n+m)
def mergeSortedScores(list1, list2):
    final=[]
    i,j=0,0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            final.append(list1[i])
            i+=1
        else:
            final.append(list2[j])
            j+=1
    while i<len(list1):
        final.append(list1[i])
        i+=1
    while j<len(list2):
        final.append(list2[j])
        j+=1
    return final

print(mergeSortedScores([1, 4, 9], [2, 3, 10]))   # [1, 2, 3, 4, 9, 10]
print(mergeSortedScores([1, 4, 9], [5, 6]))   # expected [1, 4, 5, 6, 9]