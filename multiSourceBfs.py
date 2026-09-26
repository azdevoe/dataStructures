from collections import deque
def multi(grid):
    queue=deque([])
    visited=set()
    row,col=len(grid),len(grid[0])
    pre=[[float("inf")]*col for _ in range(row)]
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==1:
                pre[row][col] =0
                queue.append((row,col,0))
    while queue:
        ro,co,dis=queue.popleft()
        neighbour=[(ro-1,co),(ro+1,co),(ro,co+1),(ro,co-1)]
        for r,c in neighbour:
            if tinyHelper(grid,r,c,visited):
                queue.append((r,c,dis+1))
                visited.add((r,c))
                pre[r][c]=dis+1
    return pre
    
def tinyHelper(grid,row,col,visited):
    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
        return False
    if (row,col) in visited:
        return False
    return True
print(multi([[1,0,0,0,1]]))

grid = [
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

