def wrapper(grid):
    visited=set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == 0 or row==len(grid)-1 or col == 0 or col==len(grid[row])-1:
                if grid[row][col]==0:
                    surrounded(grid,row,col,visited)
                    
    for rower in range(len(grid)):
        for coler in range(len(grid[rower])):
            if tinyHelper(grid,rower,coler,visited) and grid[rower][coler] == 0:
                grid[rower][coler]=1
    return grid
def surrounded(grid,row,col,visited):
    stack=[(row,col)]
    
    while stack:
        r,c=stack.pop()
        visited.add((r,c))
        neighbourArray=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for neighbour in neighbourArray:
            ro,co=neighbour
            if tinyHelper(grid,ro,co,visited):
                if grid[ro][co] == 0:
                    if (ro,co) not in visited:
                        stack.append((ro,co))
                        visited.add((ro,co))
                    

def tinyHelper(grid,row,col,visited):
    if row<0 or  row>=len(grid) or col <0 or col>=len(grid[row]):
        return False
    if (row,col) in visited:
        return False
    return True

grid1 = [
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]

grid2 = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]

print(wrapper(grid1))  # should stay unchanged
print(wrapper(grid2))  # should be all 1s