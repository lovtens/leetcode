# https://leetcode.com/problems/longest-palindrome/#
# greedy
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(list(s))
        ret = 0
        for k, v in counter.items():
            if v % 2 == 0:
                ret += v
            else:
                if ret % 2 == 0:
                    ret += v
                else:
                    ret += v - 1
        return ret
