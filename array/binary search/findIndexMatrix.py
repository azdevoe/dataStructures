def findIdInMatrix(matrix, target):
    # matrix: rows x cols grid of integers
    # each row is sorted ascending, and the first number of each row
    # is bigger than the last number of the previous row
    # return [row, col] of target, or [-1, -1] if it isn't there
    rows,cols=len(matrix),len(matrix[0])
    left,right=0,(rows*cols)
    while left<right:
        mid=left+(right-left)//2
        row=mid//cols
        col=mid%cols
        if matrix[row][col]<target:
            left=(row*cols)+col+1
        elif matrix[row][col]>target:
            right=row*cols+col
        else:
            return [row,col]
    return [-1,-1]
matrix = [ [ 1,  3,  5,  7],
           [10, 11, 16, 20],
           [23, 30, 34, 60] ]

print(findIdInMatrix(matrix, 16))    # expect [1, 2]
print(findIdInMatrix(matrix, 13))    # expect [-1, -1]
print(findIdInMatrix(matrix, 1))     # expect [0, 0]
print(findIdInMatrix(matrix, 60))    # expect [2, 3]
print(findIdInMatrix(matrix, 100))   # expect [-1, -1]  (crashed before the fix)