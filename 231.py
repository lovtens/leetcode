# https://leetcode.com/problems/power-of-two/
# bit manipulation recursion

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        def bit_count(x: int):
            if x == 0:
                return False
            if x == 1:
                return True
            r = x % 2
            if r != 0:
                return False
            return bit_count(x // 2)

        counts = bit_count(n)
        return counts == 1


# if (n <= 0) return false;
# return !(n & (n - 1))

