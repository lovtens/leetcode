# https://leetcode.com/problems/combination-sum/
# backtracking
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 합이 target이 되도록 comb를 만들어서 반환

        result = []

        def backtracking(comb: List[int], sum_of_comb: int, index: int):
            if sum_of_comb == target:
                result.append(comb[:])
                return
            if sum_of_comb > target:
                return

            for i in range(index, len(candidates)):
                comb.append(candidates[i])
                backtracking(comb, candidates[i] + sum_of_comb, i)
                comb.pop()

        backtracking([], 0, 0)
        return result
