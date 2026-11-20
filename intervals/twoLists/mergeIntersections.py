# intervalIntersections: given two sorted lists of free slots
# [start, end] (each list has no overlaps inside itself),
# return the list of slots where both people are free.
def intervalIntersections(a:list, b:list):
    # your code here
    final=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        inner=[max(a[i][0],b[j][0]),min(a[i][1],b[j][1])]
        if inner[0]<=inner[1]:
            final.append(inner)
        if a[i][1]>=b[j][1]:
            j+=1
        else:
            i+=1
    return final

# Tests
print(intervalIntersections([[1, 5], [8, 12]], [[3, 10]]))
# expect [[3, 5], [8, 10]]

print(intervalIntersections(
    [[0, 2], [5, 10], [13, 23], [24, 25]],
    [[1, 5], [8, 12], [15, 24], [25, 26]]))
# expect [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

print(intervalIntersections([[1, 2]], [[3, 4]]))              # expect []
print(intervalIntersections([], [[1, 2]]))                    # expect []
print(intervalIntersections([[1, 10]], [[2, 3], [4, 5]]))     # expect [[2, 3], [4, 5]]