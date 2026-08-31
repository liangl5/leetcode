# Hint: stack backtracking, keep note of open and closed counts
# My solution was similar to backtracking but used a stack and it kept track of the built string, open parentheses and closed parentheses.
# The backtrack solution given used a separate function to add parentheses, explore further, then backtrack.
# There is a dynamic programming solution - idea is that when you add 1 parentheses, you have n-1 parentheses to distribute inside and to the right of the new parentheses.
# So for 3 it could be (0)2, (1)1, or (2)0.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass
