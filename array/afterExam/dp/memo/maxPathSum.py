def maxPathS(grid,r,c,memo={}):
    if (r,c) in memo: return memo[r,c]
    if r>=len(grid) or c>=len(grid[0]): return 0 
    if r == len(grid)-1 and c ==len(grid[0])-1:
        return grid[r][c]
    left = grid[r][c] +maxPathS(grid,r+1,c,memo)
    right =grid[r][c]+ maxPathS(grid,r,c+1,memo)
    memo[r,c]= max(left,right)
    return memo[r,c]

print(maxPathS(
    [
        [1,3,12],
        [5,6,2]
    ],0,0
))