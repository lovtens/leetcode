# https://leetcode.com/problems/container-with-most-water/
# two pointers
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo = 0
        hi = len(height) - 1
        max_area = 0

        def get_area(lo: int, hi: int):
            return min(height[lo], height[hi]) * (hi - lo)

        while lo < hi:
            area = get_area(lo, hi)
            # print(lo, hi, area)
            max_area = max(area, max_area)
            if height[lo] < height[hi]:
                lo += 1
            elif height[lo] > height[hi]:
                hi -= 1
            else:
                lo += 1
                hi -= 1

        # print(max_area)
        return max_area
