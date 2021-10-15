# https://leetcode.com/problems/combination-sum-ii/
# backtracking
from typing import List
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        counter = Counter(candidates)
        keys = list(counter.keys())

        def backtracking(comb: List[int], sum_of_comb: int, key_index: int):
            if sum_of_comb == target:
                result.append(comb[:])
                return

            if sum_of_comb > target:
                return

            for i in range(key_index, len(keys)):
                num = keys[i]
                if counter[num] < 1:
                    continue
                comb.append(num)
                counter[num] -= 1
                backtracking(comb, sum_of_comb + num, i)
                comb.pop()
                counter[num] += 1

        backtracking([], 0, 0)
        return result
