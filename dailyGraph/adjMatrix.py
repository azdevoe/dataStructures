def wrapper(matrix):
    visited=set()
    final=0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] ==1:
                if (row,col) not in visited:
                    final = max(final,dfs(matrix,row,col,visited))
    return final

def dfs(matrix,row,col,visited):
    stack=[(row,col)]
    count=1
    while stack:
        curr=stack.pop()
        r,c=curr
        visited.add((r,c))
        neighbours=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for ro,co in neighbours:
            if tinyHelper(matrix,ro,co,visited):
                stack.append((ro,co))
                visited.add((ro,co))
                count+=1
    return count

def tinyHelper(matrix,row,col,visited):
    if(row,col) in visited:
        return False
    if row <0 or row>=len(matrix) or col<0 or col>=len(matrix[row]):
        return False
    if matrix[row][col]==0:
        return False
    return True

grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print(wrapper(grid))