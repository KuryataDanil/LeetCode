# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def deleteDuplicates(head):
    temp = ListNode(0)
    temp.next = head
    cur = temp

    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            duplicate_val = cur.next.val
            while cur.next and cur.next.val == duplicate_val:
                cur.next = cur.next.next
        else:
            cur = cur.next

    return temp.next
