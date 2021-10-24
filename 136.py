# https://leetcode.com/problems/single-number/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0)+1
        for k, v in hash_table.items():
            if v == 1:
                return k
