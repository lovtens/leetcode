# https://leetcode.com/problems/reorder-list/
# recursion
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def print_as_list(node: Optional[ListNode]) -> None:
            values = []
            now = node
            while now:
                values.append(str(now.val))
                now = now.next
            print(" ".join(values))

        reverse_order_stack = []
        node = head
        while True:
            if node == None:
                break
            reverse_order_stack.append(node)
            node = node.next

        cur_node = head
        while True:
            # print_as_list(head)
            # print(cur_node.val)
            if cur_node is reverse_order_stack[-1]:
                return
            if cur_node.next is reverse_order_stack[-1]:
                return
            next_node = cur_node.next
            insert_node = reverse_order_stack.pop()
            reverse_order_stack[-1].next = None
            insert_node.next = next_node
            cur_node.next = insert_node
            cur_node = next_node
