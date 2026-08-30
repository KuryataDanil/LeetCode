from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        res = ListNode(0, head)
        prev = res
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next

        for _ in range(right - left):
            print(res)
            next_node = cur.next
            cur.next, next_node.next, prev.next = next_node.next, prev.next, next_node

        return res.next


