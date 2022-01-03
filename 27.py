# https://leetcode.com/problems/remove-element/
# two pointers
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j-1]
                j -= 1
            else:
                i += 1

        return j
