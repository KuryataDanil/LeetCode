from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        prev = res
        cur = prev.next
        n = 0
        while head:
            n += 1
            head = head.next

        for _ in range(n // k):
            for _ in range(k - 1):
                next_node = cur.next
                cur.next, next_node.next, prev.next = next_node.next, prev.next, next_node
            prev = cur
            cur = prev.next

        return res.next