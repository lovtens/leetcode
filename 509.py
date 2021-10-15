# https://leetcode.com/problems/fibonacci-number/
# recursion

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        x = [0, 1]
        for i in range(1, n):
            x.append(x[i] + x[i - 1])
        return x[-1]
