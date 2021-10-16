# https://leetcode.com/problems/binary-tree-level-order-traversal/
# bfs
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = [[]]
        current_level = 0
        q = deque()
        if root:
            q.append((root, 0))
        else:
            return []
        while q:
            node, level = q.popleft()
            if level > current_level:
                current_level = level
                ret.append([])

            ret[-1].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return ret
