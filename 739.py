# https://leetcode.com/problems/daily-temperatures/
# stack
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # (index, value)
        for i, t in enumerate(temperatures):
            # print(i,t, stack)
            while stack:
                if stack[-1][1] < t:
                    answer[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                else:
                    break
            stack.append([i, t])

        return answer
