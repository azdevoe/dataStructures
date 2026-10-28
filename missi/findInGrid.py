def findInGrid(grid,target):
    rows,cols=len(grid),len(grid[0])
    left,right=0,rows*cols
    while left<right:
        mid=left+(right-left)//2
        actualMid=grid[mid//cols][mid%cols]
        if actualMid<target:
            left=mid+1
        elif actualMid>target:
            right=mid
        else:
            return [mid//cols,mid%cols]
    return [-1,-1]
    
matrix = [ [ 1,  3,  5,  7],
           [10, 11, 16, 20],
           [23, 30, 34, 60] ]
print(findInGrid(matrix,20))