# https://leetcode.com/problems/3sum/
# two pointers
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo = i + 1
            hi = n - 1
            while lo < hi:
                tmp_sum = nums[lo] + nums[hi] + nums[i]
                if tmp_sum == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif tmp_sum < 0:
                    lo += 1
                else:
                    hi -= 1

        return ans
