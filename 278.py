# https://leetcode.com/problems/first-bad-version/
# binary search

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = None
        while low<high:
            mid =low + int(( high - low ) / 2 )
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low