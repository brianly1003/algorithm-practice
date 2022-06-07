# 36. Valid Sudoku (Medium)
# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# TODO: Approach 1: Using Iteration         [O(1) & O(1)]

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Init data
        horizontal_lines = [{} for i in range(9)]
        vertical_lines = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # Validate a board
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    num = int(num)
                    box_index = (row // 3) * 3 + (col // 3)

                    horizontal_lines[row][num] = horizontal_lines[row].get(num, 0) + 1
                    vertical_lines[col][num] = vertical_lines[col].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    if (horizontal_lines[row][num] > 1 or
                        vertical_lines[col][num] > 1 or
                            boxes[box_index][num] > 1):
                        return False

        return True


if __name__ == "__main__":
    valid_sudoku = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    invalid_sudoku = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    s = Solution()
    # print(s.isValidSudoku(valid_sudoku))
    print(s.isValidSudoku(invalid_sudoku))
