# https://leetcode.com/problems/sum-of-left-leaves/
# dfs
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], node_type: str):
            # left leaf
            if not node.left and not node.right and node_type == 'left':
                return node.val
            ret = 0
            if node.left:
                ret += dfs(node.left, 'left')
            if node.right:
                ret += dfs(node.right, 'right')

            return ret

        return dfs(root, 'root')
