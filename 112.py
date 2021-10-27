# https://leetcode.com/problems/path-sum/
# dfs
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(s: int, node: Optional[TreeNode]):
            # is leaf
            if not node:
                return False
            is_leaf = (not node.right) and (not node.left)
            if is_leaf:
                return s + node.val == targetSum

            left = dfs(s + node.val, node.left)
            if left:
                return True
            right = dfs(s + node.val, node.right)
            if right:
                return True

            return False

        if not root:
            return False
        return dfs(0, root)
