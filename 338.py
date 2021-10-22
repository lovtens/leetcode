# https://leetcode.com/problems/counting-bits/
# bit manipulation dp
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []

        k = 1
        for i in range(n + 1):
            if i == 0:
                ret.append(0)
            elif i == 1:
                ret.append(1)
            else:
                l = 2 ** k
                j = i % l
                ret.append(1 + ret[j])
                if j == l - 1:
                    k += 1

        return ret


        """
        6 -> 110
        3 -> 11
        (6 >> 1) = 3
        8 -> 1000
        4 -> 100
        (4 << 1) = 8
        """
        # result = [0]
        # for i in range(1, n+1):
        #     result.append(result[i // 2] + i % 2)
        # return result