def wrapper(matrix):
    count=0
    visited=set()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                if (row,col) not in visited:
                    dfs(matrix,row,col,visited)
                    count+=1
    return count
def dfs(matrix,row,col,visited):
    stack=[(row,col)]
    while stack:
        curr=stack.pop()
        visited.add(curr)
        row,col=curr
        possiBleNeighbour = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        for nr,nc in possiBleNeighbour:
            if tinyHelper(matrix,nr,nc,visited):
                stack.append((nr,nc))
                visited.add((nr,nc))
        
def tinyHelper(matrix,row,col,visited):
    if row<0 or row >=len(matrix) or col<0 or col>=len(matrix[0]):
        return False
    if matrix[row][col]==0:
        return False
    if (row,col) in visited:
        return False
    return True

grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print(wrapper(grid))