# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeNthFromEnd(head, n: int):
    lenHead = 0
    temp = head
    while temp:
        lenHead += 1
        temp = temp.next
    if lenHead == n:
        return head.next
    temp = head
    for _ in range(lenHead - n - 1):
        temp = temp.next

    temp.next = temp.next.next
    return head