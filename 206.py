# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode], prev_node: Optional[ListNode]):
            if node == None:
                return None
            if node.next == None:
                return ListNode(val=node.val, next=prev_node)

            if prev_node == None:
                # 시작노드가 끝노드가 됨
                new_node = ListNode(val=node.val, next=None)
            else:
                new_node = ListNode(val=node.val, next=prev_node)

            return reverse(node.next, new_node)

        return reverse(node=head, prev_node=None)
