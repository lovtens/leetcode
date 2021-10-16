# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# two pointer linked list

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # fast slow
        fast = head
        for _ in range(n):
            fast = fast.next

        # [1,2,3] 3
        if fast == None:
            return head.next

        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


