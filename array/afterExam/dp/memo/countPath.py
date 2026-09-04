def countPath(grid,r,c,memo={}):
    if (r,c) in memo: return memo[r,c]
    if r >=len(grid) or c>=len(grid[0]) or grid[r][c]==1: return 0
    if r == len(grid)-1 or c ==len(grid[0])-1: return 1
    
    left = countPath(grid,r+1,c,memo)
    right = countPath(grid,r,c+1,memo)
    memo[r,c]= left+right
    memo[c,r] = left+right
    return memo[r,c]
print(countPath([
    [0,1],
    [0,0]
    ],0,0))
