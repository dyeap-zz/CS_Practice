'''
var:

1. use a dictionary {let:adjacent letters}

1. go through all letters in grid.
    if match first letter call search
2.

valid (row,col,grid)
search (word, index, row, col,grid )
    1. base case:
        return True
    2. for row in (-1,1)
            for col in (-1,1)
                if valid(row,col,grid)
                    recurse
        return False
'''


class Solution:
    def exist_helper(self, word, index, row, col, grid):
        if index >= len(word):
            return True

        if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or (grid[row][col] != word[index]):
            return False

        # on board visited
        save_letter = grid[row][col]
        grid[row][col] = "#"
        res = self.exist_helper(word, index + 1, row + 1, col, grid) or self.exist_helper(word, index + 1, row - 1, col,
                                                                                          grid) or self.exist_helper(
            word, index + 1, row, col + 1, grid) or self.exist_helper(word, index + 1, row, col - 1, grid)
        save_letter = grid[row][col]
        return res

    def exist(self, board, word: str) -> bool:
        if len(board) == 0:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.exist_helper(word, 0, row, col, board[:][:]):
                    return True

        return False


board =[["C","A","A"],["A","A","A"],["B","C","D"]]

word = "AAB"
sol = Solution()
print(sol.exist(board,word))