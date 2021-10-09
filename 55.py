# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # 최대로 갈 수 있는 index
        dp = [nums[0]]
        for i in range(1, n - 1):
            if dp[-1] < i:
                # 지금 보고 있는 위치로 도착 할 수 없음
                return False

            value = max(i + nums[i], dp[-1])
            if value >= n - 1:
                return True
            dp.append(value)

        return dp[n - 2] >= n - 1
