# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# dfs bfs

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return depth

            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        if not root:
            return 0
        return dfs(root, 0)
