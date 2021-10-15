# https://leetcode.com/problems/get-maximum-in-generated-array/
# recursion

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        x = [0, 1]
        ret = 1

        for i in range(2, n+1):
            if i % 2 == 0:
                value = x[int(i / 2)]
                x.append(value)
                ret = max(ret, value)
            else:
                value = x[int((i - 1) / 2)] + x[int((i - 1) / 2) + 1]
                x.append(value)
                ret = max(ret, value)

        return max(x[-1], x[-2])
