# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# two pointers
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        n = len(nums)
        if n == 0:
            return 0

        while j < n:
            if nums[i] < nums[j]:
                i += 1
                nums[i] = nums[j]
            else:
                j += 1

        return i + 1
