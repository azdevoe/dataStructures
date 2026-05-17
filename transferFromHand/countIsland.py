def wrapper(grid):
    visited=set()
    count=0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==1:
                if (row,col) not in visited:
                    dfs(grid,row,col,visited)
                    count+=1
    return count
def dfs(grid,row,col,visited):
    stack=[(row,col)]
    while stack:
        ro,co=stack.pop()
        visited.add((ro,co))
        neighbour=[(ro-1,co),(ro+1,co),(ro,co-1),(ro,co+1)]
        for r,c in neighbour:
            if tinyHelper(grid,r,c,visited):
                stack.append((r,c))
def tinyHelper(grid,row,col,visited):
    if row<0 or row >= len(grid) or col<0 or col>=len(grid[row]):
        return False
    if grid[row][col] == 0:
        return False
    if (row,col) in visited:
        return False
    return True
grid1 = [
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1]
]

print(wrapper(grid1))