# https://leetcode.com/problems/permutations-ii/
# backtracking
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []

        def generate(comb: List[int], hashtable: dict):
            if len(comb) == n:
                result.append(comb[:])
                return

            for k, v in hashtable.items():
                if v < 1:
                    continue
                comb.append(k)
                hashtable[k] -= 1
                generate(comb, hashtable)
                comb.pop()
                hashtable[k] += 1

        counter = Counter(nums)

        generate([], counter)
        return result
