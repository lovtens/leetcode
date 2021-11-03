# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# dfs
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], path: List[str]):
            if not node.left and not node.right:
                return int("".join(path))
            else:
                ret = 0
                if node.left:
                    ret += dfs(node.left, path + [str(node.left.val)])
                if node.right:
                    ret += dfs(node.right, path + [str(node.right.val)])
                return ret

        return dfs(root, [str(root.val)])


