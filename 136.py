# https://leetcode.com/problems/single-number/
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0)+1
        for k, v in hash_table.items():
            if v == 1:
                return k

    def singleNumber2(self, nums: List[int]) -> int:
        # 0^n = n
        # n^n = 0
        return reduce((lambda x, y: x ^ y), nums)
