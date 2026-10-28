def isInsideGrid(matrix,row, col,visited):
    # return True if (row, col) is a valid cell in a rows x cols grid,
    # False if it is off the edge
    if row<0 or row>=len(matrix) or col<0 or col>=len(matrix[0]):
        return False
    if (row,col) in visited:
        return False
    return True


def spiralOrderWalk(matrix):
    if not matrix: return []
    # return all numbers of the grid in spiral order:
    # right along the top, down the last column, left along the bottom, up the first column, then inward
    rows, cols = len(matrix), len(matrix[0])
    total = rows * cols
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    result = []
    row, col, d = 0, 0, 0
    while len(result) < total:
        # 1. add matrix[row][col] to result, and (row, col) to visited
        if isInsideGrid(matrix,row,col,visited):
            result.append(matrix[row][col])
            visited.add((row,col))
        # 2. find the next cell: row + dr, col + dc, using directions[d]
            dr,dc=directions[d]
            nextRow, nextCol = row + dr, col + dc
            if (isInsideGrid(matrix,nextRow,nextCol,visited)):
                row=nextRow
                col=nextCol
# 3. if you can't step there (use isInsideGrid): turn, then find the next cell again
        else:
            d=(d+1)%4
            dr,dc=directions[d]
            row=row+dr
            col=col+dc
        # 4. move: row, col become the next cell
    return result
m = [[1, 2], [3, 4]]
# print(isInsideGrid(m, 0, 2, set()))  #   -> col 2 >= 2 columns      -> False ✓
# print(isInsideGrid(m, 1, 1, set()))   #  -> inside, (1,1) not in set> True  ✓
# print(isInsideGrid(m, 1, 1, {(1,1)}))  # -> inside, but (1,1) in set-> False ✓
# print(isInsideGrid(m, -1, 0, set()))    #-> row < 0        -> False ✓
print(spiralOrderWalk([[1, 2], [3, 4]]))            # expect [1, 2, 4, 3]
print(spiralOrderWalk([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))# expect [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralOrderWalk([]))         # expect []
print(spiralOrderWalk([[]]))       # expect []
print(spiralOrderWalk([[7]]))      # expect [7]




def isInsideGrid(matrix, row, col, visited):
    # return True if (row, col) is a valid cell in the grid
    # AND has not been visited yet; otherwise False
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False
    if (row, col) in visited:
        return False
    return True


# def spiralOrderWalk(matrix):
#     # return all numbers of the grid in spiral order:
#     # right along the top, down the last column,
#     # left along the bottom, up the first column, then inward
#     rows, cols = len(matrix), len(matrix[0])
#     total = rows * cols

#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     #               right    down     left     up
#     d = 0                       # which direction we are facing
#     row, col = 0, 0             # where we are standing
#     visited = set()
#     result = []

#     while len(result) < total:
#         # 1. collect the cell we are ON
#         result.append(matrix[row][col])
#         visited.add((row, col))

#         # 2. peek at the next cell (don't move yet)
#         dr, dc = directions[d]
#         nextRow, nextCol = row + dr, col + dc

#         # 3. blocked? turn right, then peek again with the new direction
#         if not isInsideGrid(matrix, nextRow, nextCol, visited):
#             d = (d + 1) % 4
#             dr, dc = directions[d]
#             nextRow, nextCol = row + dr, col + dc

#         # 4. move
#         row, col = nextRow, nextCol

#     return result


# print(spiralOrderWalk([[1, 2], [3, 4]]))                          # [1, 2, 4, 3]
# print(spiralOrderWalk([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))         # [1, 2, 3, 6, 9, 8, 7, 4, 5]
# print(spiralOrderWalk([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]