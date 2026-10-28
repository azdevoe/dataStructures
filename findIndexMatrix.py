def findIndex(matrix,target):
    rows,cols=len(matrix),len(matrix[0])
    left,right=0,rows*cols
    while left<right:
        mid=left+(right-left)//2
        if matrix[mid//cols][mid%cols] < target:
            left=mid+1
        elif matrix[mid//cols][mid%cols] > target:
            right=mid
        else:
            return [mid//cols,mid%cols]
    return [-1,-1]
matrix = [ [ 1,  3,  5,  7],
           [10, 11, 16, 20],
           [23, 30, 34, 60] ]

print(findIndex(matrix,20))
print(findIndex(matrix, 100))   # expect [-1, -1]
print(findIndex(matrix, 13))    # expect [-1, -1]
print(findIndex(matrix, 1))     # expect [0, 0]