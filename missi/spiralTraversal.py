def spiralTraversal(grid):
    visited=set()
    direction=[(0,1),(1,0),(0,-1),(-1,0)]
    final=[]
    row,col,d=0,0,0
    while len(final)<len(grid)*len(grid[0]):
        if helperFunction(grid,row,col,visited):
            visited.add((row,col))
            final.append(grid[row][col])
            dr,dc=direction[d]
            rower=row+dr
            coler=col+dc
            if helperFunction(grid,row,col,visited):
                row=rower
                col=coler
        else:
            d=(d+1)%4
            newr,newc=direction[d]
            row=row+newr
            col+=newc

    return final
    
def helperFunction(grid,row,col,visited):
    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
        return False
    if (row,col) in visited:
        return False
    return True
matrix =[[ 1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60] ]

print(spiralTraversal(matrix))