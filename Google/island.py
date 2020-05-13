def is_island(row, col, grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    # check if bad move/no island
    # print(row,col)
    if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] == 0:
        return False
    return True


def remove_curr_island(row, col, grid):
    # base case
    if not is_island(row, col, grid):
        return
    # recursive case

    grid[row][col] = 0
    for (x, y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        # make move
        crow = row + x
        ccol = col + y

        remove_curr_island(crow, ccol, grid)
        # undo move
        # crow -= x
        # ccol -= y


def get_number_of_islands(binaryMatrix):
    grid = binaryMatrix
    res = 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                remove_curr_island(0, 0, binaryMatrix)
                res += 1
    return res


print(get_number_of_islands([[1, 0, 1, 0],
                             [0, 1, 1, 1],
                             [0, 0, 1, 0]]))


if [-1]:
    print("yes")