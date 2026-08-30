# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def rotateRight(head, k: int):
    if not head or k == 0:
            return head

    lenHead = 1
    temp = head
    while temp.next:
        lenHead += 1
        temp = temp.next

    k = k % lenHead

    if k == 0:
        return head

    temp = head
    for _ in range(lenHead - k - 1):
        temp = temp.next

    new_head = temp.next
    temp.next = None
    temp = new_head
    while temp.next:
        temp = temp.next

    temp.next = head

    return new_head
    
        
