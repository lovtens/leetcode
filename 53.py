# https://leetcode.com/problems/maximum-subarray/
# divide and conquer
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        min_sum = -len(nums) * (10 ** 4)

        def max_sum_sub_array(nums: List[int], low: int, high: int):

            if low == high:
                return nums[low]

            mid = (low + high) // 2

            left_max_sum = min_sum
            left_sum = 0
            for i in range(mid, low - 1, -1):
                left_sum += nums[i]
                left_max_sum = max(left_max_sum, left_sum)

            right_max_sum = min_sum
            right_sum = 0
            for i in range(mid + 1, high + 1):
                right_sum += nums[i]
                right_max_sum = max(right_max_sum, right_sum)

            left = max_sum_sub_array(nums, low, mid)
            right = max_sum_sub_array(nums, mid + 1, high)
            return max(left_max_sum + right_max_sum, left, right)

        return max_sum_sub_array(nums, 0, len(nums) - 1)
