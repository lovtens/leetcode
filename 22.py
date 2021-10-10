# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ans.append("".join(s))
            if left < n:
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()

        backtrack([], 0, 0)
        return ans
