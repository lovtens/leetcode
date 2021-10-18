# https://leetcode.com/problems/validate-binary-search-tree/
# binary-search-tree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root: TreeNode, max_value: int, min_value: int):
            if root.val >= max_value or root.val <= min_value:
                return False

            ret = True
            if root.left:
                ret = ret and validate(root.left, min(max_value, root.val), min_value)

            if root.right:
                ret = ret and validate(root.right, max_value, max(min_value, root.val))

            return ret

        return validate(root, 2 ** 31, -2 ** 31 - 1)
