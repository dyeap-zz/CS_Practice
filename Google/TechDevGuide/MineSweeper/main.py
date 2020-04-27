'''

input: row/col

2 boards?
real and what is displayed

1. setupboard
    - everything is '-'
    - randomly put mines
    - each no mines put in number mines aorund it
functions
    setupboard
    placemines
    compute numbers around mines


2. play game()
    click  no mine then show everything that are not
'''

import random

def is_mine(i,j,grid):
    if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < 9):
        return False
    return True

def num_mines_around(i,j,grid):
    num_mines = 0
    if (is_mine(i-1,j-1,grid)):
        num_mines += 1
    if (is_mine(i-1,j,grid)):
        num_mines += 1
    if (is_mine(i-1,j+1,grid)):
        num_mines += 1
    if (is_mine(i, j-1, grid)):
        num_mines += 1
    if (is_mine(i, j+1, grid)):
        num_mines += 1
    if (is_mine(i+1, j-1, grid)):
        num_mines += 1
    if (is_mine(i+1, j, grid)):
        num_mines += 1
    if (is_mine(i+1, j+1, grid)):
        num_mines += 1

    return num_mines

def placeNums(grid):
    num_row = len(grid)
    num_col = len(grid[0])
    for i in range(num_row):
        for j in range(num_col):
            if (grid[i][j] == 0):
                grid[i][j] = num_mines_around(i,j,grid)

def placeMines(grid):
    num_row = len(grid)
    num_col = len(grid[0])
    for row in range(num_row):
        for col in range(num_col):
            if (random.randint(0,1)):
                grid[row][col] = 9

def setupBoard(row,col):
    grid = [[0] * col for _ in range(row)]
    placeMines(grid)
    placeNums(grid)
    return grid


board = setupBoard(20,20)
for row in board:
    print(row)

'''
feedback
https://techdevguide.withgoogle.com/paths/foundational/coding-question-minesweeper/#code-challenge

don't use the if method. Use double for loop to set the mine.
1. if less than half randomly place assuming everything is 0
2. if more than half randomly place assuming everything is mine

'''



