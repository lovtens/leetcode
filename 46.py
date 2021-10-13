# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []

        def generate(subset: List[int], visited: set):
            if len(subset) == n:
                ret.append(subset[:])

            for num in nums:
                if num in visited:
                    continue
                subset.append(num)
                visited.add(num)
                generate(subset, visited)
                subset.pop()
                visited.remove(num)

        generate([], set())
        return ret
