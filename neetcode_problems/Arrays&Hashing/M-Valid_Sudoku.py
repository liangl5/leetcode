# Hint: 27 sets or 27 integers using bit manipulation
# O(n^2) space complexity used 3 variables (row, cols, blocks) and each had 9 sets for each respective group
# O(n) instead of 9 sets, it is just 9 integers with bit representation
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blocks = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                b = r // 3 * 3 + c // 3
                val = 1 << (int(board[r][c])-1)
                if val & rows[r] or val & cols[c] or val & blocks[b]:
                    return False
                rows[r] |= val
                cols[c] |= val
                blocks[b] |= val

        return True
