# https://leetcode.com/problems/number-of-1-bits/
# bit manipulation


class Solution:
    def hammingWeight(self, n: int) -> int:
        def bit_count(x: int):
            if x == 0:
                return 0
            return (x % 2) + bit_count(int(x / 2))

        return bit_count(n)